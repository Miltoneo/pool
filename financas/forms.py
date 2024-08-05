
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
class Grupo_despesa_pagar_Form(ModelForm):
    class Meta:
        model = Grupo_despesa
        fields =  ('total_pago_FEFC', 'total_pago_fundo_partidario', 'total_pago_outros_rec')   


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


#--------------------------------------------------------
#--------------------------------------------------------
class MyGrupoDespesaWidget(s2forms.Select2Widget):
    model= Grupo_despesa,
    search_fields = [
        'codigo__icontains',
    ]
    #queryset= Despesas.objects.all().annotate(sort_order=F('title')).order_by('-sort_order'))

#--------------------------------------------------------
class Pessoa_contrato_Form(ModelForm):
    class Meta:
        model = Pessoa_contratada
        fields =  "__all__"   
        widgets = {
                    'data': widgets.DateInput(attrs={'type': 'date'}),
                    'grupo': MyGrupoDespesaWidget,
                    }
        exclude = ('despesa_pessoal', 'valor_total')    


class Despesa_Form(ModelForm):
    class Meta:
        model = Despesas
        fields =  ('data','grupo','valor_contratado','valor_estimavel',)  
        widgets = {
                    'data': widgets.DateInput(attrs={'type': 'date'}),
                    #'grupo': MyGrupoDespesaWidget,
                     'grupo': Select2Widget,
                    #'grupo' : Select2Widget(queryset= Grupo_despesa.objects.all().order_by('codigo')),   
                    }

    """
    city = forms.ModelChoiceField(
        queryset=City.objects.all(),
        label=u"City",
        widget=ModelSelect2Widget(
            model=City,
            search_fields=['name__icontains'],
            dependent_fields={'country': 'country'},
            max_results=500,
        )
    )

     """
    
#-----------------------------------------
class Grupo_receitas_Form(ModelForm):
    class Meta:
        model = Grupo_receitas
        fields =  ('codigo', 'descricao')   
        #exclude = ('receita', 'despesa')        

#-----------------------------------------
class Receita_Candidato_Form(ModelForm):
    class Meta:
        model = Receita_Candidato
        fields =  ('total_financeiro', 'total_estimavel', 'total', )   
        #exclude = ('receita', 'despesa')      