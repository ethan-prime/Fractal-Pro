from rendertools import *
from PIL import Image
from gradient import lerp, GRADIENTS
from fractals import *
import numpy as np
import os
from cfg import INSTALLATION_PATH
from natsort import natsorted
import cv2
from concurrent.futures import ProcessPoolExecutor

FRACTALS_DICT = {
    'julia':julia,
    'loader':None,
    'burning_ship':burning_ship,
    'julia_log':julia_log,
    'julia_exp':julia_exp,
    'burning_ship_log':burning_ship_log,
    'burning_ship_exp':burning_ship_exp,
    'mandelbrot':mandelbrot
}

def handle_lerps(parts):
    grad = []
    for part in parts:
        grad += lerp(part[0], part[1], part[2])
    return grad

class Fractal:
    def __init__(self, fractal_name: str):
        if fractal_name.lower() not in FRACTALS_DICT.keys():
            raise Exception('Fractal not found.')
        else:
            self.fractal_name = FRACTALS_DICT[fractal_name.lower()]
        self.pixels = []
        self.temp_pixels = []
        self.image = None
        self.grad = []
        self.batches = []
    
    def calculate_batches(self, img_size: tuple, x_range: tuple, y_range: tuple, samples: int = 1, c = C, max_iters = MAX_ITERS):
        scale_factor = 100/img_size[1] #400p resolution
        img_size = (int(img_size[0]*scale_factor), int(img_size[1]*scale_factor))
        self.get_pixels('NOSAVE', img_size=img_size, x_range=x_range, y_range=y_range, samples=samples, c=c, max_iters=max_iters)
        batches = []
        sum = 0
        for y in range(len(self.pixels)):
            for x in range(len(self.pixels[y])):
                sum += self.pixels[y][x]
        sum = sum/10 #10 threads?
        batch_sum = 0
        for y in range(len(self.pixels)):
            for x in range(len(self.pixels[y])):
                batch_sum += self.pixels[y][x]
            if batch_sum >= sum:
                batches.append(int((y+1)/scale_factor))
                batch_sum = 0
            if len(batches) == 9:
                break
        batches = [-1] + batches
        batches.append(int(img_size[1]/scale_factor))
        for i in range(len(batches)-1, 0, -1):
            batches[i] = [batches[i-1]+1, batches[i]]
        batches = batches[1:]
        self.batches = batches

    def get_pixels_from_batches(self, filename: str, img_size: tuple, x_range: tuple, y_range: tuple, samples: int = 1, c = C, max_iters = MAX_ITERS):
        print(img_size)
        delta_y = y_range[1]-y_range[0]
        with ProcessPoolExecutor() as executor:
            img_nsize = []
            x_range = [x_range for _ in range(10)]
            y_nrange = []
            fractal = [self.fractal_name for _ in range(10)]
            samples = [samples for _ in range(10)]
            c = [c for _ in range(10)]
            max_iters = [max_iters for _ in range(10)]
            for i, batch in enumerate(self.batches):
                if i == 0:
                    img_nsize.append((img_size[0], batch[1]-batch[0]))
                    y_nrange.append((y_range[0],y_range[0]+(batch[1]/img_size[1])*delta_y))
                else:
                    img_nsize.append((img_size[0], batch[1]-batch[0]+1))
                    y_nrange.append((y_range[0]+(batch[0]/img_size[1])*delta_y,y_range[0]+(batch[1]/img_size[1])*delta_y))
            results = executor.map(render, img_nsize, x_range, y_nrange, fractal, samples, c, max_iters)
            for j, result in enumerate(results):
                if j == 0:
                    final = result
                else:
                    final += result
        np.save(os.path.join(INSTALLATION_PATH, filename),final)
        self.pixels = final

    def get_pixels(self, filename: str, img_size: tuple, x_range: tuple, y_range: tuple, samples: int = 1, c = C, max_iters = MAX_ITERS) -> None:
        pixels = render(img_size, x_range, y_range, fractal=self.fractal_name, samples=samples, c=c, max_iters=max_iters)
        print(filename)
        if filename.lower() != 'nosave':
            np.save(os.path.join(INSTALLATION_PATH, filename),pixels)
        self.pixels = pixels

    def load_pixels(self, filename: str):
        if self.pixels == []:
            self.pixels = np.load(os.path.join(INSTALLATION_PATH, filename)).tolist()
            return self.pixels

    def to_image(self, pixels: list[float], grad: list=lerp(250), show: bool=False, save: bool=False, temp: bool=False):
        print('Adding color...')
        new = []
        for y in tqdm(range(len(pixels))):
            new.append([[]]*len(pixels[y]))
            for x in range(len(pixels[y])):
                new[y][x] = grad[int(pixels[y][x]*(len(grad)-1))]
        new = np.array(new, dtype="uint8")
        img = Image.fromarray(new, mode="RGB")
        if save:
            if show:
                img.show()
            n = int(natsorted(os.listdir(os.path.join(INSTALLATION_PATH, 'results')))[-1].split('.')[0])+1
            img.save(os.path.join(os.path.join(INSTALLATION_PATH, 'results'), f'{n}.png'))
        if temp:
            img.save(os.path.join(INSTALLATION_PATH, 'static','temp','temp.png'))
        self.image = img
        return img