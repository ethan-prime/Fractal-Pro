# Fractal Pro ![Static Badge](https://img.shields.io/badge/Python-blue) ![Static Badge](https://img.shields.io/badge/JavaScript-yellow) ![Static Badge](https://img.shields.io/badge/HTML-orange) ![Static Badge](https://img.shields.io/badge/CSS-03BAFC) ![Static Badge](https://img.shields.io/badge/Flask-7303FC)
### My fractal renderer. Made with Python, JavaScript, HTML, CSS, and Flask (among other Python libraries). You can (currently) make fractals from the [Mandelbrot Set](https://en.wikipedia.org/wiki/Mandelbrot_set), [Julia Set](https://en.wikipedia.org/wiki/Julia_set) and [Burning Ship](https://en.wikipedia.org/wiki/Burning_Ship_fractal) fractals.

# The Interface
![alt text](https://github.com/ethan-prime/fractal-renderer/blob/master/assets/interface.png)

# Installation and Launching
### First, download the repo as a zip file or run ```git clone https://github.com/ethan-prime/Fractal-Pro.git```.
### Then, make sure to specify the installation path in ```cfg.py``` (note: please include the \Fractal-Pro at the end of the path - see the example in ```cfg.py```).
### Install all requirements in requirements.txt by running ```pip install -r requirements.txt```
### Start ```flask_server.py```
### Navigate to [localhost:5000](http://localhost:5000).

# Generating Fractals
## Fractal Name: the name of the fractal function used to generate a fractal. A comprehensive list can be found in ```fractals.py```. Common values could be ```mandelbrot```, ```julia```, or ```burning_ship```.
## File Name: the name of the file that the generated fractal will be stored in. Should end with ```.npy``` (numpy file).
## Image Size: The size or resolution of the fractal generated. 
## X-Range: Range of x (real) values seen in the generated fractal.
## Y-Range: Range of y (imaginary) values seen in the generated fractal.
## Samples: Number of samples taken per pixel rendered. Higher values make the image look less jagged and sharp.
## C value (optional): Really only relevant to the [Julia Set](https://en.wikipedia.org/wiki/Julia_set). Default value can be configured in ```cfg.py```.
## Max Iterations (optional, default = 50): How many iterations of the formula to perform before assigning numerical value to each pixel (if not already terminated). Generally, use higher values for more detailed fractal images. Default value can be configured in ```cfg.py```. 

# Loading Fractals
## Type in the file name of your fractal template stored in ```fractal_templates```. Then click "Load Fractal." That's it - your fractal should be loaded in.

# Gradient
## Use the Gradient Tool to find a gradient you like, then click "Apply Gradient." Gradient is only applied if it has actually changed (due to the way the application loads pre-existing gradients).

# Config (```cfg.py```)
## INSTALLATION_PATH: where Fractal-Pro is installed. Please make sure to include \FractalPro at the end of the path just like my example.
## THREADS: number of threads used to generate new fractals. if set to 1, there will be no threading done.
## C: default C value
## MAX_ITERS: default Max Iterations value.

# Create Your Own Fractal
## 1. Write the function in ```fractals.py```.
## 2. Add to ```FRACTAL_DICT``` in ```render.py```.
## Note that your fractal function should return a value between 0 and 1. Based on these values, the gradient will be applied.

# Examples
![alt text](https://github.com/ethan-prime/fractal-renderer/blob/master/results/8.png)
![alt text](https://github.com/ethan-prime/fractal-renderer/blob/master/results/1.png)
![alt text](https://github.com/ethan-prime/fractal-renderer/blob/master/results/3.png)
![alt text](https://github.com/ethan-prime/fractal-renderer/blob/master/results/7.png)
![alt text](https://github.com/ethan-prime/fractal-renderer/blob/master/results/2.png)
![alt text](https://github.com/ethan-prime/fractal-renderer/blob/master/results/6.png)