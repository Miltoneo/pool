
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
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profissao'].required = False
        self.fields['dnascimento'].required = False

        self.fields['endereco'].required = False
        self.fields['cep'].required = False
        self.fields['fone'].required = False
        self.fields['email'].required = False

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
        exclude = ('doador','candidato',) 
        widgets = {
                    'data': widgets.DateInput(attrs={'type': 'date'}),
                    }
#-----------------------------------------
class Teto_gastos_Form(ModelForm):
    class Meta:
        model = Teto_gasto_cargo
        fields =  "__all__"   

#-----------------------------------------
class Pessoa_contrato_Form(ModelForm):
    class Meta:
        model = Pessoa_contratada
        fields =  "__all__"   
        widgets = {
                    'data': widgets.DateInput(attrs={'type': 'date'}),
                    }
        exclude = ('despesa_pessoal', 'valor_total')    
