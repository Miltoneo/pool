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


#------------------------------------------------------
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