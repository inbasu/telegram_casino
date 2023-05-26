import random


async def roll():
    spoint = random.randint(0, 10)
    if spoint == 0:
        point = "Зеро"
    elif spoint % 2:
        point = "Не чёт"
    else:
        point = "Чёт"
    return (point, spoint)
