class Render:
    @staticmethod
    def view_floor(building, numer_floor):
        if building.elevator.current_floor == int(numer_floor):
            elevator = str(building.elevator)
        else:
            elevator = " [] "
        r = f"{numer_floor.center(4)}| {elevator.center(10)} | {building[numer_floor]}"
        return r
