import numpy as np
GRADIENTS = ['lerp']

def lerp(num: int, color0: list = [0, 0, 0], color1: list = [255, 255, 255], reverse: bool=False): #RGB values
    grad = []
    t = range(num-1, -1, -1)
    delta = 1/(num-1)
    t = list(map(lambda x: 1-x*delta, t))
    for i in t:
        grad.append([int(color0[0]*(1-i) + color1[0]*i),int(color0[1]*(1-i) + color1[1]*i),int(color0[2]*(1-i) + color1[2]*i)])
    if reverse:
        return list(reversed(grad))
    else:
        return grad