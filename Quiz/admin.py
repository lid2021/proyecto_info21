from django.contrib import admin
from .models import Preguntas, ElegirRespuesta, PreguntasRespondidas
from .forms import ElegirInlineFormset

 #Register your models here.

class ElegirRespuestaInline(admin.TabularInline):
    ''' Se hereda del campo elejirResuesta las respuestas de las preguntas, 
    para listarlas dentro de la clase PreguntaAdmin como un multiple choices, con list_display'''
    model = ElegirRespuesta
    can_delete = False 
    max_num = ElegirRespuesta.MAXIMO_RESPUESTAS
    min_num = ElegirRespuesta.MAXIMO_RESPUESTAS
    formset = ElegirInlineFormset
    
class PreguntaAdmin(admin.ModelAdmin):
    model = Preguntas
    inlines = (ElegirRespuestaInline, )
    #Lista las respuestas heredadas de model ElegirRespusta
    list_display = ['texto',]
    search_fields = ['texto', 'pregunta__texto']



class PreguntasRespondidasAdmin(admin.ModelAdmin):
    '''Se pasa los campos de la plantilla model para mostar por pantalla'''
    list_display = ['pregunta', 'respuesta', 'correcta', 'puntaje_obtenido', ]
    class Meta:
        model = PreguntasRespondidas

admin.site.register(PreguntasRespondidas)
admin.site.register(Preguntas, PreguntaAdmin)
admin.site.register(ElegirRespuesta)
