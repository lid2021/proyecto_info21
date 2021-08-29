from django import forms
from .models import Preguntas, ElegirRespuesta, PreguntasRespondidas


class ElegirInlineFormset(forms.BaseInlineFormSet):
    def clean(self):
        super(ElegirInlineFormset, self).clean()

        #Valida los datos traidos de 'ElegirRespuesa'
        respuesta_correcta = 0
        for formulario in self.forms:
            if not formulario.is_valid():
                return
            
            if formulario.cleaned_data and formulario.cleaned_data.get('correcta') is True:
                respuesta_correcta += 1
    
        try:
            assert respuesta_correcta == Preguntas.NUMER_DE_RESPUESTAS_PERMITIDAS
        except AssertionError:
            raise forms.ValidationError('Solo Se Permite Una Respuesta')

