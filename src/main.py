"""Main module"""

import random
import asyncio

from elevator import Building
from render import Render


async def main(floors_amount: int | None = None, loop: int = 50):
    """This function run main program"""
    if not floors_amount:
        floors_amount: int = random.randrange(5, 20)
    building = Building(floors_amount)
    render = Render()

    for _ in range(loop):
        await render.view_building(building)
        print(str(f" Step {_} ").center(50, "*"), end="\n")
        await building.run()


if __name__ == "__main__":
    from pyfiglet import Figlet
    custom_fig = Figlet(font='graffiti')
    
    print(custom_fig.renderText('Elevator'))

    FLOORS_INPUT = int(input("How many building floor? (default range 5-20): "))
    print('\n')
    if not FLOORS_INPUT:
        FLOORS_INPUT = None
    asyncio.run(main(FLOORS_INPUT))
