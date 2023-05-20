import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sympy import *
from math import sqrt, pow


class Muller:
    def __init__(self, fx, x0, x1, x2, ex):
        self.fx = fx
        self.x0 = x0
        self.x1 = x1
        self.x2 = x2
        self.ex = ex

        #Valores a calcular:
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

        # Letra a usar como variable:
        self.x = symbols("x")

    def evalFunctions(self):
        # Evaluar los f(xn)
        self.fx = sympify(self.fx)
        self.fx0 = round(self.fx.subs(self.x, self.x0), 5)
        self.fx1 = round(self.fx.subs(self.x, self.x1), 5)
        self.fx2 = round(self.fx.subs(self.x, self.x2), 5)

        print("fx0: ", self.fx0)
        print("fx1", self.fx1)

        # Obtener los valores para h
        self.h0 = self.x1 - self.x0
        self.h1 = self.x2 - self.x1

        print("h0: ", self.h0)
        print("h1: ", self.h1)

        # Obtener los valores de sigma
        self.s0 = (self.fx1 - self.fx0)/(self.x1 - self.x0)
        self.s1 = (self.fx2 - self.fx1)/(self.x2 - self.x1)

        self.s0 = round(self.s0, 5)
        self.s1 = round(self.s1, 5)

        print("s0: ", self.s0)
        print("s1: ", self.s1)

        # Obtener el valor de a:
        self.a = (self.s1 - self.s0)/(self.h1 - self.h0)
        self.a = round(self.a, 5)

        # Obtener el valor de b:
        self.b = (self.a*self.h1) + self.s1
        self.b = round(self.b, 5)

        # Obtener c:
        self.c = self.fx.subs(self.x, self.x2)
        self.c = round(self.c, 5)

        print("a: ", self.a)
        print("b: ", self.b)
        print("c: ", self.c)


    def findNewValue(self):
        if self.b > 0:
            self.x3 = self.x2 + (-2*self.c)/(self.b + sqrt(pow(self.b, 2) - 4*self.a*self.c))
        else:
            self.x3 = self.x2 + (-2 * self.c) / (self.b - sqrt(pow(self.b, 2) - 4 * self.a * self.c))


    def printResult(self):
        print("x3: ", str(self.x3))


def main():
    fx = input("Ingresa la función a evaluar (en términos de x): ")
    x0 = float(input("Ingresa el valor de X0: "))
    x1 = float(input("Ingresa el valor de X1: "))
    x2 = float(input("Ingresa el valor de X2: "))
    ex = float(input("Margen de error minimo permitido: "))

    m = Muller(fx, x0, x1, x2, ex)
    m.evalFunctions()
    m.findNewValue()
    m.printResult()


if __name__ == "__main__":
    main()
