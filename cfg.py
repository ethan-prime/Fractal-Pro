import math, cmath

#SYSTEM VARIABLES 
INSTALLATION_PATH = r"C:\Path\To\Installation\Fractal-Pro" #where Fractal-Pro is installed. Please make sure to include \FractalPro at the end of the path just like my example.
THREADS = 1 #number of threads used to generate new fractals. if set to 1, there will be no threading done.

#DEFAULT VARIABLES FOR GENERATING FRACTALS. OVERRIDEN BY FORM WHEN GENERATING.
C = complex(-0.835, 0.2321) #used for generating fractals. see documentation on wikipedia!
MAX_ITERS = 100 #used for generating fractals. see documentation on wikipedia!