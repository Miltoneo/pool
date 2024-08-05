from django.http import HttpResponse, FileResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from .models import *
from .geral import *
from .forms import *
import datetime

# django tables
from django.views.generic import ListView
from django_tables2 import SingleTableView
from .tables import *

import locale
locale.setlocale(locale.LC_ALL,'')

#---------------------------------------------------------------
def cadastro_main(request):
  
  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']

  template = loader.get_template('financas/cadastro/cadastro_main.html')
  context = {
              'ano_fiscal'        : ano_fiscal,
              'msg'               : msg,
              'user'              : request.user,
            }
  
  return HttpResponse(template.render(context, request))

#----------------------------------------------------------
# CADASTRO CIDADE
#---------------------------------------------------------
def cadastro_cidade(request):
  
  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']

  lst_cidades = Cidade.objects.all

  template = loader.get_template('financas/cadastro/cidade/cadastro_cidade.html')
  context = {
              'ano_fiscal'        : ano_fiscal,
              'lst_cidades'        : lst_cidades,
              'msg'               : msg,
              'user'              : request.user,
            }
  
  return HttpResponse(template.render(context, request))

#------------------------------------------------------
def cidade_incluir(request):
  
  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']

  if request.POST: 
      form = cidade_Form(request.POST)    

      if form.is_valid():
        form.save()
   
        request.session['msg_status'] = 'Cidade incluída com sucesso!'
        return redirect('financas:cadastro_cidade')
      else:
        request.session['msg_status'] = 'Falha inclusão !'
        return redirect('financas:cadastro_cidade')

  else:
    
    template = loader.get_template('financas/cadastro/cidade/cidade_editar_incluir.html')
    form = cidade_Form( )  

    context = {
                'form'       : form,
                'user'       : request.user,
                'msg'        : msg
              }
    return HttpResponse(template.render(context, request))

#------------------------------------------------------
def cidade_editar(request, cidade_id):

  msg =  request.session['msg_status']
  #cidade_id = request.session['cidade_id']
  ano_fiscal = request.session['ano_fiscal']

  cidade = Cidade.objects.get(id=cidade_id)
  if request.method == 'POST':

    form = cidade_Form(request.POST, instance = cidade)
    if form.is_valid():
      form.save()
      request.session['msg_status'] = 'Edição com sucesso!!!'

      return redirect('financas:cadastro_cidade')     

    else:
      request.session['msg_status'] = 'Falha na edição dos dados'
      return redirect('financas:cadastro_cidade')    
    
  else:
    #msg =  empresa_nome
    form = cidade_Form(instance = cidade)
    template = loader.get_template('financas/cadastro/cidade/cidade_editar_incluir.html')
    context = {
                'cidade'     : cidade,
                'ano_fiscal'  : ano_fiscal,
                'form'        : form,
                'msg'         : msg,
                'user'        : request.user,
              }
  
    return HttpResponse(template.render(context, request))

#------------------------------------------------------
def cidade_excluir(request, cidade_id):
  
  msg =  request.session['msg_status']

  cidade = Cidade.objects.get(id = cidade_id)
  cidade.delete()
  request.session['msg_status'] = 'exclusão com sucesso!!!'

  return redirect('financas:cadastro_cidade')    

#----------------------------------------------------------
# CADASTRO PESSOA
#---------------------------------------------------------
def cadastro_pessoa(request):
  
  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']


  lst_pessoas = Pessoa.objects.all

  template = loader.get_template('financas/cadastro/pessoa/cadastro_pessoa.html')
  context = {
              'ano_fiscal'        : ano_fiscal,
              'lst_pessoas'       : lst_pessoas,
              'msg'               : msg,
              'user'              : request.user,
            }
  
  return HttpResponse(template.render(context, request))

