from django.db import models
from django.contrib.auth.models import User


# Preguntas ¿? -----> Elecciones de Respuestas -----> Intentos Preguntas -----> Perfil Quiz ----> Puntaje Total
 

# Create your models here.
# se crea los Campos de DB

#Se crea una Pregunta
class Preguntas(models.Model): #Se crea la caja de preguntas
    '''Se cargan las preguntas desde el panel de admin y se conecta con la clase ElegirRespuestas con el campo texto'''
    #atributos de la clase

    NUMER_DE_RESPUESTAS_PERMITIDAS = 2

    texto = models.TextField(verbose_name='Texto de la pregunta')

    #Metodo de la clase
    def __str__(self):
        return self.texto

#Se crea una Respuesta a esa Pregunta
class ElegirRespuesta(models.Model): #se crea y se polimorfea con la clase 'Pregunta'
    
    #Atributo de la clase
    #Se limpia el campo despues de recargar la preguntaPara que la DB nos muestre el campo con ese nombre referencial
    MAXIMO_RESPUESTAS = 5
    pregunta = models.ForeignKey(Preguntas, related_name='preguntas', on_delete=models.CASCADE)
    #El campo booleano es para marcar la respuesta correcta al momento de cargar las preguntas
    correcta = models.BooleanField(verbose_name='¿Es la Pregunta Correcta?',default=False, null=False)
    texto = models.TextField(verbose_name='Texto de la Pregunta')

    #Metodo de la clase
    def __str__(self):
        return self.texto
    
#Se guarda el usuario
class Usuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    puntaje_total = models.DecimalField(verbose_name='Puntaje_total', default=0, decimal_places=2, max_digits=10,)

#Se guarda la pregunta respondida
class PreguntasRespondidas(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Preguntas, on_delete=models.CASCADE)
    #Limpia Respuesta despues de seleccionada la misma
    respuesta = models.ForeignKey(ElegirRespuesta, on_delete=models.CASCADE, related_name='intento')
    correcta = models.BooleanField(verbose_name='¿Es la Respuesta Correct?', default=False, null=False)
    puntaje_obtenido = models.DecimalField(verbose_name='Puntaje Obtenido', default=0, decimal_places=2, max_digits=6)