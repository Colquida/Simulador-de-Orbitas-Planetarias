import numpy as np
import matplotlib.pyplot as plt

import simulator
import Cy_simulator
import time
import sys


def call_simulator(simulator):
    AU = (149.6e6 * 1000)
    sun = simulator.Body()
    sun.name = 'Sun'
    sun.mass = 1.98892 * 10**30

    earth = simulator.Body()
    earth.name = 'Earth'
    earth.mass = 5.9742 * 10**24
    earth.px = -1 * AU
    earth.vy = 29.783 * 1000

    venus = simulator.Body()
    venus.name = 'Venus'
    venus.mass = 4.8685 * 10**24
    venus.px = 0.723 * AU
    venus.vy = -35.02 * 1000

    simulator.loop([sun, earth, venus])


def main():
    start = time.time()
    call_simulator(simulator)
    tiempoPy = time.time() - start

    start = time.time()
    call_simulator(Cy_simulator)
    tiempoCy = time.time() - start

    speedUp = round(tiempoPy/tiempoCy, 3)
    print(f"Tiempo en Python: {tiempoPy} \n")
    print(f"Tiempo en Cython: {tiempoCy} \n")
    print(f"SpeedUp: {speedUp} \n")
    return tiempoPy, tiempoCy
	
		


if __name__ == '__main__':
    tiempoPy, tiempoCy = main()
    tiempos = [tiempoPy,tiempoCy]
    etiquetas = ['Tiempo Python','Tiempo Cython']
    fig, ax = plt.subplots() 
    ax.set_ylabel("Tiempo")
    plt.bar(etiquetas, tiempos, width=0.3, color=["crimson", "orange"], align='center')
    plt.savefig('graficaTiempos.png')
    plt.grid()
    plt.show()
