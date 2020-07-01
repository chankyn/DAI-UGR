# practica_09/views.py
from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect,JsonResponse
from django.shortcuts import render,get_object_or_404
from django.db.models import Count
from .forms import *

def index(request):
    musicos = Musico.objects.all()
    albums = Album.objects.all()
    grupos = GrupoMusical.objects.all()
    instrumentos = Instrumentos.objects.all()
    return render(request,'index.html',{'musicos':musicos,'albums':albums,'grupos':grupos,'instrumentos':instrumentos})

def test_template(request):
    context = {}   # Aquí van la las variables para la plantilla
    context["user"] = "migue"
    return render(request,'basico.html', context)

def nuevo_musico(request):

    if request.method == 'POST':
        # creamos una instancia con los datos del request
        form = MusicianForm(request.POST)

        if form.is_valid():                # validamos
            # procesamos los datos de form.cleaned_data
            # nombre = form.cleaned_data.get('tu_nombre')
            name = form.cleaned_data.get('nombre')
            nac = form.cleaned_data.get('fecha_nacimiento')
            if Musico.objects.filter(nombre=name, fecha_nacimiento=nac).first() == None:
                form.save()
                return HttpResponseRedirect('/correcto/')
            else:
                return HttpResponseRedirect('/incorrecto/Duplicado')
	   
            return HttpResponseRedirect('/correcto/')

    else:
        form = MusicianForm()
    # enviamos el formlario limpio,
    # o con errorres si is_valid() == 'False'
    return render(request, 'formulario.html', {'form': form,'nombre': 'Músico','nombreFormulario':'nuevo_musico'})

def correcto(request):
    return render(request,'index.html',{'correcto':True})

def incorrecto(request,error):
    return render(request,'index.html',{'correcto':False,'error':error})

def borrar(request,tipo,id):
    correcto = False
    if tipo == "instrumento":
        Instrumentos.objects.filter(id=id).delete()
        correcto = True
    elif tipo == "musico":
        Musico.objects.filter(id=id).delete()
        correcto = True
    elif tipo == "album":
        Album.objects.filter(id=id).delete()
        correcto = True
    elif tipo == "grupo":
        GrupoMusical.objects.filter(id=id).delete()
        correcto = True
    
    if correcto:
        return HttpResponseRedirect('/correcto/')
    else:
        return HttpResponseRedirect('/incorrecto/Nombre inválido')

def modificar(request,tipo=None,id=None):
    if request.method != 'POST':
        if tipo == "instrumento":
            new = get_object_or_404(Instrumentos, pk=id)
            form = InstrumentosForm(request.POST or None, instance=new)
        elif tipo == "musico":
            new = get_object_or_404(Musico, pk=id)
            form = MusicianForm(request.POST or None, instance=new)
        elif tipo == "album":
            new = get_object_or_404(Album, pk=id)
            form = AlbumForm(request.POST or None, instance=new)
        else:
            new = get_object_or_404(GrupoMusical, pk=id)
            form = GrupoForm(request.POST or None, instance=new)
    else:
        if tipo == "instrumento":
            new = Instrumentos(id=id)
            form = InstrumentosForm(request.POST or None, instance=new)
        elif tipo == "musico":
            new = Musico(id=id)
            form = MusicianForm(request.POST or None, instance=new)
        elif tipo == "album":
            new = Album(id=id)
            form = AlbumForm(request.POST or None, instance=new)
        else:
            new = GrupoMusical(id=id)
            form = GrupoForm(request.POST or None, instance=new)

        if request.POST and form.is_valid():
            form.save()
            return HttpResponseRedirect('/correcto/')
    return render(request, 'formulario.html', {'form': form,'nombreFormulario':'modificar/'+tipo+'/'+id})
        
def nuevo_instrumento(request):

    if request.method == 'POST':
        # creamos una instancia con los datos del request
        form = InstrumentosForm(request.POST)

        if form.is_valid():                # validamos
            # procesamos los datos de form.cleaned_data
            # nombre = form.cleaned_data.get('tu_nombre')
            name = form.cleaned_data.get('nombre')
            if Instrumentos.objects.filter(nombre=name).first() == None:
                form.save()
                return HttpResponseRedirect('/correcto/')
            else:
                return HttpResponseRedirect('/incorrecto/Duplicado')
            

    else:
        form = InstrumentosForm()
    # enviamos el formlario limpio,
    # o con errorres si is_valid() == 'False'
    return render(request, 'formulario.html', {'form': form,'nombre': 'Instrumento','nombreFormulario':'nuevo_instrumento'})


