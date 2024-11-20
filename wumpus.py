from entity import Entity

class Wumpus(Entity):
    def __init__(self, x: int, y: int, world) -> None:
        super().__init__(x, y, world, "smell", True)

    def __str__(self) -> str:
        return "Wumpus"