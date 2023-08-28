# Fractal Pro ![Static Badge](https://img.shields.io/badge/Python-blue) ![Static Badge](https://img.shields.io/badge/JavaScript-yellow) ![Static Badge](https://img.shields.io/badge/HTML-orange) ![Static Badge](https://img.shields.io/badge/CSS-03BAFC) ![Static Badge](https://img.shields.io/badge/Flask-7303FC)
### My fractal renderer. Made with Python, JavaScript, HTML, CSS, and Flask (among other Python libraries). You can (currently) make fractals from the [Mandelbrot Set](https://en.wikipedia.org/wiki/Mandelbrot_set), [Julia Set](https://en.wikipedia.org/wiki/Julia_set) and [Burning Ship](https://en.wikipedia.org/wiki/Burning_Ship_fractal) fractals.

# The Interface
![alt text](https://github.com/ethan-prime/fractal-renderer/blob/master/assets/interface.png)

### Yeah. It's pretty straight-forward. You can load fractals from the fractal-templates folder, generate fractals by giving information it in the form, and you can create custom gradients/color schemes that can be applied to a fractal once generated.

### When a fractal is generated, it stores values between 0 and 1 for each pixel which are then converted to colors within your custom gradient. This makes it so that you don't have to re-generate a new fractal every time you want to change the color; you just need to load it in.

### Saved fractals go to the results folder.

# Installation and Launching
### First, download the repo as a zip file or run ```git clone https://github.com/ethan-prime/Fractal-Pro.git```.
### Then, make sure to specify the installation path in ```cfg.py``` (note: please include the \Fractal-Pro at the end of the path - see the example in ```cfg.py```).
### Install all requirements in requirements.txt by running ```pip install -r requirements.txt```
### Start ```flask_server.py```
### Navigate to [localhost:5000](http://localhost:5000).


# Examples
![alt text](https://github.com/ethan-prime/fractal-renderer/blob/master/results/8.png)
![alt text](https://github.com/ethan-prime/fractal-renderer/blob/master/results/1.png)
![alt text](https://github.com/ethan-prime/fractal-renderer/blob/master/results/3.png)
![alt text](https://github.com/ethan-prime/fractal-renderer/blob/master/results/7.png)
![alt text](https://github.com/ethan-prime/fractal-renderer/blob/master/results/2.png)
![alt text](https://github.com/ethan-prime/fractal-renderer/blob/master/results/6.png)