"""Main module"""

import random

from elevator import Building
from render import Render


def main():
    """This function run main program"""
    floors_amount: int = random.randrange(5, 20)
    building = Building(floors_amount)
    render = Render()
    
    for _ in range(20):
        render.view_building(building)
        print(str("-"*40).center(20), end="\n")
        building.run()


if __name__ == "__main__":
    main()