#------------------------------------------------------
def pessoa_incluir(request):
  
  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']

  if request.POST: 
      form = Pessoa_Form(request.POST)    

      if form.is_valid():
        form.save()
   
        request.session['msg_status'] = 'pessoa incluída com sucesso!'
        return redirect('financas:cadastro_pessoa')
      else:
        request.session['msg_status'] = 'Falha inclusão !'
        return redirect('financas:cadastro_pessoa')

  else:
    
    template = loader.get_template('financas/cadastro/pessoa/pessoa_editar_incluir.html')
    form = Pessoa_Form( )  

    context = {
                'form'       : form,
                'user'       : request.user,
                'msg'        : msg
              }
    return HttpResponse(template.render(context, request))

#------------------------------------------------------
def pessoa_editar(request, pessoa_id):

  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']

  pessoa = Pessoa.objects.get(id=pessoa_id)
  if request.method == 'POST':

    form = Pessoa_Form(request.POST, instance = pessoa)
    if form.is_valid():
      form.save()
      request.session['msg_status'] = 'Edição com sucesso!!!'
      return redirect('financas:cadastro_pessoa')     

    else:
      request.session['msg_status'] = 'Falha na edição dos dados'
      return redirect('financas:cadastro_pessoa')    
    
  else:

    form = Pessoa_Form(instance = pessoa)
    template = loader.get_template('financas/cadastro/pessoa/pessoa_editar_incluir.html')
    context = {
                'pessoa'     : pessoa,
                'ano_fiscal'  : ano_fiscal,
                'form'        : form,
                'msg'         : msg,
                'user'        : request.user,
              }
  
    return HttpResponse(template.render(context, request))

#------------------------------------------------------
def pessoa_excluir(request, pessoa_id):
  
  msg =  request.session['msg_status']

  pessoa = Pessoa.objects.get(id = pessoa_id)
  pessoa.delete()
  request.session['msg_status'] = 'exclusão com sucesso!!!'

  return redirect('financas:cadastro_pessoa')    


#----------------------------------------------------------
# CADASTRO PARTIDO
#---------------------------------------------------------
def cadastro_partido(request):
  
  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']


  lst_partidos = Partido.objects.all
  msg = 'teste'
  template = loader.get_template('financas/cadastro/partido/cadastro_partido.html')
  context = {
              'ano_fiscal'        : ano_fiscal,
              'lst_partidos'       : lst_partidos,
              'msg'               : msg,
              'user'              : request.user,
            }
  
  return HttpResponse(template.render(context, request))

#------------------------------------------------------
def partido_incluir(request):
  
  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']

  if request.POST: 
      form = Partido_Form(request.POST)    

      if form.is_valid():
        form.save()
   
        request.session['msg_status'] = 'partido incluída com sucesso!'
        return redirect('financas:cadastro_partido')
      else:
        request.session['msg_status'] = 'Falha inclusão !'
        return redirect('financas:cadastro_partido')

  else:
    
    template = loader.get_template('financas/cadastro/partido/partido_editar_incluir.html')
    form = Partido_Form( )  

    context = {
                'form'       : form,
                'user'       : request.user,
                'msg'        : msg
              }
    return HttpResponse(template.render(context, request))

#------------------------------------------------------
def partido_editar(request, partido_id):

  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']

  partido = Partido.objects.get(id=partido_id)
  if request.method == 'POST':

    form = Partido_Form(request.POST, instance = partido)
    if form.is_valid():
      form.save()
      request.session['msg_status'] = 'Edição com sucesso!!!'
      return redirect('financas:cadastro_partido')     

    else:
      request.session['msg_status'] = 'Falha na edição dos dados'
      return redirect('financas:cadastro_partido')    
    
  else:

    form = Partido_Form(instance = partido)
    template = loader.get_template('financas/cadastro/partido/partido_editar_incluir.html')
    context = {
                'partido'     : partido,
                'ano_fiscal'  : ano_fiscal,
                'form'        : form,
                'msg'         : msg,
                'user'        : request.user,
              }
  
    return HttpResponse(template.render(context, request))

