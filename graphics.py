# Desarrollado por:
# - Ulloa Serpas, Hugo Alexander - US21003
# - Vásquez Crespo, Ángel Gabriel - VC21007

import matplotlib.pyplot as plt
import numpy as np


class Graphics:
    def __init__(self, xValues, yValues, fx):
        self._x = xValues
        self._y = yValues
        self._fx = str(fx)

    def createGraphics(self):
        fig, graphics = plt.subplots()
        #x = np.linspace(round(min(self._x, 0), 0), round(max(self._x), 0), 100)
        x = np.linspace(float(round(np.amin(self._x, 0))), float(round(np.amax(self._x), 0)), 100)
        y = eval(self._fx)

        #Puntos que se acercan a la raiz:
        graphics.scatter(self._x, self._y, color="green")
        graphics.plot(x, y, color="red", label="fx")

        # Agregar las coordenadas a cada punto
        for i, (x, y) in enumerate(zip(self._x, self._y)):
            label = f'({x:.2f}, {y:.2f})'  # Formateo de cadena para mostrar solo dos decimales
            graphics.annotate(label, (x, y), textcoords="offset points", xytext=(0, 10), ha='center')

        plt.title(self._fx)
        plt.grid()
        plt.show()
