# practica_09/urls.py

from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^test_template/$', views.test_template, name='test_template'),
  url(r'^nuevo_musico/$', views.nuevo_musico, name='nuevo_musico'),
  url(r'^nuevo_instrumento/$', views.nuevo_instrumento, name='nuevo_instrumento'),
  url(r'^nuevo_album/$', views.nuevo_album, name='nuevo_album'),
  url(r'^nuevo_grupo/$', views.nuevo_grupo, name='nuevo_grupo'),
  url(r'^correcto/$', views.correcto, name='correcto'),
  url(r'^incorrecto/(?P<error>\w{0,50})/$', views.incorrecto, name='incorrecto'),
  url(r'^modificar/(?P<tipo>\w{0,50})/(?P<id>\w{0,50})/$', views.modificar, name='modificar'),
  url(r'^editar/(?P<tipo>\w{0,50})/$', views.modificar, name='editar'),
  url(r'^borrar/(?P<tipo>\w{0,50})/(?P<id>\w{0,50})/$', views.borrar, name='borrar'),
  url(r'^login/$', views.login, name='login'),
  url(r'^busqueda/$', views.busqueda, name='busqueda'),
  url(r'^reclama_datos/$', views.reclama_datos, name='reclama_datos'),
  url(r'^ajax/$', views.tablaAjax, name='ajax'),
  url(r'^mapa/(?P<id>\w{0,50})/$', views.crearMapa, name='mapa'),
  url(r'^grafico/$', views.crearGrafico, name='grafico'),
  url(r'^grafico_ajax/$', views.crearGraficoAjax, name='graficoAjax'),
  url(r'^reclama_datos_grafico/$', views.reclama_datos_grafico, name='reclama_datos_grafico'),
  
]