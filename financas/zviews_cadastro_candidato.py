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

#------------------------------------------------------
def cadastro_candidato(request):
  
  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']


  lst_candidato = Candidato.objects.all

  template = loader.get_template('financas/cadastro/candidato/cadastro_candidato.html')
  context = {
              'ano_fiscal'        : ano_fiscal,
              'lst_candidato'      : lst_candidato,
              'msg'               : msg,
              'user'              : request.user,
            }
  
  return HttpResponse(template.render(context, request))

#------------------------------------------------------
def candidato_incluir(request):
  
  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']


  if request.POST: 
      form = candidato_Form(request.POST)    

      if form.is_valid():
        form.save()
        return redirect('financas:cadastro_candidato')

  template = loader.get_template('financas/cadastro/candidato/candidato_incluir.html')
  form = candidato_Form( )  

  context = {
              'form'       : form,
              'user'       : request.user,
              'msg'        : msg
            }
  return HttpResponse(template.render(context, request))

#------------------------------------------------------
def candidato_editar(request):
  
  msg =  request.session['msg_status']
  s_id_empresa = request.session['candidato']
  ano_fiscal = request.session['ano_fiscal']


  lst_candidato = Candidato.objects.all

  template = loader.get_template('financas/cadastro/cadastro_candidato.html')
  context = {
              'ano_fiscal'        : ano_fiscal,
              'lst_candidato'      : lst_candidato,
              'msg'               : msg,
              'user'              : request.user,
            }
  
  return HttpResponse(template.render(context, request))

#------------------------------------------------------
def candidato_excluir(request):
  
  msg =  request.session['msg_status']
  s_id_empresa = request.session['candidato']
  ano_fiscal = request.session['ano_fiscal']


  lst_candidato = Candidato.objects.all

  template = loader.get_template('financas/cadastro/cadastro_candidato.html')
  context = {
              'ano_fiscal'        : ano_fiscal,
              'lst_candidato'      : lst_candidato,
              'msg'               : msg,
              'user'              : request.user,
            }
  
  return HttpResponse(template.render(context, request))