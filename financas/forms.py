
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

#-----------------------------------------
class Pessoa_Form(ModelForm):
    class Meta:
        model = Pessoa
        fields =  "__all__"

#-----------------------------------------
class Partido_Form(ModelForm):
    class Meta:
        model = Partido
        fields =  "__all__"

#-----------------------------------------
class Cargo_Form(ModelForm):
    class Meta:
        model = Cargo
        fields =  "__all__"        

#-----------------------------------------
class Candidato_Form(ModelForm):
    class Meta:
        model = Candidato
        fields =  "__all__"    
        exclude = ('receita', 'despesa')    

#-----------------------------------------
class Gpo_despesas_Form(ModelForm):
    class Meta:
        model = Grupo_despesa
        fields =  "__all__"    
        exclude = ('receita', 'despesa')    

#-----------------------------------------
class Item_despesa_Form(ModelForm):
    class Meta:
        model = Item_despesa
        fields =  "__all__"    
        exclude = ('receita', 'despesa')    

#-----------------------------------------
class Doador_Form(ModelForm):
    class Meta:
        model = Doador
        fields = ['pessoa',]   

#-----------------------------------------
class Doacao_Form(ModelForm):
    class Meta:
        model = Doacoes
        fields =  "__all__"   
        exclude = ('doador',) 
        widgets = {
                    'data': widgets.DateInput(attrs={'type': 'date'}),
                    }
        
#-----------------------------------------
class Teto_gastos_Form(ModelForm):
    class Meta:
        model = Teto_gasto_cargo
        fields =  "__all__"   




