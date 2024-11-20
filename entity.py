class Entity:
    def __init__(self, x:int, y:int, world, sign="", deadly=False) -> None:
        self.__x = x #dont write to __x/__y directly
        self.__y = y
        #ganz oben links ist (x,y)=(0,0)
        self.sign = sign
        self.deadly = deadly

        self.world = world
        world.add(self)


    def move(self, direction:str):
        assert direction in ["UP", "DOWN", "LEFT", "RIGHT"]

        if direction == "UP" and self.isMoveAllowed("UP"):
            self.__y -= 1
        elif direction == "DOWN" and self.isMoveAllowed("DOWN"):
            self.__y += 1
        elif direction == "LEFT" and self.isMoveAllowed("LEFT"):
            self.__x -= 1
        elif direction == "RIGHT" and self.isMoveAllowed("RIGHT"):
            self.__x += 1
        else:
            print("move not allowed (dir=", direction, ",x=", self.__x, ",y=", self.__y, ")")
        
        self.world.checkGameOver()

    def isMoveAllowed(self, direction:str):
        return direction in self.getAllowedMoves()

    def getAllowedMoves(self) -> list[str]:
        moves = []
        if self.__x > 0:
            moves.append("LEFT")
        if self.__x < self.world.width-1:
            moves.append("RIGHT")
        if self.__y > 0:
            moves.append("UP")
        if self.__y < self.world.height-1:
            moves.append("DOWN")
        return moves

    @property
    def coordinates(self):
        return {"x": self.__x, "y": self.__y}

    def __str__(self) -> str:
        return "entity"