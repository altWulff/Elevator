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
        exit_passengers = str(building[numer_floor].exit_passengers)

        result = f"{exit_passengers.center(3)}| {elevator.center(10)} | {building[numer_floor]}"
        return result

    @staticmethod
    def view_building(building):
        """Display all floors"""
        floors_amount = building.floors_amount
        for i in reversed(range(1, floors_amount)):
            print(Render.view_floor(building, str(i)))