#------------------------------------------------------
def partido_excluir(request, partido_id):
  
  msg =  request.session['msg_status']

  partido = Partido.objects.get(id = partido_id)
  partido.delete()
  request.session['msg_status'] = 'exclusão com sucesso!!!'

  return redirect('financas:cadastro_partido')  


#----------------------------------------------------------
# CADASTRO CARGO
#---------------------------------------------------------
def cadastro_cargo(request):
  
  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']


  lst_cargos = Cargo.objects.all

  template = loader.get_template('financas/cadastro/cargo/cadastro_cargo.html')
  context = {
              'ano_fiscal'        : ano_fiscal,
              'lst_cargos'       : lst_cargos,
              'msg'               : msg,
              'user'              : request.user,
            }
  
  return HttpResponse(template.render(context, request))

#------------------------------------------------------
def cargo_incluir(request):
  
  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']

  if request.POST: 
      form = Cargo_Form(request.POST)    

      if form.is_valid():
        form.save()
   
        request.session['msg_status'] = 'cargo incluída com sucesso!'
        return redirect('financas:cadastro_cargo')
      else:
        request.session['msg_status'] = 'Falha inclusão !'
        return redirect('financas:cadastro_cargo')

  else:
    
    template = loader.get_template('financas/cadastro/cargo/cargo_editar_incluir.html')
    form = Cargo_Form( )  

    context = {
                'form'       : form,
                'user'       : request.user,
                'msg'        : msg
              }
    return HttpResponse(template.render(context, request))

#------------------------------------------------------
def cargo_editar(request, cargo_id):

  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']

  cargo = Cargo.objects.get(id=cargo_id)
  if request.method == 'POST':

    form = Cargo_Form(request.POST, instance = cargo)
    if form.is_valid():
      form.save()
      request.session['msg_status'] = 'Edição com sucesso!!!'
      return redirect('financas:cadastro_cargo')     

    else:
      request.session['msg_status'] = 'Falha na edição dos dados'
      return redirect('financas:cadastro_cargo')    
    
  else:

    form = Cargo_Form(instance = cargo)
    template = loader.get_template('financas/cadastro/cargo/cargo_editar_incluir.html')
    context = {
                'cargo'     : cargo,
                'ano_fiscal'  : ano_fiscal,
                'form'        : form,
                'msg'         : msg,
                'user'        : request.user,
              }
  
    return HttpResponse(template.render(context, request))

#------------------------------------------------------
def cargo_excluir(request, cargo_id):
  
  msg =  request.session['msg_status']

  cargo = Cargo.objects.get(id = cargo_id)
  cargo.delete()
  request.session['msg_status'] = 'exclusão com sucesso!!!'

  return redirect('financas:cadastro_cargo') 

#----------------------------------------------------------
# CADASTRO CANDIDATO
#---------------------------------------------------------
def cadastro_candidato(request):
  
  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']

  lst_candidatos = Candidato.objects.all

  template = loader.get_template('financas/cadastro/candidato/cadastro_candidato.html')
  context = {
              'ano_fiscal'        : ano_fiscal,
              'lst_candidatos'    : lst_candidatos,
              'msg'               : msg,
              'user'              : request.user,
            }
  
  return HttpResponse(template.render(context, request))

