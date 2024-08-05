from django.http import HttpResponse, FileResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from .models import *
from .geral import *
from .forms import *
import json
import datetime

# django tables
from django.views.generic import ListView
from django_tables2 import SingleTableView
from .tables import *

import locale
locale.setlocale(locale.LC_ALL,'')

#from https://django-tables2.readthedocs.io/en/latest/pages/installation.html
# teste
class ReceitastView(ListView):
    model = Grupo_receitas
    template_name = 'financas/receitas/receitas_main.html'  


#---------------------------------------------------
#teste2  >> funciona sem contexto para o template
class ReceitasTableView2( SingleTableView):
    model = Grupo_receitas
    queryset = Grupo_receitas.objects.all()
    table_class = ReceitasTable
    template_name = 'financas/receitas/receitas_main.html'
    paginate_by = 15

    context = {
                'ano_fiscal'        : 'teste',
              }

#---------------------------------------------------

class Receitas_main_TableView( SingleTableView):
       
    paginate_by = 15

    def get_table_class(self):
        return Receita_Candidato_Table 
    
    def get_queryset(self):
        candidato_id = self.request.session['candidato_id']
        candidato = Candidato.objects.get(id = candidato_id)
        qs = Receita_Candidato.objects.filter(candidato = candidato )
        #qs = qs.exclude(id=self.request.user.contestant.id)
        return qs
    
    def get_template_names(self):
        return 'financas/receitas/receitas_main.html'
        

    def get_context_data(self):
        context = super().get_context_data()

        candidato_id = self.request.session['candidato_id']
        candidato = Candidato.objects.get(id= candidato_id)

        context["msg"] = self.request.session['msg_status']
        context["ano_fiscal"] = self.request.session['ano_fiscal']
        context["candidato"] = candidato
        return context
 

#-------------------------------------------------
def receitas_main(request):
    msg =  request.session['msg_status']
    ano_fiscal = request.session['ano_fiscal']
    
    return redirect('financas:Receitas_main_TableView')


#------------------------------------------------------
def receitas_atualiza_resumo(request):
  
  #request.session['msg_status'] = chk_despesa_pessoal(request)

  return redirect('financas:receitas_main')

#------------------------------------------------------
def receitas_editar(request, receita_id):

  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']
  candidato_id = request.session['candidato_id']

  candidato = Candidato.objects.get(id= candidato_id)
  receita = Receita_Candidato.objects.get(id=receita_id).receita

  receita = Receita_Candidato.objects.get(receita=receita)
  if request.POST: 
      form = Receita_Candidato_Form(request.POST, instance=receita)    
      if form.is_valid():
        form.save()

        request.session['msg_status'] = 'Edição com sucesso!'
        return redirect('financas:receitas_main')
      else:
        request.session['msg_status'] = 'Falha edição !'
        return redirect('financas:receitas_main')

  else:
    
    template = loader.get_template('financas/receitas/receita_editar.html')
    form = Receita_Candidato_Form(instance=receita)  

    context = {
                'ano_fiscal' : ano_fiscal,
                'candidato'  : candidato,
                'form'       : form,
                'msg'        : msg,
                'user'       : request.user,
              }
    return HttpResponse(template.render(context, request))



