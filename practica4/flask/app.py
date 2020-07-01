#./flask/app.py

from flask import Flask, render_template, request, session
from pickleshare import *
from pymongo import MongoClient



app = Flask(__name__, static_url_path='/static')
app.secret_key = '1234'

db = PickleShareDB('/usuarios')

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
        if db.keys(usuario):
            if password == db[usuario]['pass']: 
                session['user'] =  usuario
                session['historial'] =  []            
            else:
                return render_template('index.html',errorPassword="Contraseña incorrecta")
        else:
            return render_template('index.html',errorUsuarioNoValido="Usuario no válido")
    else:
        return render_template('index.html',errorCampoVacio="Campo vacío")
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

@app.route('/registrar', methods = ['GET', 'POST'])
def registrar():
    if request.method == 'POST':
        usuario = request.form['registerName']
        password = request.form['registerPass']

        if password != '' and usuario != '':
            if not db.keys(usuario): # Buscamos el usuario por si ya esta registrado 
                db[usuario] = dict()
                db[usuario]['pass'] = password # Creamos el usuario con los datos proporcionados
                db[usuario]['direccion'] = ""
                db[usuario]['pais'] = ""
                db[usuario]['provincia'] = ""
                db[usuario]['localidad'] = ""     

                db[usuario] = db[usuario]
                session['user'] =  usuario # Creamos la sesión
                session['historial'] =  []

                return render_template("index.html",user=session['user'],historial=session['historial'])
            return render_template("registro.html",errorRegistro="error")
        else:
            return render_template("registro.html",errorCampoVacio="error")       
    else:
        if 'user' in session:
            historial_navegacion("/","Inicio")
            return render_template("registro.html",user=session['user'],historial=session['historial'])
        else:
            return render_template("registro.html")

@app.route('/user', methods = ['GET', 'POST'])
def perfil_usuario():
    usuario = session['user']
    if request.method == 'POST':
        
        password = db[usuario]["pass"]
        
        newPass1 = request.form['newPass1']
        newPass2 = request.form['newPass2']

        newDireccion = request.form['newDireccion'] 
        newPais = request.form['newPais']
        newProvincia = request.form['newProvincia']
        newLocalidad = request.form['newLocalidad']

        if newPass1 != '' and newPass2 != '':
            passActual = request.form['passActual']
            if newPass1 == newPass2 and passActual == password:
                db[usuario]['pass'] = newPass1
        

        db[usuario]['direccion'] = newDireccion
        db[usuario]['pais'] = newPais
        db[usuario]['provincia'] = newProvincia
        db[usuario]['localidad'] = newLocalidad 

        db[usuario] = db[usuario]
        detalles = []
        
    detalles = []
    if 'user' in session:
        detalles.append(session['user'])
        detalles.append(db[usuario]['direccion'])
        detalles.append(db[usuario]['pais'])
        detalles.append(db[usuario]['provincia'])
        detalles.append(db[usuario]['localidad'])
        historial_navegacion("/user","Perfil de usuario")
        return render_template("user.html",user=session['user'],historial=session['historial'],detalles=detalles)
    else:
        return render_template("user.html")

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
    

client = MongoClient("mongo", 27017) # Conectar al servicio (docker) "mongo" en su puerto estandar
dbmongo = client.SampleCollections      # Elegimos la base de datos de ejemplo

@app.route('/search', methods = ['GET', 'POST'])
def busqueda():
    if request.method == 'POST':
        busqueda = request.form['busqueda']
        val = dbmongo.samples_pokemon.find({"name" : {"$regex" : busqueda}})
        return render_template('mongo.html',pokemons = val)
    else:
        return redireccion()

@app.route('/add', methods = ['GET', 'POST'])
def anadir():
    if request.method == 'POST':
        nuevoPok = request.form['nuevoPok']
        if not len(list(dbmongo.samples_pokemon.find({"name" : nuevoPok}))) > 0:
            dbmongo.samples_pokemon.insert_one({ "name": nuevoPok })
            return redireccion('exito')
        else:
            return redireccion('errorDupli')
    else:
        return redireccion()

@app.route('/delete', methods = ['GET', 'POST'])
def delete():
    if request.method == 'POST':
        borrarPok = request.form['borrarPok']
        if len(list(dbmongo.samples_pokemon.find({"name" : borrarPok}))) > 0:
            dbmongo.samples_pokemon.delete_one({ "name": borrarPok })
            return redireccion('exitoBorrado')
        else:
            return redireccion('errorBorrado')
    else:
        return redireccion()

@app.route('/mongo')
def mongo():
    return redireccion()

@app.route('/mod', methods = ['GET', 'POST'])
def modificarAtributos():
    if request.method == 'POST':
        nombre = request.form['nombre']
        altura = request.form['altura']
        peso = request.form['peso']

        buscar = { "name": nombre }
        nuevos_valores = { "$set": { "height": altura } }
        dbmongo.samples_pokemon.update_one(buscar, nuevos_valores)

        nuevos_valores = { "$set": { "weight": peso } }
        dbmongo.samples_pokemon.update_one(buscar, nuevos_valores)

        datos_pokemon = dbmongo.samples_pokemon.find({"name" : nombre})
        return render_template('mongo.html', datos = datos_pokemon[0])
    else:
        pokemon = request.args.get('name')
        datos_pokemon = dbmongo.samples_pokemon.find({"name" : pokemon})

    return render_template('mongo.html', datos = datos_pokemon[0])

def redireccion(parametro=None):
    val = dbmongo.samples_pokemon.find()  # Encontramos los documentos de la coleccion "samples_pokemon
    if parametro is not None:
        return render_template('mongo.html',pokemons = val, par = parametro)
    else:
        return render_template('mongo.html',pokemons = val)