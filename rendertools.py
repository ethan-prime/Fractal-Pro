import cmath
import math
from cfg import C, MAX_ITERS
from tqdm import tqdm
import random

def pixel_map(img_size: tuple, x_range: tuple, y_range: tuple, pixel: tuple) -> tuple:
    delta_x = (x_range[1]-x_range[0])/img_size[0]
    delta_y = (y_range[1]-y_range[0])/img_size[1]
    map = (x_range[0]+(pixel[0]-x_range[0])*delta_x, y_range[0]+(pixel[1]-y_range[0])*delta_y) 
    return map

def render(img_size: tuple, x_range: tuple, y_range: tuple, fractal, samples: int = 1, c = C, max_iters = MAX_ITERS) -> list[list]:
    canvas = []
    for j in tqdm(range(img_size[1])):
        canvas.append([0]*img_size[0])
        for i in range(img_size[0]):
            p = pixel_map(img_size, x_range, y_range, (i, j))
            if samples > 1:
                num = 0
                delta_x = (x_range[1]-x_range[0])/img_size[0]
                delta_y = (y_range[1]-y_range[0])/img_size[1]
                for _ in range(samples):
                    z = complex(p[0]+delta_x*.5*(random.random()-0.5), p[1]+delta_y*.5*(random.random()-0.5))
                    num += fractal(z, c, max_iters)
                num = num/samples
                canvas[j][i] = num
            else:
                z = complex(p[0], p[1])
                num = fractal(z, c, max_iters)
                canvas[j][i] = num
    return canvas
