
from django import forms
from django.forms import ModelForm, ChoiceField,  DateField, widgets
from django.forms.widgets import HiddenInput
from .models import *
from django.conf import settings

from django_select2 import forms as s2forms
from django_select2.forms import Select2MultipleWidget, Select2Widget

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
class Grupo_despesa_Form(ModelForm):
    class Meta:
        model = Grupo_despesa
        fields =  ('codigo', 'descricao')   
        #exclude = ('receita', 'despesa')    

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


#-----------------------------------------
class Despesa_Form(ModelForm):
    class Meta:
        model = Despesas
        fields =  "__all__"   
        widgets = {
                    'data': widgets.DateInput(attrs={'type': 'date'}),
                    }
        exclude = ('candidato',)    


#--------------------------------------------------------

class MyGrupoWidget(s2forms.Select2Widget):
    model= Despesas,
    search_fields = [
        'grupo__icontains',
    ]

"""
    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(Despesa_Form, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['descricao'].required = False

"""

class Despesa_Form(ModelForm):
    class Meta:
        model = Despesas
        fields =  ('data','grupo','valor_contratado','valor_estimavel',)  
        widgets = {
                    'data': widgets.DateInput(attrs={'type': 'date'}),
                    'grupo': MyGrupoWidget,
                    }
        #exclude = ('codigo','descricao','valor_pago_FEFC','valor_pago_fundo_partidario','valor_pago_outros_rec', 'valor_nao_pago',)    