import asyncio

async def start_strongman(name, power):
    number_of_ball = 5
    for _ in range(1, number_of_ball+1):
        print(f'Силач {name} начал соревнования.')
        await asyncio.sleep(1/power)
        print(f'Силач {name} поднял {_} шар')
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    task_1 = asyncio.create_task(start_strongman('Pasha', 3))
    task_2 = asyncio.create_task(start_strongman('Denis', 4))
    task_3 = asyncio.create_task(start_strongman('Apollon', 5))
    await task_1
    await task_2
    await task_3

asyncio.run(start_tournament())
