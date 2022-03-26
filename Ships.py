class Ships:
    def __init__(self, positions=None, size=0, count=0):
        if positions is None:
            positions = []
        self.size = size
        self.count = count
        self.positions = positions


class Carrier:
    Ships.size = 0
    Ships.count = 0
    Ships.positions = []


class BattleShip:
    Ships.size = 0
    Ships.count = 0
    Ships.positions = []


class Cruiser:
    Ships.size = 0
    Ships.count = 0
    Ships.positions = []


class Submarine:
    Ships.size = 0
    Ships.count = 0
    Ships.positions = []


class Destroyer:
    Ships.size = 0
    Ships.count = 0
    Ships.positions = []


class PlayersStat:
    pass


class HitShips:
    pass
