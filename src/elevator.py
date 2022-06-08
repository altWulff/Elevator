"""
Module contain Building, Floor, Elevator and Passenger classes
"""

import random


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


class Elevator:
    """Elevator class"""

    def __init__(self, floors_amount: int, direction: str = "up"):
        self.floors_amount: int = floors_amount
        self.direction: str = direction
        self.max_passenger: int = 5
        self.current_floor: int = 1
        self.passengers: list = []

    async def is_max_passengers(self) -> bool:
        """Check maximum passenger in elevator"""
        return len(self.passengers) >= self.max_passenger

    async def add_passenger(self, passenger: Passenger) -> None:
        """Add passenger from elevator"""
        self.passengers.append(passenger)

    async def exit_passenger(self, passenger) -> None:
        """Remove passenger from elevator"""
        indx = self.passengers.index(passenger)
        self.passengers.pop(indx)

    def __repr__(self) -> str:
        if self.direction == "up":
            direction = "^"
        else:
            direction = "v"
        return f"| {direction} {self.passengers} {direction} |"

    async def move_up(self, to_floor: int = 1) -> None:
        """
        Move up elevator
        :param to_floor: default 1
        :return: None
        """
        self.current_floor += to_floor

    async def move_down(self, to_floor: int = 1) -> None:
        """
        Move down elevator
        :param to_floor: default 1
        :return: None
        """
        self.current_floor -= to_floor

    async def move(self) -> None:
        """Move elevator, default its up"""
        if self.current_floor == 1:
            self.direction = "up"

        if self.direction == "up":
            if self.current_floor < self.floors_amount - 1:
                await self.move_up()
            else:
                self.direction = "down"
        else:
            await self.move_down()

    @property
    def destination_floor(self) -> int:
        """
        Elevator destination floor, max value from passengers destination
        default destination: current + 1
        """
        floors = [f.destination_floor for f in self.passengers]
        try:
            return max(floors)
        except ValueError:
            if self.current_floor + 1 >= self.floors_amount:
                return self.current_floor - 1
            return self.current_floor + 1


class Floor:
    """Floor class"""

    def __init__(self, curr_floor: int, floors_amount: int, passengers: int) -> None:
        self.curr_floor: int = curr_floor
        self.passengers_amount: range = range(random.randrange(0, passengers))
        self.passengers: list[Passenger] = [
            Passenger(floors_amount) for _ in self.passengers_amount
        ]
        self.exit_passengers: int = 0

    def __repr__(self) -> str:
        return ", ".join(map(str, self.passengers))

    async def is_destination_floor(self, passenger) -> bool:
        """Check diff passengers to current floor"""
        return passenger.destination_floor == self.curr_floor

    async def exit_from_elevator(self, elevator: Elevator) -> None:
        """Exit passengers from elevator"""
        for passenger in elevator.passengers:
            if await self.is_destination_floor(passenger):
                self.exit_passengers += 1
                await elevator.exit_passenger(passenger)

    async def elevator_on_floor(self, elevator: Elevator):
        """Move passengers from current floor to elevator"""
        if elevator.current_floor == self.curr_floor:

            for _ in self.passengers:
                if not await elevator.is_max_passengers():
                    await elevator.add_passenger(self.passengers.pop())

            await self.exit_from_elevator(elevator)


class Building:
    """Building class"""

    def __init__(self, floors_amount: int, passengers: int) -> None:
        self.floors_amount: int = floors_amount + 1
        for num_floor in range(1, self.floors_amount):
            setattr(
                self, f"{num_floor}", Floor(num_floor, self.floors_amount, passengers)
            )

        self.elevator: Elevator = Elevator(self.floors_amount)

    def __getitem__(self, item):
        return self.__dict__[item]

    async def run(self):
        """
        Main run to other classes
        :return: None
        """
        for i in range(1, self.floors_amount):
            await self[str(i)].elevator_on_floor(self.elevator)
            if not self[str(i)].passengers or not self.elevator.passengers:
                await self.elevator.move()

        if self.elevator.current_floor != self.elevator.destination_floor:
            await self.elevator.move()
