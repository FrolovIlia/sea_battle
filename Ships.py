class Ship:

    def __init__(self, positions: list, name: str, padded_pos=None):
        ship_length = len(positions)
        if padded_pos is None:
            padded_pos = []
            self.ship_length = ship_length
            self.padded_pos = padded_pos
            self.name = name
            self.positions = positions

    # попадание в пределы корабля
    def shot_at_ship(self, shot):
        if shot in self.positions:
            return True
        else:
            return False

    # подбитие корабля
    def hit_at_ship(self, shot):
        if self.shot_at_ship(shot) is True and shot not in self.padded_pos:
            self.padded_pos.append(shot)
            return True
        else:
            return False

    # количество подбитий у корабля
    def counter_hits(self):
        return len(self.padded_pos)

    # уничтожение корабля
    def ship_dead(self):
        if self.ship_length == len(self.padded_pos):
            return True
        else:
            return False

    def __repr__(self):
        return "s"
