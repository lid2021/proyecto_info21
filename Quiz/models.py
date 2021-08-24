from django.db import models


# Preguntas ¿? -----> Elecciones de Respuestas -----> Intentos Preguntas -----> Perfil Quiz ----> Puntaje Total
 

# Create your models here.
# se crea los Campos de DB

class Preguntas(models.Model): #Se crea la caja de preguntas
    '''Se cargan las preguntas desde el panel de admin y se conecta con la clase ElegirRespuestas con el campo texto'''
    #atributos de la clase
    texto = models.TextField(verbose_name='Texto de la pregunta')

    #Metodo de la clase
    def __str__(self):
        return self.texto

class ElegirRespuesta(models.Model): #se crea y se polimorfea con la clase 'Pregunta'
    
    #Atributo de la clase
    #Se limpia el campo despues de recargar la preguntaPara que la DB nos muestre el campo con ese nombre referencial
    pregunta = models.ForeignKey(Preguntas, related_name='preguntas', on_delete=models.CASCADE)
    #El campo booleano es para marcar la respuesta correcta al momento de cargar las preguntas
    correcta = models.BooleanField(verbose_name='¿Es la Pregunta Correcta?',default=False, null=False)
    texto = models.TextField(verbose_name='Texto de la Pregunta')

    #Metodo de la clase
    def __str__(self):
        return self.texto
    
    