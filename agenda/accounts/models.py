from django.db import models
from contatos.models import Contato
from django import forms


class FormContato(forms.ModelForm):
    class Meta:
        #esse formulario representa o model Contato
        #exclui a visualização do campo mostrar no dashboard.html
        model = Contato
        exclude = ('mostrar',)
