from entity import Entity

class Agent(Entity):
    def __init__(self, x: int, y: int, world) -> None:
        super().__init__(x, y, world)
        self.arrows = 5

    def shootArrow(direction: str):
        pass

    @property
    def currentSituation(self):
        return self.world.checkOutCurrentRoom(self)

    def __str__(self) -> str:
        return "Agent"

    def loop(self):
        print("DO SOMETHING")
        print(self.currentSituation)
        self.move("UP")