#------------------------------------------------------
def candidato_incluir(request):
  
  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']

  if request.POST: 
      form = Candidato_Form(request.POST)    

      if form.is_valid():
        
        candidato = form.save(commit= False)

        # calcula limites de gastos
        val_teto_gastos = Teto_gasto_cargo.objects.get(cidade = candidato.pessoa.cidade, cargo=candidato.cargo).valor
        candidato.val_permitido_autofinanciamento =  val_teto_gastos * (LIMITE_PERCENTUAL_AUTO_FINANCIAMENTO /100)
        candidato.val_percent_permitido_autofinanciamento = LIMITE_PERCENTUAL_AUTO_FINANCIAMENTO
        candidato.save()
   
        # cria doador [candidato] para autofinanciamento 
        doador = Doador.objects.create(pessoa=candidato.pessoa,\
                                        candidato= candidato)


        request.session['msg_status'] = 'candidato incluído com sucesso!'
        return redirect('financas:cadastro_candidato')
      else:
        request.session['msg_status'] = 'Falha inclusão !'
        return redirect('financas:cadastro_candidato')

  else:
    
    template = loader.get_template('financas/cadastro/candidato/candidato_editar_incluir.html')
    form = Candidato_Form( )  

    context = {
                'form'       : form,
                'user'       : request.user,
                'msg'        : msg
              }
    return HttpResponse(template.render(context, request))

#------------------------------------------------------
def candidato_editar(request, candidato_id):

  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']

  candidato = Candidato.objects.get(id=candidato_id)
  if request.method == 'POST':

    form = Candidato_Form(request.POST, instance = candidato)
    if form.is_valid():
      form.save()
      request.session['msg_status'] = 'Edição com sucesso!!!'
      return redirect('financas:cadastro_candidato')     

    else:
      request.session['msg_status'] = 'Falha na edição dos dados'
      return redirect('financas:cadastro_candidato')    
    
  else:

    form = Candidato_Form(instance = candidato)
    template = loader.get_template('financas/cadastro/candidato/candidato_editar_incluir.html')
    context = {
                'candidato'     : candidato,
                'ano_fiscal'  : ano_fiscal,
                'form'        : form,
                'msg'         : msg,
                'user'        : request.user,
              }
  
    return HttpResponse(template.render(context, request))

#------------------------------------------------------
def candidato_excluir(request, candidato_id):
  
  msg =  request.session['msg_status']

  candidato = Candidato.objects.get(id = candidato_id)
  candidato.delete()
  request.session['msg_status'] = 'exclusão com sucesso!!!'

  return redirect('financas:cadastro_candidato') 


#----------------------------------------------------------
# CADASTRO GRUPO DESPESAS
#---------------------------------------------------------
def cadastro_gpo_despesas(request):
  
  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']

  lst_gpo_despesas = Grupo_despesa.objects.all

  template = loader.get_template('financas/cadastro/gpo_despesas/gpo_despesas.html')
  context = {
              'ano_fiscal'        : ano_fiscal,
              'lst_gpo_despesas'    : lst_gpo_despesas,
              'msg'               : msg,
              'user'              : request.user,
            }
  
  return HttpResponse(template.render(context, request))

#------------------------------------------------------
def gpo_despesas_incluir(request):
  
  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']

  if request.POST: 
      form = Gpo_despesas_Form(request.POST)    

      if form.is_valid():
        form.save()
   
        request.session['msg_status'] = 'gpo_despesa incluído com sucesso!'
        return redirect('financas:cadastro_gpo_despesas')
      else:
        request.session['msg_status'] = 'Falha inclusão !'
        return redirect('financas:cadastro_gpo_despesas')

  else:
    
    template = loader.get_template('financas/cadastro/gpo_despesas/gpo_despesas_editar_incluir.html')
    form = Gpo_despesas_Form( )  

    context = {
                'form'       : form,
                'user'       : request.user,
                'msg'        : msg
              }
    return HttpResponse(template.render(context, request))

