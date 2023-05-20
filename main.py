import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sympy import *
from math import sqrt, pow


class Muller:
    def __init__(self, fx, x0, x1, x2, ex):
        self.fx = fx # Ecuación
        self.x0 = x0 # Valor inicial de x
        self.x1 = x1 # Valor medio de x
        self.x2 = x2 # Valor final de x
        self.ex = ex # Margen de error hasta el que se desea iterar

        # Valores a calcular:
        self.x3 = 0
        self.h0 = 0
        self.h1 = 0
        self.fx0 = 0
        self.fx1 = 0
        self.fx2 = 0
        self.s0 = 0
        self.s1 = 0
        self.a = 0
        self.b = 0
        self.c = 0
        self.currentError = 0 # Margen de error de las iteraciones

        # Letra a emplear como variable:
        self.x = symbols("x")

    def findIterations(self):
        self.evalFunctions()
        self.findHValues()
        self.findSigmaValues()
        self.findQEquationValues()
        self.findNewValue()
        self.findAproxError()
        self.saveValuesToList()
        self.resetValues()

    def evalFunctions(self):
        # Evaluar los f(xn)
        self.fx = sympify(self.fx)
        self.fx0 = round(self.fx.subs(self.x, self.x0), 5)
        self.fx1 = round(self.fx.subs(self.x, self.x1), 5)
        self.fx2 = round(self.fx.subs(self.x, self.x2), 5)

    def findHValues(self):
        # Obtener los valores para h
        self.h0 = self.x1 - self.x0
        self.h1 = self.x2 - self.x1

    def findSigmaValues(self):
        # Obtener los valores de sigma
        self.s0 = (self.fx1 - self.fx0) / (self.x1 - self.x0)
        self.s1 = (self.fx2 - self.fx1) / (self.x2 - self.x1)

        self.s0 = round(self.s0, 5)
        self.s1 = round(self.s1, 5)

    def findQEquationValues(self):
        # Obtener el valor de a:
        self.a = round((self.s1 - self.s0) / (self.h1 - self.h0), 5)

        # Obtener el valor de b:
        self.b = (self.a * self.h1) + self.s1
        self.b = round(self.b, 5)

        # Obtener c:
        self.c = self.fx2

    def findNewValue(self):
        if self.b > 0:
            self.x3 = round(self.x2 + (-2 * self.c) / (self.b + sqrt(pow(self.b, 2) - 4 * self.a * self.c)), 5)
        else:
            self.x3 = round(self.x2 + (-2 * self.c) / (self.b - sqrt(pow(self.b, 2) - 4 * self.a * self.c)), 5)

    def findAproxError(self):
        self.currentError = abs(((self.x3 - self.x2) / self.x3) * 100)

    def resetValues(self):
        self.x0 = self.x1
        self.x1 = self.x2
        self.x2 = self.x3

        # Repetiremos el proceso mientras el error obtenido sea mayor que el solicitado
        while self.currentError > self.ex:
            self.findIterations()

    def saveValuesToList(self):
        print("x0: ", self.x0)
        print("x1: ", self.x1)
        print("x2: ", self.x2)
        print("h0: ", self.h0)
        print("h1: ", self.h1)
        print("s0: ", self.s0)
        print("s1: ", self.s1)
        print("a: ", self.a)
        print("b: ", self.b)
        print("c: ", self.c)
        print("x3: ", self.x3)
        print("E: ", self.currentError)
        print("*" * 50)


def main():
    fx = input("Ingresa la función a evaluar (en términos de x): ")
    x0 = float(input("Ingresa el valor de X0: "))
    x1 = float(input("Ingresa el valor de X1: "))
    x2 = float(input("Ingresa el valor de X2: "))
    ex = float(input("Margen de error minimo permitido: "))

    m = Muller(fx, x0, x1, x2, ex)
    m.findIterations()

if __name__ == "__main__":
    main()
