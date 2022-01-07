import src.physics
from math import pi
from time import time, sleep

class Simulation:
    def __init__(self, gravity=-9.8, initial_position=[0, 0], initial_velocity=100, angle=45, sim_speed=1, sleep_time=0.1):
        self.object = src.physics.ObjectTrajectory(gravity, initial_position, initial_velocity, angle / 180 * pi)
        self.sim_speed = sim_speed
        self.sleep_time = sleep_time
        self.positions = list()

    def runSimulation(self):
        wCurrentTime = time()
        wStartTime = wCurrentTime
        while self.object.position[1] >= 0:
            self.object.updateObject((time() - wCurrentTime) * self.sim_speed)
            wCurrentTime = time()
            self.positions.append([self.object.position.copy(), (wCurrentTime - wStartTime) * self.sim_speed])
            sleep(self.sleep_time)