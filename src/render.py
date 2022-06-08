"""Module for render classes"""

from rich.console import Console


class Render:
    """Base render"""

    console = Console()
    style = "bold white"

    @staticmethod
    async def view_floor(building, numer_floor):
        """Display passengers and elevator on floor"""
        if building.elevator.current_floor == int(numer_floor):
            elevator = str(building.elevator).center(30, "_")
        else:
            elevator = "".center(30, "_")
        exit_passengers = str(building[numer_floor].exit_passengers)
        result = f"{exit_passengers.center(3)} | {elevator} | {building[numer_floor]}"
        return result

    @staticmethod
    async def view_building(building):
        """Display all floors"""
        floors_amount = building.floors_amount
        for i in reversed(range(1, floors_amount)):
            Render.console.print(
                await Render.view_floor(building, str(i)), style=Render.style
            )

    @staticmethod
    async def start_line(step_number: int):
        """Title line, with step execution number"""
        fill_space = 43
        sign = "*"
        Render.console.print(
            str(f" Step {step_number} ").center(fill_space, sign),
            style=Render.style,
            end="\n",
        )
