import json

from agent import Agent

class World:
    def __init__(self, width:int, height:int, gameOverFunc) -> None:
        self.width = width
        self.height = height
        self.entities = []
        self.gameoverFunc = gameOverFunc
        
    @property
    def rooms(self):
        rooms = [[{"attributes": [], "entities": []} for a in range(0, self.width)] for b in range(0,self.height)]
        for obj in self.entities:
            rooms[obj.coordinates["y"]][obj.coordinates["x"]]["entities"].append(obj)
        self.updateAdjacentRooms(rooms)

        return rooms

    def __str__(self) -> str:
        string = ""
        for row in self.rooms:
            string += "["
            for room in row:
                string+="[attr:"
                string+= "[" + ", ".join(map(str, room["attributes"])) + "]"
                string+=","
                string+="ent:"
                string+= "[" + ", ".join(map(str, room["entities"])) + "]"
                string+="], "
            string+="]\n"
        return string

    def add(self, entity):        
        assert entity.coordinates["x"] < self.width and entity.coordinates["y"] < self.height

        self.entities.append(entity)

    def updateAdjacentRooms(self, rooms):
        for i in range(self.width):
            for j in range(self.height):
                for entity in rooms[i][j]["entities"]:
                    if entity.sign != "":
                        neighbors = [(i - 1, j), (i + 1, j),(i, j - 1),(i, j + 1),]

                        for x, y in neighbors:
                            if 0 <= x < self.width and 0 <= y < self.height and not entity.sign in rooms[x][y]["attributes"]:
                                rooms[x][y]["attributes"].append(entity.sign)
        
    def __getCurrentRoom(self, agent):
        return self.rooms[agent.coordinates["y"]][agent.coordinates["x"]]
    
    def checkOutCurrentRoom(self, agent):
        room = self.__getCurrentRoom(agent)
        return {"attributes": room["attributes"], "entities": [str(e) for e in room["entities"]]}
    
    def checkGameOver(self):
        for entity in self.entities:
            if isinstance(entity, Agent):
                for entity in self.__getCurrentRoom(entity)["entities"]:
                    if entity.deadly:
                        self.gameoverFunc()

