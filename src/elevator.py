"""
Module contain Building, Floor, Elevator and Passenger classes
"""

import random


class Elevator:
    """Elevator class"""

    def __init__(self, floors_amount: int, direction: str = "up"):
        self.floors_amount: int = floors_amount
        self.direction: str = direction
        self.max_passenger: int = 5
        self.current_floor: int = 1
        self.passengers: list = []

    def add_passenger(self, passenger) -> None:
        """Add passenger from elevator"""
        self.passengers.append(passenger)

    def exit_passenger(self, passenger) -> None:
        """Remove passenger from elevator"""
        self.passengers.remove(passenger)

    def __repr__(self) -> str:
        if self.direction == "up":
            direction = "^"
        else:
            direction = "v"
        destination = f"to {self.destination_floor}"
        return f"{destination} | {direction} {list(self.passengers)} {direction} |"

    def move_up(self, to_floor: int = 1) -> None:
        """
        Move up elevator
        :param to_floor: default 1
        :return: None
        """
        self.current_floor += to_floor

    def move_down(self, to_floor: int = 1) -> None:
        """
        Move down elevator
        :param to_floor: default 1
        :return: None
        """
        self.current_floor -= to_floor

    def move(self) -> None:
        """Move elevator, default its up"""
        is_not_destination = self.current_floor != self.destination_floor
        if self.floors_amount == self.current_floor:
            self.direction = "down"
        if self.current_floor == 1:
            self.direction = "up"
        if self.direction == "up":
            if is_not_destination:
                self.move_up()
        else:
            self.move_down()

    @property
    def destination_floor(self) -> int:
        """
        Elevator destination floor, max value from passengers destination
        default destination 1
        """
        floors = [f.destination_floor for f in self.passengers]
        try:
            return max(floors)
        except ValueError:
            return 1


class Floor:
    """Floor class"""

    def __init__(self, curr_floor: int, floors_amount: int) -> None:
        self.curr_floor: int = curr_floor
        self.passengers_amount: range = range(random.randrange(0, 10))
        self.passengers: list[Passenger] = [
            Passenger(floors_amount) for _ in self.passengers_amount
        ]
        self.exit_passengers: int = 0

    def __repr__(self) -> str:
        return ", ".join(map(str, self.passengers))

    def is_destination_floor(self, passenger) -> bool:
        """Check diff passenger.floor to current floor"""
        return passenger.destination_floor == self.curr_floor

    def exit_from_elevator(self, elevator: Elevator) -> None:
        """Exit passengers from elevator"""
        for passenger in elevator.passengers:
            if self.is_destination_floor(passenger) and elevator.passengers:
                self.exit_passengers += 1
                elevator.exit_passenger(passenger)

    def elevator_on_floor(self, elevator: Elevator):
        """Move passengers from current floor to elevator"""
        if elevator.current_floor == self.curr_floor:
            while (
                len(elevator.passengers) != elevator.max_passenger and self.passengers
            ):
                elevator.add_passenger(self.passengers.pop())

                self.exit_from_elevator(elevator)


class Building:
    """Building class"""

    def __init__(self, floors_amount: int) -> None:
        self.floors_amount: int = floors_amount + 1
        for num_floor in range(1, self.floors_amount):
            setattr(self, f"{num_floor}", Floor(num_floor, self.floors_amount))

        self.elevator: Elevator = Elevator(self.floors_amount)

    def __getitem__(self, item):
        return self.__dict__[item]

    def run(self):
        """
        Main run to other classes
        :return: None
        """
        for i in range(1, self.floors_amount):
            self[str(i)].elevator_on_floor(self.elevator)

        if self.elevator.current_floor != self.elevator.destination_floor:
            self.elevator.move()


class Passenger:
    """Passenger class"""

    def __init__(self, floors_amount: int):
        self.floors_amount: int = floors_amount
        self.curr_floor: int = random.randrange(1, floors_amount)
        self.set_destination_floor(floors_amount)

        while self.curr_floor == self.destination_floor:
            self.set_destination_floor(floors_amount)

    def set_destination_floor(self, floors_amount: int) -> None:
        """Set destination floor"""
        self.destination_floor: int = random.randrange(1, floors_amount)

    def __repr__(self) -> str:
        return f"{self.destination_floor}"
