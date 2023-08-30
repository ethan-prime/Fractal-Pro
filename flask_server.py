from flask import Flask, request, render_template, redirect, url_for
from render import *
import cv2
from cfg import INSTALLATION_PATH, THREADS

app = Flask(__name__)

current_fractal = None

@app.route('/')
def base():
    return redirect(url_for('home', grad_info='000000+0&ffffff+100'))

@app.route('/<grad_info>', methods=['GET', 'POST'])
def home(grad_info):
    grad_info = grad_info.replace('#','')
    if grad_info == "" or grad_info == None:
        grad_info = ""
    if request.method == 'GET':
        return render_template('main.html', g_info=grad_info)
    elif request.method == 'POST':
        filename = request.form['loadfile']
        fractalname = request.form['fractalname']
        file = request.form['file']
        imgsize = request.form['imgsize'].replace(' ','')
        xrange = request.form['xrange'].replace(' ','')
        yrange = request.form['yrange'].replace(' ','')
        samples = request.form['samples']
        c = request.form['constant']
        max_iters = request.form['maxiters']
        grad_str = ""
        grad_process = []
        for param, value in request.form.items():
            if param.startswith('c') and param.endswith('v'):
                grad_str += f'{value.replace("#","")}+{request.form[param.replace("v","d")]}&'
                grad_process.append([value.replace("#",""), float(request.form[param.replace("v","d")])])
        grad_str = grad_str[:-1]
        grad_process.sort(key=lambda x: x[1])
        if grad_process[0][1] != 0:
            grad_process = [[grad_process[0][0], 0]] + grad_process
        if grad_process[-1][1] != 100:
            grad_process = grad_process + [[grad_process[-1][0], 100]]
        for i in range(len(grad_process)-1, 0, -1):
            grad_process[i][1] = grad_process[i][1] - grad_process[i-1][1]
        lerps = []
        for i in range(0, len(grad_process)-1):
            lerps.append([int(grad_process[i+1][1]*100), hex_to_rgb(grad_process[i][0]), hex_to_rgb(grad_process[i+1][0])]) #multiply by 10, we'll get ~ 1000 colors in grad
        grad = handle_lerps(lerps)
        if len(filename) > 0:
            load(filename)
        if grad_info == grad_str:
            pass
        else:
            add_grad(grad=grad)
        if len(file) > 0 and len(fractalname) > 0 and len(imgsize) > 0 and len(xrange) > 0 and len(yrange) > 0 and len(samples) > 0:
            if fractalname.lower() not in FRACTALS_DICT:
                print('Fractal not found.')
            else:
                f = Fractal(fractalname.lower())
                imgsize = (int(imgsize.split(',')[0]),int(imgsize.split(',')[1]))
                xrange = (float(xrange.split(',')[0]),float(xrange.split(',')[1]))
                yrange = convert_yrange(yrange)
                samples = int(samples)
                if c == "":
                    c = C
                else:
                    c = c.replace(' ', '').split(',')
                    c = complex(float(c[0]), float(c[1]))
                if max_iters == "":
                    max_iters = MAX_ITERS
                else:
                    max_iters = int(max_iters)
                if THREADS > 1:
                    f.calculate_batches(imgsize, xrange, yrange, samples, c=c, max_iters=max_iters)
                    f.get_pixels_from_batches('fractal_templates/'+file, imgsize, xrange, yrange, samples, c=c, max_iters=max_iters)
                elif THREADS == 1:
                    f.get_pixels('fractal_templates/'+file, imgsize, xrange, yrange, samples, c=c, max_iters=max_iters)
                res = np.array(f.pixels)
                scale_factor = 720/res.shape[0]
                res = cv2.resize(res, dsize=(int(res.shape[1]*scale_factor), int(res.shape[0]*scale_factor))).tolist()
                global current_fractal
                current_fractal = f
                current_fractal.temp_pixels = res
                current_fractal.to_image(current_fractal.temp_pixels, temp=True)

        return redirect(url_for("home", grad_info=grad_str))

def add_grad(grad):
    global current_fractal
    try:
        current_fractal.to_image(current_fractal.temp_pixels, grad=grad, temp=True)
        current_fractal.grad = grad
    except Exception:
        print('Fractal not loaded.')
        return "Error"
    return "Gradient added."

@app.route('/load/<filename>')
def load(filename):
    f = Fractal('loader')
    f.load_pixels(os.path.join('fractal_templates', filename))
    res = np.array(f.pixels)
    scale_factor = 720/res.shape[0]
    res = cv2.resize(res, dsize=(int(res.shape[1]*scale_factor), int(res.shape[0]*scale_factor))).tolist()
    global current_fractal
    current_fractal = f
    current_fractal.temp_pixels = res
    current_fractal.to_image(current_fractal.temp_pixels, temp=True)
    return "Fractal loaded."

@app.route('/save-fractal')
def save_fractal():
    global current_fractal
    current_fractal.to_image(current_fractal.pixels, grad=current_fractal.grad, save=True, temp=False)
    return redirect(url_for("base"))

def handle_lerps(parts):
    grad = []
    for part in parts:
        grad += lerp(part[0], part[1], part[2])
    return grad

def hex_to_rgb(hex):
  return [int(hex[i:i+2], 16) for i in (0, 2, 4)]

def convert_yrange(yrange):
    yrange = yrange.split(',')
    new_yrange = ['','']
    if yrange[0].startswith('-'):
        new_yrange[0] += '-'
    if yrange[1].startswith('-'):
        new_yrange[1] += '-'
    new_yrange[0] += yrange[1].replace('-','')
    new_yrange[1] += yrange[0].replace('-','')
    return (float(new_yrange[0]), float(new_yrange[1]))

    
if __name__ == '__main__':
    app.run()