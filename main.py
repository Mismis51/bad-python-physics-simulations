from src import Simulation
import matplotlib.pyplot as plt
from time import time

if __name__ == '__main__':
    wSimulation = Simulation(sim_speed=1)
    wStart_time = time()
    print(f'Starting simulation at {wStart_time}')
    wSimulation.runSimulation()
    print(f'Simulation ended. Real Time : {time() - wStart_time}')
    x_p = list()
    y_p = list()
    for i in wSimulation.positions:
        y_p.append(i[0][1])
        x_p.append(i[1])
    plt.plot(x_p, y_p)
    plt.show()