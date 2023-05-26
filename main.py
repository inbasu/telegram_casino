import asyncio
from aiogram import Bot, Dispatcher


from hendlers import router, COMMAND_LIST

TOKEN: str = str()

ROUTER = router


async def main():
    bot: Bot = Bot(token=TOKEN, parse_mode="HTML")
    dp: Dispatcher = Dispatcher()
    dp.include_router(ROUTER)
    await bot.set_my_commands(commands=COMMAND_LIST)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())


"""ЧЕТ не Чет игра на поинты"""
