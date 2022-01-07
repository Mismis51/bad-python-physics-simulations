import os
import time

class Renderer:
    def __init__(self, iSimulation):
        self.simulation = iSimulation
        self.grid = [[" " for _ in range(iSimulation.size[0])] for _ in range(iSimulation.size[1])]

    def _clearScreen(self):
        if os.name in ('nt', 'dos') : os.system('cls')
        else : os.systetm('clear')


    def _renderPosition(self):
        x, y = self.simulation.position
        # if x > self.simulation.size[0] or y > self.simulation.size[1]:
        #     self.grid[self.simulation.size[0]][self.simulation.size[1]] = "x"
        # else:
        #     self.grid[x][y] = "x"
        # for line in self.grid:print(line)
        # if x > self.simulation.size[0] or y > self.simulation.size[1]:
        #     self.grid[self.simulation.size[0]][self.simulation.size[1]] = " "
        # else:
        #     self.grid[x][y] = " "
        print(x, y)

    def renderSimulation(self):
        while True:
            self.simulation.updateSimulation()
            self._renderPosition()
            time.sleep(1)
            self._clearScreen()
    