from sympy import symbols, sqrt, tan
import numpy as np

k = 2
m = 0.1
a = 0.6

approx = (0.354, 0.68)

x = symbols('x:2')
y_1 = tan(x[0]*x[1] + m) - x[0]
y_2 = a*x[0]**2 + 2*x[1]**2 - 1


def get_system():
    return np.array([
        [
            y_1,
            y_2
        ],
        [
            tan(x[0]*x[1] + m),
            sqrt((1 - a*x[0]**2) / 2)
        ]
    ])
