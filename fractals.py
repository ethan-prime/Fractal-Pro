import math
import cmath
import numpy as np

def julia(z: complex, c: complex, max_iterations: int) -> float:
    for i in range(1, max_iterations):
        z = z**2+c
        if abs(z) > 2:
            return i/max_iterations
    return 1

def julia_log(z: complex, c: complex, max_iterations: int) -> float:
    for i in range(1, max_iterations):
        z = z**2+c
        if abs(z) > 2:
            return np.log(i)/max_iterations
    return 1

def julia_exp(z: complex, c: complex, max_iterations: int) -> float:
    for i in range(1, max_iterations):
        z = z**2+c
        if abs(z) > 2:
            return np.exp(-i/max_iterations)
    return 1

def burning_ship(c: complex, opt, max_iterations: int) -> float:
    z = 0
    for i in range(1, max_iterations):
        z = (complex(abs(z.real), abs(z.imag)))**2 + c
        if abs(z) > 2:
            return i/max_iterations
    return 1

def burning_ship_log(c: complex, opt, max_iterations: int) -> float:
    z = 0
    for i in range(1, max_iterations):
        z = (complex(abs(z.real), abs(z.imag)))**2 + c
        if abs(z) > 2:
            return np.log(i)/max_iterations
    return 1

def burning_ship_exp(c: complex, opt, max_iterations: int) -> float:
    z = 0
    for i in range(1, max_iterations):
        z = (complex(abs(z.real), abs(z.imag)))**2 + c
        if abs(z) > 2:
            return np.exp(-i/max_iterations)
    return 1

def mandelbrot(c: complex, opt, max_iterations: int) -> float:
    z = 0
    for i in range(1, max_iterations):
        z = z**3 + c
        if abs(z) > 2:
            return i/max_iterations
    return 1