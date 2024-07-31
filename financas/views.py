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

import locale
locale.setlocale(locale.LC_ALL,'')

#----------------------------------------------------------
def index(request):
  
  #-----------------------
  # inicialização
  #-----------------------

  now=datetime.datetime.now()
  #now.strftime("%Y-%m-%d"))
  ano_fiscal = now.strftime("%Y")
  mes = now.strftime("%m")
  msg =  ''

  request.session['sistema'] = 'Sistema de apoio ao candidato'
  
  if 'msg' in request.session:
    msg = request.session['msg_status']
  else:
    request.session['msg_status'] = 'Bem-vindo Miltinho'

  if 'ano_fiscal' in request.session:
   ano_fiscal = request.session['ano_fiscal']

  else:
    request.session['ano_fiscal'] = now.strftime("%Y")
    request.session['mes'] = now.strftime("%Y")
    ano_fiscal = now.strftime("%Y")


  #-----------------------------------------------------------------

  if request.method == 'POST':
    
    ano_fiscal = request.POST['mySelect']
    request.session['ano_fiscal'] =  request.POST['mySelect']
    request.session['msg_status'] = 'MUDOU O ANO!!! = ' + ano_fiscal

    #messages.success(request, 'Formulário salvo - yeepa!')
    return redirect('milenio:index')    
  
  else:  
    request.session['msg_status'] = 'Bem-vindo meu amor!!!'
    ds_candidatos= Candidato.objects.all()

    template = loader.get_template('financas/index.html')
    context = {
                'ano_fiscal'    : ano_fiscal,
                'lst_candidatos'   : ds_candidatos,
                'user'          : request.user,

                'msg'           : msg + 'mes:' + str(mes)
              }

    return HttpResponse(template.render(context, request))

#----------------------------------------------------------
# receitas
#---------------------------------------------------------
def candidato_receitas(request, candidato_id):
  
  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']

  request.session['candidato_id'] =   candidato_id
  candidato = Candidato.objects.all

  template = loader.get_template('financas/receitas/receitas.html')
  context = {
              'ano_fiscal'        : ano_fiscal,

              'candidato'         : candidato,
              'msg'               : msg,
              'user'              : request.user,
            }
  
  return HttpResponse(template.render(context, request))