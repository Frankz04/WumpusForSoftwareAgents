from world import World
import random
from wumpus import Wumpus
from agent import Agent
from pit import Pit

HEIGHT = 4
WIDTH = 4
ENTITIES = [Agent, *[Wumpus]*2, *[Pit]*2]

class Game:
    def __init__(self) -> None:
        self.world = World(WIDTH, HEIGHT, self.gameOver)        
        self.agents = []

        self.spawnEntities()
        

    def spawnEntities(self):
        all_rooms = [(i, j) for i in range(HEIGHT) for j in range(WIDTH)]

        assert len(ENTITIES) < len(all_rooms), "Not enough rooms for entities"
    
        rooms = random.sample(all_rooms, len(ENTITIES))

        for index, entity in enumerate(ENTITIES):
            if entity == Agent:
                self.agents.append(entity(*rooms[index], self.world))
            else:
                entity(*rooms[index], self.world)
                            
    def gameOver(self):
        print("GAME OVER")
        exit(0)

if __name__ == "__main__":
    game = Game()

    for agent in game.agents:
        agent.loop()
