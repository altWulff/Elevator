import random
from collections import deque


class Building:
    def __init__(self, floors_amount: int):
        self.floors_amount = floors_amount
        for f in range(1, self.floors_amount):
            setattr(self, f"{f}", Floor(f, self.floors_amount))

        self.elevator = Elevator(self.floors_amount)

    def __getitem__(self, item):
        return self.__dict__[item]


class Floor:
    def __init__(self, curr_floor, floors_amount):
        self.curr_floor = curr_floor
        self.passengers = [
            Passenger(floors_amount) for _ in range(random.randrange(0, 10))
        ]

    def __repr__(self):
        return ", ".join(map(str, self.passengers))

    def to_elevator(self, elevator):
        if elevator.current_floor == self.curr_floor:
            for p in self.passengers:
                elevator.add_passenger(p)


class Elevator:
    def __init__(self, floors_amount, direction="up"):
        self.floors_amount: int = floors_amount
        self.direction: str = direction
        self.max_passenger: int = 5
        self.current_floor: int = 1
        self.passengers: deque = deque(maxlen=self.max_passenger)

    def add_passenger(self, passenger):
        if len(self.passengers) >= self.max_passenger:
            return
        self.passengers.append(passenger)

    def exit_passenger(self, passenger):
        if self.passengers:
            self.passengers.remove(passenger)

    def __repr__(self):
        if self.direction == "up":
            direction = "^"
        else:
            direction = "v"
        destination = f"to {self.destination_floor}"
        return f"{destination}|{direction} {list(self.passengers)} {direction}"

    def move_up(self, to_floor: int = 1):
        to_floor -= 1
        self.current_floor += to_floor

    def move_down(self, to_floor: int = 1):
        self.current_floor -= to_floor

    def move(self):
        """Move elevator, default its up"""
        if self.floors_amount == self.current_floor:
            self.direction = "down"
        if self.direction == "up":
            self.move_up(self.destination_floor)
        else:
            self.move_down()

    @property
    def destination_floor(self) -> int:
        floors = [f.dest_floor for f in self.passengers]
        try:
            return max(floors)
        except ValueError:
            return 1


class Passenger:
    def __init__(self, floors_amount):
        self.floors_amount: int = floors_amount
        self.curr_floor: int = random.randrange(1, floors_amount)
        self.dest_floor: int = random.randrange(1, floors_amount)

    def __repr__(self):
        return f"<{self.dest_floor}>"