#------------------------------------------------------
def gpo_despesas_editar(request, gpo_despesas_id):

  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']

  gpo_despesa = Grupo_despesa.objects.get(id=gpo_despesas_id)
  if request.method == 'POST':

    form = Gpo_despesas_Form(request.POST, instance = gpo_despesa)
    if form.is_valid():
      form.save()
      request.session['msg_status'] = 'Edição com sucesso!!!'
      return redirect('financas:cadastro_gpo_despesas')     

    else:
      request.session['msg_status'] = 'Falha na edição dos dados'
      return redirect('financas:cadastro_gpo_despesas')    
    
  else:

    form = Gpo_despesas_Form(instance = gpo_despesa)
    template = loader.get_template('financas/cadastro/gpo_despesas/gpo_despesas_editar_incluir.html')
    context = {
                'gpo_despesa'     : gpo_despesa,
                'ano_fiscal'  : ano_fiscal,
                'form'        : form,
                'msg'         : msg,
                'user'        : request.user,
              }
  
    return HttpResponse(template.render(context, request))

#------------------------------------------------------
def gpo_despesas_excluir(request, gpo_despesas_id):
  
  msg =  request.session['msg_status']

  gpo_despesa = Grupo_despesa.objects.get(id = gpo_despesas_id)
  gpo_despesa.delete()
  request.session['msg_status'] = 'exclusão com sucesso!!!'

  return redirect('financas:cadastro_gpo_despesas') 


#----------------------------------------------------------
# CADASTRO ITEM DE DESPESAS
#---------------------------------------------------------
def cadastro_grupo_despesas(request):
  
  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']

  lst_grupo_despesas = Grupo_despesa.objects.all().order_by('codigo','descricao')

  template = loader.get_template('financas/cadastro/grupo_despesas/grupo_despesas.html')
  context = {
              'ano_fiscal'        : ano_fiscal,
              'lst_grupo_despesas'    : lst_grupo_despesas,
              'msg'               : msg,
              'user'              : request.user,
            }
  
  return HttpResponse(template.render(context, request))

#------------------------------------------------------
def grupo_despesas_incluir(request):
  
  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']

  if request.POST: 
      form = Grupo_despesa_Form(request.POST)    

      if form.is_valid():
        form.save()
   
        request.session['msg_status'] = 'gpo_despesa incluído com sucesso!'
        return redirect('financas:cadastro_grupo_despesas')
      else:
        request.session['msg_status'] = 'Falha inclusão !'
        return redirect('financas:cadastro_grupo_despesas')

  else:
    
    template = loader.get_template('financas/cadastro/grupo_despesas/grupo_despesas_editar_incluir.html')
    form = Grupo_despesa_Form( )  

    context = {
                'form'       : form,
                'user'       : request.user,
                'msg'        : msg
              }
    return HttpResponse(template.render(context, request))

#------------------------------------------------------
def grupo_despesas_editar(request, grupo_despesas_id):

  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']

  item_despesa = Grupo_despesa.objects.get(id=grupo_despesas_id)
  if request.method == 'POST':
     
    form = Grupo_despesa_Form(request.POST, instance = item_despesa)
    if form.is_valid():
      form.save()
      request.session['msg_status'] = 'Edição com sucesso!!!'
      return redirect('financas:cadastro_grupo_despesas')     

    else:
      request.session['msg_status'] = 'Falha na edição dos dados'
      return redirect('financas:cadastro_grupo_despesas')    
    
  else:

    form = Grupo_despesa_Form(instance = item_despesa)
    template = loader.get_template('financas/cadastro/grupo_despesas/grupo_despesas_editar_incluir.html')
    context = {
                'ano_fiscal'  : ano_fiscal,
                'form'        : form,
                'msg'         : msg,
                'user'        : request.user,
              }
  
    return HttpResponse(template.render(context, request))

#------------------------------------------------------
def grupo_despesas_excluir(request, grupo_despesas_id):
  
  msg =  request.session['msg_status']

  Grupo_despesa.objects.get(id = grupo_despesas_id).delete()
  request.session['msg_status'] = 'exclusão com sucesso!!!'

  return redirect('financas:cadastro_grupo_despesas') 


