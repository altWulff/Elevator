"""Module for render classes"""


class Render:
    """Base render"""

    @staticmethod
    def view_floor(building, numer_floor):
        """Display passengers and elevator on floor"""
        if building.elevator.current_floor == int(numer_floor):
            elevator = str(building.elevator)
        else:
            elevator = " [] "
        result = (
            f"{numer_floor.center(4)}| {elevator.center(10)} | {building[numer_floor]}"
        )
        return result
