#./flask/ejer1.py

from flask import Flask, render_template, request, session

#from pickleshare import *

app = Flask(__name__, static_url_path='/static')
app.secret_key = '1234'

#db = PickleShareDB('/usuarios')

@app.route('/')
def index():
    if 'user' in session:
        historial_navegacion("/","Inicio")
        return render_template("index.html",user=session['user'],historial=session['historial'])
    else:
        return render_template("index.html")
@app.route('/about')
def about():
    if 'user' in session:
        historial_navegacion("/about","Página about")
        return render_template("about.html",user=session['user'],historial=session['historial'])
    else:
        return render_template("about.html")

@app.route('/contacto')
def contacto():
    if 'user' in session:
        historial_navegacion("/contacto","Página de contacto")
        return render_template("contacto.html",user=session['user'],historial=session['historial'])
    else:
        return render_template("contacto.html")

@app.route('/logear', methods = ['GET', 'POST'])
def login():
    usuario = request.form['loginName']
    password = request.form['loginPass']

    if password != '' and usuario != '':
        session['user'] =  usuario
        session['historial'] =  []
        
    if 'user' in session:
        historial_navegacion("/","Inicio")
        return render_template("index.html",user=session['user'],historial=session['historial'])
    else:
        return render_template("index.html")

@app.route('/logout', methods = ['GET', 'POST'])
def logout():
    session.pop('user',None)
    session.pop('historial',None)
    
    if 'user' in session:
        historial_navegacion("/","Inicio")
        return render_template("index.html",user=session['user'],historial=session['historial'])
    else:
        return render_template("index.html")

def historial_navegacion(href,name):
    direcciones = []
    if 'historial' in session:
        direcciones = session['historial']
    direcciones.insert(0,[href,name])

    if len(direcciones) > 3:
        direcciones.pop()
    
    session['historial'] = direcciones
    print(session['historial'])

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
    
    