from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


class DataError(Exception):
    pass


async def button_builder(
    raw: list[list | str], deep: bool = True
) -> list[list | KeyboardButton]:
    buttons = []
    for i in raw:
        if isinstance(i, str):
            i = [KeyboardButton(text=i)] if deep else KeyboardButton(text=i)
            buttons.append(i)
        elif isinstance(i, list) and deep:
            buttons.append(await button_builder(i, deep=False))
        else:
            raise DataError("Raw data type error: list[list|str]")
    return buttons


async def keybord_build(raw: list[list | str]) -> ReplyKeyboardMarkup:
    buttons = await button_builder(raw)
    keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    return keyboard


if __name__ == "__main__":
    import asyncio

    print(asyncio.run(keybord_build(["Hello", "world"])))
