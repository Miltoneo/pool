
from django import forms
from django.forms import ModelForm, ChoiceField,  DateField, widgets
from django.forms.widgets import HiddenInput
from .models import *
from django.conf import settings


#-----------------------------------------
class candidato_Form(ModelForm):
    class Meta:
        model = Candidato
        fields =  "__all__"
        exclude = ('receita', 'despesa')

#-----------------------------------------
class cidade_Form(ModelForm):
    class Meta:
        model = Cidade
        fields =  "__all__"