def nuevo_album(request):

    if request.method == 'POST':
        form = AlbumForm(request.POST)

        if form.is_valid():                # validamos
            name = form.cleaned_data.get('titulo')
            date = form.cleaned_data.get('fecha_lanzamiento')
            if Album.objects.filter(titulo=name,fecha_lanzamiento=date).first() == None:
                form.save()
                return HttpResponseRedirect('/correcto/')
            else:
                return HttpResponseRedirect('/incorrecto/Duplicado')

    else:
        form = AlbumForm()
    return render(request, 'formulario.html', {'form': form,'nombre': 'Album','nombreFormulario':'nuevo_album'})

def nuevo_grupo(request):

    if request.method == 'POST':
        form = GrupoForm(request.POST)

        if form.is_valid():                # validamos
            name = form.cleaned_data.get('nombre')
            if GrupoMusical.objects.filter(nombre=name).first() == None:
                form.save()
                return HttpResponseRedirect('/correcto/')
            else:
                return HttpResponseRedirect('/incorrecto/Duplicado')

    else:
        form = GrupoForm()
    return render(request, 'formulario.html', {'form': form,'nombre': 'Grupo Musical','nombreFormulario':'nuevo_grupo'})


def login(request):
    return render(request, 'registro.html')

def busqueda(request):
    musicos = Musico.objects.all()
    albums = Album.objects.all()
    grupos = GrupoMusical.objects.all()
    instrumentos = Instrumentos.objects.all()
    return render(request,'busqueda.html',{'musicos':musicos,'albums':albums,'grupos':grupos,'instrumentos':instrumentos})


def reclama_datos (request):
    id_grupo = request.GET.get("id")
    tipo = request.GET.get("tipo")

    if tipo == "Musico":   
        resultados = list(Musico.objects.filter(grupos_musicales=id_grupo).values_list('nombre'))
    elif tipo == "Album":
        resultados = list(Album.objects.filter(grupo=id_grupo).values_list('titulo'))
     
    datos = {'resultados': list(resultados)}
    
    return JsonResponse(datos, safe=False)

def tablaAjax(request):
    grupos = GrupoMusical.objects.all()
    return render(request,'tablaAjax.html',{'grupos': grupos})
    
def crearMapa(request,id):
    datos = Musico.objects.filter(id=id).first()
    #,{'nombre_localizacion':datos.lugar_nacimiento,'latitud': datos.latitud,'longitud':datos.longitud}
    return render(request,'mapa.html',{'nombre_localizacion':datos.lugar_nacimiento,'latitud': datos.latitud,'longitud':datos.longitud})

def crearGrafico(request,ajax=None,tipo=None):
    grupos = GrupoMusical.objects.all()
    instrumentos = Instrumentos.objects.all()
    albums = Album.objects.all()

    resultados_grupo = {}
    resultados_instrumentos = {}
    resultados_albums = {}

    for grupo in grupos:
        n_musicos = Musico.objects.filter(grupos_musicales=grupo.id).count()
        n_albums = Album.objects.filter(grupo=grupo.id).count()
        resultados_grupo[grupo.nombre] = [n_musicos,n_albums]
    for instrumento in instrumentos:
        n_instrumentos = Musico.objects.filter(instrumento_principal=instrumento.id).count()
        n_instrumentos += Musico.objects.filter(instrumentos_secundarios=instrumento.id).count()
        resultados_instrumentos[instrumento.nombre] = n_instrumentos
    for album in albums:
        anio = album.fecha_lanzamiento.year
        if anio in resultados_albums:
            resultados_albums[anio] += 1
        else:
            resultados_albums[anio] = 1

    inst, n_inst = zip(*resultados_instrumentos.items()) 
    groups, list_g = zip(*resultados_grupo.items())
    anio, n_album = zip(*resultados_albums.items())

    if ajax is None:
        return render(request,'grafico.html',{'grupos':list(groups),'valores_grupos':list_g,'instrumentos':list(inst),'n_instrumentos':list(n_inst),'anio':list(anio),'n_albums':list(n_album)})
    else:
        if tipo == "Opcion1":
            return {'categoria':list(groups),'serie':list_g[0]}
        elif tipo == "Opcion2":
            return {'categoria':list(groups),'serie':list_g[1]}
        elif tipo == "Opcion3":
            return {'categoria':list(inst),'serie':list(n_inst)}
        elif tipo == "Opcion4":
            return {'categoria':list(anio),'serie':list(n_album)}

def crearGraficoAjax(request):
    return render(request,'grafico_ajax.html')

def reclama_datos_grafico(request):
    tipo = request.GET.get("tipo")
    datos = crearGrafico(request,True,tipo)
     
    return JsonResponse(datos, safe=False)