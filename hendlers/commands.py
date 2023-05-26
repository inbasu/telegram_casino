from aiogram.types.bot_command import BotCommand

COMMANDS = {
    "start": "start casino",
    "cancel": "stop game",
}


COMMAND_LIST = [
    BotCommand(command=key, description=val) for key, val in COMMANDS.items()
]
