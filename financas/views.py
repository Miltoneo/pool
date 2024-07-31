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

  request.session['nome_aplicativo'] = 'Sistema de apoio ao candidato'
  
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


#----------------------------------------------------------
# Doações PESSOA FÍSICA
#---------------------------------------------------------
def doacoes_main(request):
  
  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']
  candidadto_id = request.session['candidato_id']

  candidato = Candidato.objects.get(id=candidadto_id)
  lst_doadores = Doador.objects.all

  template = loader.get_template('financas/doacoes_pessoa_fisica/doacoes_main.html') 
  context = {
              'ano_fiscal'        : ano_fiscal,
              'candidato'       : candidato,
              'lst_doadores'      : lst_doadores,
              'msg'               : msg,
              'user'              : request.user,
            }
  
  return HttpResponse(template.render(context, request))


#------------------------------------------------------
#------------------------------------------------------
def lst_doacoes_doador(request, doador_id):
  
  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']

  doador = Doador.objects.get(id=doador_id)
  lst_doacoes = Doacoes.objects.filter(doador = doador_id).order_by('data').order_by('tipo_doacao')

  template = loader.get_template('financas/doacoes_pessoa_fisica/doacoes_doador.html')
  context = {
              'ano_fiscal'        : ano_fiscal,
              'doador'            : doador,
              'lst_doacoes'       : lst_doacoes,
              'msg'               : msg,
              'user'              : request.user,
            }
  
  return HttpResponse(template.render(context, request))

#------------------------------------------------------
#------------------------------------------------------
def doacao_incluir(request, doador_id):
  
  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']

  doador = Doador.objects.get(id=doador_id)
  if request.POST: 
      form = Doacao_Form(request.POST)    

      if form.is_valid():
        doacao = form.save(commit=False)
        doacao.doador = doador

        # totaliza doações
        if(doacao.tipo_doacao == TIPO_DOACAO_FINANCEIRA):
          doador.total_doacao_financeira += doacao.valor
        else:
          doador.total_doacao_estimavel += doacao.valor 

        doador.total_doacao_totalizado = doador.total_doacao_financeira + doador.total_doacao_estimavel 

        # save
        doador.save()
        doacao.save()

        request.session['msg_status'] = 'doador incluído com sucesso!'
        return redirect('financas:lst_doacoes_doador', doador_id)
      else:
        request.session['msg_status'] = 'Falha inclusão !'
        return redirect('financas:lst_doacoes_doador', doador_id)

  else:
    
    template = loader.get_template('financas/doacoes_pessoa_fisica/doacao_editar_incluir.html')
    form = Doacao_Form( )  

    context = {
                'ano_fiscal' : ano_fiscal,
                'doador'     : doador,
                'form'       : form,
                'msg'        : msg,
                'user'       : request.user,
              }
    return HttpResponse(template.render(context, request))
  
#----------------------------------------------------------
# AutoFinanciamento
#---------------------------------------------------------
def autofinancia_main(request):
  
  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']
  candidadto_id = request.session['candidato_id']

  candidato = Candidato.objects.get(id=candidadto_id)
  teto_gasto = Teto_gasto_cargo.objects.get(cidade=candidato.pessoa.cidade, cargo=candidato.cargo).valor


  lst_doadores = Doador.objects.all

  template = loader.get_template('financas/autofinancia/autofinancia_main.html') 
  context = {
              'ano_fiscal'        : ano_fiscal,
              'candidato'         : candidato,
              'teto_gasto'        : teto_gasto,
              'lst_doadores'      : lst_doadores,
              'msg'               : msg,
              'user'              : request.user,
            }
  
  return HttpResponse(template.render(context, request))

#------------------------------------------------------
#------------------------------------------------------
def autofinanciameto_incluir(request, candidato_id):
  
  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']

  candidato = Candidato.objects.get(id=candidato_id)
  if request.POST: 
      form = Doacao_Form(request.POST)    

      if form.is_valid():
        doacao = form.save(commit=False)
        doacao.candidato = candidato

        # totaliza doações
        if (doacao.tipo_doacao == TIPO_DOACAO_FINANCEIRA):
            candidato.total_autofin_financeiro += doacao.valor

        elif (doacao.tipo_doacao == TIPO_DOACAO_ESTIMAVEL_BENS):
            candidato.total_autofin_estimavel_bens += doacao.valor 

        elif (doacao.tipo_doacao == TIPO_DOACAO_ESTIMAVEL_VEICULOS):
            candidato.total_autofin_estimavel_veiculos += doacao.valor 

        candidato.total_autofin_totalizado = candidato.total_autofin_financeiro +\
                                              candidato.total_autofin_estimavel_bens + \
                                              candidato.total_autofin_estimavel_veiculos

        # save
        candidato.save()
        doacao.save()

        request.session['msg_status'] = 'doador incluído com sucesso!'
        return redirect('financas:autofinancia_main')
      else:
        request.session['msg_status'] = 'Falha inclusão !'
        return redirect('financas:autofinancia_main')

  else:
    
    template = loader.get_template('financas/autofinancia/autofinancia_editar_incluir.html')
    form = Doacao_Form( )  

    context = {
                'ano_fiscal' : ano_fiscal,
                'candidato'     : candidato,
                'form'       : form,
                'msg'        : msg,
                'user'       : request.user,
              }
    return HttpResponse(template.render(context, request))

#----------------------------------------------------------
# TETO DE GASTOS
#---------------------------------------------------------
def teto_gatos_main(request):
  
  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']

  lst_tgastos = Teto_gasto_cargo.objects.all().order_by('cidade')

  template = loader.get_template('financas/teto_gastos/tgastos_main.html') 
  context = {
              'ano_fiscal'        : ano_fiscal,
              'lst_tgastos'       : lst_tgastos,
              'msg'               : '123',
              'user'              : request.user,
            }
  
  return HttpResponse(template.render(context, request))