#----------------------------------------------------------
# CADASTRO DOADOR
#---------------------------------------------------------
def doador_incluir(request):
  
  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']
  candidato_id = request.session['candidato_id']

  candidato = Candidato.objects.get(id=candidato_id)

  if request.POST: 
      form = Doador_Form(request.POST)    

      if form.is_valid():
        doador = form.save(commit=False)
        doador.candidato = candidato
        doador.val_limite_doacao_estimavel = LIMITE_DOACAO_ESTIMAVEL
        doador.val_limite_doacao_financeira = doador.pessoa.rendimento_bruto_irpf2024 * (LIMITE_PERCENTUAL_DOACAO_SOBRE_RENDIMENTO_IRPF2024 / 100)
        doador.val_limite_total = doador.val_limite_doacao_estimavel + doador.val_limite_doacao_financeira
        doador.save()

        request.session['msg_status'] = 'doador incluído com sucesso!'
        return redirect('financas:doacoes_main')
      else:
        request.session['msg_status'] = 'Falha inclusão !'
        return redirect('financas:doacoes_main')

  else:
    
    template = loader.get_template('financas/cadastro/doador/doador_editar_incluir.html')
    form = Doador_Form( )  

    context = {
                'form'       : form,
                'user'       : request.user,
                'msg'        : msg
              }
    return HttpResponse(template.render(context, request))

#------------------------------------------------------
def doador_editar(request, doador_id):

  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']

  doador = Doador.objects.get(id=doador_id)
  if request.method == 'POST':

    form = Doador_Form(request.POST, instance = doador)
    if form.is_valid():
      form.save()
      request.session['msg_status'] = 'Edição com sucesso!!!'
      return redirect('financas:doacoes_main')     

    else:
      request.session['msg_status'] = 'Falha na edição dos dados'
      return redirect('financas:doacoes_main')    
    
  else:

    form = Doador_Form(instance = doador)
    template = loader.get_template('financas/cadastro/doador/doador_editar_incluir.html')
    context = {
                'doador'     : doador,
                'ano_fiscal'  : ano_fiscal,
                'form'        : form,
                'msg'         : msg,
                'user'        : request.user,
              }
  
    return HttpResponse(template.render(context, request))

#------------------------------------------------------
def doador_excluir(request, doador_id):
  
  msg =  request.session['msg_status']

  doador = Doador.objects.get(id = doador_id)
  doador.delete()
  request.session['msg_status'] = 'exclusão com sucesso!!!'

  return redirect('financas:doacoes_main') 

#----------------------------------------------------------
# CADASTRO TETO GASTOS
#---------------------------------------------------------
def teto_gatos_main(request):
  
  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']

  lst_tgastos = Teto_gasto_cargo.objects.all().order_by('cidade', 'cargo__nome')

  template = loader.get_template('financas/cadastro/teto_gastos/tgastos_main.html') 
  context = {
              'ano_fiscal'        : ano_fiscal,
              'lst_tgastos'       : lst_tgastos,
              'msg'               : '123',
              'user'              : request.user,
            }
  
  return HttpResponse(template.render(context, request))


def tgastos_incluir(request):
  
  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']

  if request.POST: 
      form = Teto_gastos_Form(request.POST)    

      if form.is_valid():
        form.save()

        request.session['msg_status'] = 'Teto de gastos incluído com sucesso!'
        return redirect('financas:teto_gatos_main')
      else:
        request.session['msg_status'] = 'Falha inclusão !'
        return redirect('financas:teto_gatos_main')

  else:
    
    template = loader.get_template('financas/cadastro/tgastos/tgastos_editar_incluir.html')
    form = Teto_gastos_Form( )  

    context = {
                'form'       : form,
                'user'       : request.user,
                'msg'        : msg
              }
    return HttpResponse(template.render(context, request))

