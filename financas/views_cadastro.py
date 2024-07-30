from django.http import HttpResponse, FileResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from .models import *
from .geral import *
from .forms import *
import datetime

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
        form.save()
   
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
  ano_fiscal = request.session['ano_fiscal']

  lst_candidato = Candidato.objects.all

  template = loader.get_template('financas/cadastro/cargo/cadastro_cargo.html')
  context = {
              'ano_fiscal'        : ano_fiscal,
              'lst_candidatos'       : lst_candidato,
              'msg'               : msg,
              'user'              : request.user,
            }
  
  return HttpResponse(template.render(context, request))

