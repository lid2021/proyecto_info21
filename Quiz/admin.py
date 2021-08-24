from django.contrib import admin
from .models import Preguntas, ElegirRespuesta

# Register your models here.

class ElegirRespuestaInline(admin.TabularInline):
    ''' Se hereda del campo elejirResuesta las respuestas de las preguntas, 
    para listarlas dentro de la clase PreguntaAdmin como un multiple choices, con list_display'''
    model = ElegirRespuesta
    
class PreguntaAdmin(admin.ModelAdmin):
    model = Preguntas
    inlines = (ElegirRespuestaInline, )
    #Lista las respuestas heredadas de model ElegirRespusta
    list_display = ['texto',]
    search_fields = ['texto', 'pregunta__texto']


admin.site.register(Preguntas, PreguntaAdmin)
admin.site.register(ElegirRespuesta)