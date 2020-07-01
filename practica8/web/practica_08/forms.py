from django.core.validators import RegexValidator
from django.forms import ModelForm
from .models import GrupoMusical,Album,Musico,Instrumentos

class MusicianForm(ModelForm):
    class Meta:
        model = Musico
        fields = ['nombre', 'fecha_nacimiento', 'instrumento_principal', 'instrumentos_secundarios', 'grupos_musicales','lugar_nacimiento','latitud','longitud']
        labels = {
            'nombre': 'Nombre',
            'fecha_nacimiento': 'Fecha de nacimiento',
            'instrumento_principal': 'Instrumento principal',
            'instrumentos_secundarios': 'Instrumentos secundarios',
            'grupos_musicales': 'Grupos musicales',
            'lugar_nacimiento': 'Lugar de nacimiento',
            'latitud': 'Latitud del lugar del nacimiento',
            'longitud': 'Longitud del lugar del nacimiento'
        }
        help_texts = {
            'nombre': 'Nombre para el músico',
            'fecha_nacimiento': 'Formato: dia/mes/año 16/05/1993',
            'instrumento_principal': 'Escoge un instrumento de la lista',
            'instrumentos_secundarios': 'Escoge uno o varios instrumentos de la lista',
            'grupos_musicales': 'Escoge uno o varios grupos de la lista'

        }
        error_messages = {
            'nombre': {
                'max_length': "Este nombre es muy largo",
            }
        }

class InstrumentosForm(ModelForm):
    class Meta:
        model = Instrumentos
        fields = ['nombre']
        labels = {
            'nombre': 'Nombre'
        }
        help_texts = {
            'nombre': 'Nombre para el instrumento'
        }
        error_messages = {
            'nombre': {
                'max_length': "Este nombre es muy largo",
            }
        }

class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = ['titulo', 'distribuidora', 'fecha_lanzamiento', 'grupo']
        labels = {
            'titulo': 'Título',
            'distribuidora': 'Distribuidora',
            'fecha_lanzamiento': 'Fecha de lanzamiento',
            'grupo': 'Grupo musical'
        }
        help_texts = {
            'titulo': 'Título para el album',
            'distribuidora': 'Nombre de la distribuidora',
            'fecha_lanzamiento': 'Formato: dia/mes/año 16/05/1993',
            'grupo': 'Escoge un grupo de la lista'

        }
        error_messages = {
            'nombre': {
                'max_length': "Este nombre es muy largo",
            }
        }

class GrupoForm(ModelForm):
    class Meta:
        model = GrupoMusical
        fields = ['nombre', 'fecha_fundacion', 'estilo_musical']
        labels = {
            'nombre': 'Nombre',
            'fecha_fundacion': 'Fecha de fundación',
            'estilo_musical': 'Estilo musical'
        }
        help_texts = {
            'nombre': 'Nombre del grupo',
            'fecha_fundacion': 'Formato: dia/mes/año 16/05/1993',
            'grupo': 'Escoge un grupo de la lista'

        }
        error_messages = {
            'nombre': {
                'max_length': "Este nombre es muy largo",
            }
        }