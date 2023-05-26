from aiogram import Router
from aiogram import F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message


from keyboard import keybord_build
from logic import roll


router = Router()


class Game(StatesGroup):
    bid = State()
    guess = State()


@router.message(Command(commands=["start"]))
async def start_handle(message: Message, state: FSMContext) -> None:
    """This handler receive messages with `/start  command"""
    kb = await keybord_build([["Чёт", "Не чёт"], "Зеро"])
    await state.set_state(Game.bid)
    data = await state.update_data(bank=1000)
    await message.answer(
        f"""Game started
        Bank:{data['bank']}$
        Make your bid...""",
        reply_markup=kb,
    )


@router.message(Command(commands=["cancel"]))
async def cancel_handle(message: Message, state: FSMContext) -> None:
    """This handler receive messages with `/cancel` command"""
    await state.clear()
    await message.reply(text="Game over")


@router.message(Game.guess, F.text.in_(["Чёт", "Не чёт", "Зеро"]))
async def guess_handle(message: Message, state: FSMContext) -> None:
    """This handler receive messages with guess"""
    data = await state.get_data()
    point = await roll()
    if point[0] == message.text:
        mesg = "You win"
        data = await state.update_data(bank=data["bank"] + data["bid"])
    else:
        mesg = "You lose"
        data = await state.update_data(bank=data["bank"] - data["bid"])
    await message.reply(
        text=f"""
{point[1]} - {point[0]}
{mesg}  {data['bid']}$
Current bank {data['bank']}$
    """
    )
    if data["bank"] <= 0:
        await state.clear()
        await message.reply(text="Game over")
    await state.set_state(Game.bid)


@router.message(Game.bid, F.text.isdigit())
async def bid_handle(message: Message, state: FSMContext) -> None:
    """This handler receive messages with bet"""
    data = await state.update_data(bid=int(message.text))
    await message.answer(text=f"You bid {data['bid']}$")
    await state.set_state(Game.guess)
