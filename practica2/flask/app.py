#./flask/app.py

from flask import Flask, request, render_template

import mandelbrot, os, time
import random

app = Flask(__name__, static_url_path='/static')



@app.route('/')
def hello_world():
    ##return 'Hello, World!'
    ##return app.send_static_file('index.html')
    return '''
        <!doctype html>
            <html>
                <head>
                    <title>P2: DAI</title>
                    <link rel="stylesheet" type="text/css" href="/static/css/index.css">
                </head>
                <body>
                    <h1>Hola mundo</h1>
                    <p class="blue">Prueba de css en una etiqueta párrafo usando flask</p>
                    <img src="/static/images/alcala.jpg"/>
                </body>
            </html>
        '''

@app.route('/user/')
@app.route('/user/<user>')
@app.route('/user/<user>/')
def user(user=None):
    ##return render_template('user.html', user=user)
    return '''
        <!doctype html>
                <html>
                    <head>
                        <title>P2: DAI</title>
                        <link rel="stylesheet" type="text/css" href="/static/css/index.css">
                    </head>
                    <body>
                        <h1>Hola %s</h1>
                        <p class="blue">Prueba de css en una etiqueta párrafo usando flask</p>
                    </body>
                </html>
            ''' % (user)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@app.route('/manderbolt/')
@app.route('/manderbolt/<x1>')
@app.route('/manderbolt/<x1>/<x2>')
@app.route('/manderbolt/<x1>/<x2>/<y1>')
@app.route('/manderbolt/<x1>/<x2>/<y1>/<y2>')
@app.route('/manderbolt/<x1>/<x2>/<y1>/<y2>/<int:iteraciones>')
@app.route('/manderbolt/<x1>/<x2>/<y1>/<y2>/<int:iteraciones>/<int:r>/<int:g>/<int:b>')
def manderbolt(x1=-1,x2=1,y1=-1,y2=1,iteraciones=255,r=25, g=16, b=32):
    fichero = "/static/images/dinamicas/dinamica_{}_{}_{}_{}_ite{}_{}_{}_{}.png".format(x1,x2,y1,y2,iteraciones,r,g,b)
    if not os.path.exists(str(".{}".format(fichero))):
       mandelbrot.pintaMandelbrot(float(x1), float(y1), float(x2), float(y2), 400, int(iteraciones), int(r), int(g), int(b), str(".{}".format(fichero)))
    return '<img src="{}">'.format(fichero)

current_time = time.time()

for f in os.listdir('./static/images/dinamicas'):
    path = os.path.join('./static/images/dinamicas', f)
    creation_time = os.path.getctime(path)
    if (current_time - creation_time) // (24 * 3600) >= 1:
        os.unlink(path)
        print('{} removed'.format(path))

@app.route('/nota/')
def ejercicioNota():

    imagen_svg = '<?xml version="1.0" encoding="UTF-8" standalone="no"?>'
    imagen_svg = imagen_svg + '<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%">'
    imagen_svg = imagen_svg + dibujar_line()
    imagen_svg = imagen_svg + dibujar_ellipse()
    imagen_svg = imagen_svg + dibujar_rectangle()
    imagen_svg = imagen_svg + dibujar_circle()
    imagen_svg = imagen_svg + '</svg>'

    return imagen_svg  # El XML del gráfico SVG

def generarColorHexadecimal():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    return '#%02X%02X%02X' % (r,g,b)

# elipses, rectángulos, etc. de colores y posiciones distintas.
def dibujar_ellipse():

    cx = random.randint(0,400)
    cy = random.randint(0,400)
    rx = random.randint(0,200)
    ry = random.randint(0,200)

    color_relleno = generarColorHexadecimal()
    color_linea = generarColorHexadecimal()
    
    return '<ellipse cx="{}" cy="{}" rx="{}" ry="{}" style="fill:{};stroke:{};stroke-width:2" />'.format(cx,cy,rx,ry,color_relleno,color_linea)

def dibujar_circle():

    cx = random.randint(0,400)
    cy = random.randint(0,400)
    r = random.randint(0,200)

    color_relleno = generarColorHexadecimal()
    color_linea = generarColorHexadecimal()
    
    return '<circle cx="{}" cy="{}" r="{}" stroke="{}" stroke-width="3" fill="{}" />'.format(cx,cy,r,color_linea,color_relleno)

def dibujar_rectangle():

    width = random.randint(0,400)
    height = random.randint(0,400)

    color_relleno = generarColorHexadecimal()
    color_linea = generarColorHexadecimal()

    return '<rect width="{}" height="{}" style="fill:{};stroke-width:3;stroke:{}" />'.format(width,height,color_relleno,color_linea)

def dibujar_line():
    x1 = random.randint(0,400)
    y1 = random.randint(0,400)
    x2 = random.randint(0,400)
    y2 = random.randint(0,400)

    color_linea = generarColorHexadecimal()

    return '<line x1="{}" y1="{}" x2="{}" y2="{}" style="stroke:{};stroke-width:2" />'.format(x1,y1,x2,y2,color_linea)