"""Main module"""

import asyncio
import random

from elevator import Building
from render import Render


async def main(floors_amount: int, steps: int = 50, passengers: int = 10):
    """This function run main program"""
    building = Building(floors_amount, passengers)
    render = Render()

    for _ in range(1, steps + 1):
        if (
            await building.get_waiting_passengers() == 0
            and not building.elevator.passengers
        ):
            await render.start_line(_)
            await render.view_building(building)
            break

        await render.start_line(_)
        await render.view_building(building)
        await building.run()

    print()


def floors_input(value=None):
    """Floors input function"""
    if value is None:
        value = input("How many building floor? (default range 5-20): ")
    try:
        return int(value)
    except ValueError:
        return random.randrange(5, 20)


def passengers_input(value=None):
    """Passengers input function"""
    if value is None:
        value = input("How many passengers in floor? (default range 0-10): ")
    try:
        return int(value)
    except ValueError:
        return random.randrange(0, 10)


if __name__ == "__main__":
    from pyfiglet import Figlet
    from rich.console import Console

    console = Console()
    custom_fig = Figlet(font="graffiti")
    TITLE = "Elevator"

    console.print(custom_fig.renderText(TITLE))

    FLOORS_INPUT = floors_input()
    PASSENGERS_INPUT = passengers_input()
    ELEVATOR_CAP = 5
    STEPS = (FLOORS_INPUT * PASSENGERS_INPUT) + ((FLOORS_INPUT * 2) * ELEVATOR_CAP)

    console.print(
        f"""Start program with parameters:
    Building floors: {FLOORS_INPUT}
    Passengers in floor: {PASSENGERS_INPUT}
    Maximum steps: {STEPS}
    ...
    """
    )
    asyncio.run(main(FLOORS_INPUT, STEPS, PASSENGERS_INPUT))
    console.print("End program.")

    input("Press Enter to exit ... ")