#------------------------------------------------------
def tgastos_editar(request, tgastos_id):

  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']

  tgastos = Teto_gasto_cargo.objects.get(id=tgastos_id)
  if request.method == 'POST':

    form = Teto_gastos_Form(request.POST, instance = tgastos)
    if form.is_valid():
      form.save()
      request.session['msg_status'] = 'Edição com sucesso!!!'
      return redirect('financas:teto_gatos_main')     

    else:
      request.session['msg_status'] = 'Falha na edição dos dados'
      return redirect('financas:teto_gatos_main')    
    
  else:

    form = Teto_gastos_Form(instance = tgastos)
    template = loader.get_template('financas/cadastro/tgastos/tgastos_editar_incluir.html')
    context = {
                'tgastos'     : tgastos,
                'ano_fiscal'  : ano_fiscal,
                'form'        : form,
                'msg'         : msg,
                'user'        : request.user,
              }
  
    return HttpResponse(template.render(context, request))

#------------------------------------------------------
def tgastos_excluir(request, tgastos_id):
  
  msg =  request.session['msg_status']

  tgastos = Teto_gasto_cargo.objects.get(id = tgastos_id)
  tgastos.delete()
  request.session['msg_status'] = 'exclusão com sucesso!!!'

  return redirect('financas:teto_gatos_main') 

#----------------------------------------------------------
# CADASTRO ITEM DE RECEITAS
#---------------------------------------------------------

class cadastro_receitas_main_TableView( SingleTableView):
    model = Grupo_receitas
    queryset = Grupo_receitas.objects.all()
    table_class = Cad_Receitas_Table
    template_name = 'financas/cadastro/grupo_receitas/grupo_receitas_main.html'
    paginate_by = 15

    #testing
    def get_context_data(self):
        context = super().get_context_data()

        context["msg"] = self.request.session['msg_status']
        context["ano_fiscal"] = self.request.session['ano_fiscal']
        return context

#------------------------------------------------------
def grupo_receitas_incluir(request):
  
  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']

  if request.POST: 
      form = Grupo_receitas_Form(request.POST)    

      if form.is_valid():
        form.save()
   
        request.session['msg_status'] = 'Inclusão com sucesso!'
        return redirect('financas:cadastro_receitas_main_TableView')
      else:
        request.session['msg_status'] = 'Falha na inclusão !'
        return redirect('financas:cadastro_receitas_main_TableView')

  else:
    
    template = loader.get_template('financas/cadastro/grupo_receitas/grupo_receitas_editar_incluir.html')
    form = Grupo_receitas_Form( )  

    context = {
                'form'       : form,
                'user'       : request.user,
                'msg'        : msg
              }
    return HttpResponse(template.render(context, request))
  
#------------------------------------------------------
def grupo_receitas_editar(request, grupo_receitas_id):

  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']

  gpo_receitas = Grupo_receitas.objects.get(id=grupo_receitas_id)
  if request.method == 'POST':

    form = Grupo_receitas_Form(request.POST, instance = gpo_receitas)
    if form.is_valid():
      form.save()
      request.session['msg_status'] = 'Edição com sucesso!!!'
      return redirect('financas:cadastro_receitas_main_TableView')     

    else:
      request.session['msg_status'] = 'Falha na edição dos dados'
      return redirect('financas:cadastro_receitas_main_TableView')    
    
  else:

    form = Grupo_receitas_Form(instance = gpo_receitas)
    template = loader.get_template('financas/cadastro/grupo_receitas/grupo_receitas_editar_incluir.html')
    context = {
                'ano_fiscal'  : ano_fiscal,
                'form'        : form,
                'msg'         : msg,
                'user'        : request.user,
              }
  
    return HttpResponse(template.render(context, request))
  
#------------------------------------------------------
def grupo_receitas_excluir(request, grupo_receitas_id):
  
  msg =  request.session['msg_status']

  ds = Grupo_receitas.objects.get(id = grupo_receitas_id)
  ds.delete()
  request.session['msg_status'] = 'exclusão com sucesso!!!'

  return redirect('financas:cadastro_receitas_main_TableView') 