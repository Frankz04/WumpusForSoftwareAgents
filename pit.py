from entity import Entity

class Pit(Entity):
    def __init__(self, x: int, y: int, world) -> None:
        super().__init__(x, y, world, "breeze", True)
    
    def move(self, direction: str):
        #pits cant move
        pass

    def __str__(self) -> str:
        return "Pit"