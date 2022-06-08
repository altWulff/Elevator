"""Module for render classes"""

from rich.console import Console


class Render:
    """Base render"""

    console = Console()

    @staticmethod
    async def view_floor(building, numer_floor):
        """Display passengers and elevator on floor"""
        if building.elevator.current_floor == int(numer_floor):
            elevator = str(building.elevator)
        else:
            elevator = " "
        exit_passengers = str(building[numer_floor].exit_passengers)

        result = f"{exit_passengers.center(3)} | {elevator.center(30)} | {building[numer_floor]}"
        return result

    @staticmethod
    async def view_building(building):
        """Display all floors"""
        floors_amount = building.floors_amount
        for i in reversed(range(1, floors_amount)):
            Render.console.print(
                await Render.view_floor(building, str(i)), style="bold white"
            )
