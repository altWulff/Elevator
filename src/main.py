import random

from src.elevator import Building
from src.render import Render


def main():
    floors_amount = random.randrange(5, 20)
    b = Building(floors_amount)
    r = Render()
    for i in reversed(range(1, floors_amount)):
        b[str(i)].to_elevator(b.elevator)
        print(r.view_floor(b, str(i)))
        b.elevator.move()
    print("--" * 10, end="\n")

    for i in reversed(range(1, floors_amount)):
        b[str(i)].to_elevator(b.elevator)
        print(r.view_floor(b, str(i)))
        b.elevator.move()
    print("--" * 10, end="\n")

    for i in reversed(range(1, floors_amount)):
        b[str(i)].to_elevator(b.elevator)
        print(r.view_floor(b, str(i)))
        b.elevator.move()
    print("--" * 10, end="\n")

    for i in reversed(range(1, floors_amount)):
        b[str(i)].to_elevator(b.elevator)
        print(r.view_floor(b, str(i)))
        b.elevator.move()
    print("--" * 10, end="\n")

    # b.elevator.move()
    #
    # for i in reversed(range(1, floors_amount)):
    #     print(r.view_floor(b, str(i)))


if __name__ == "__main__":
    main()
