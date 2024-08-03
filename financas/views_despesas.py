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

#-------------------------------------------------------
# DESPESAS
#-------------------------------------------------------
def despesas_main(request):
  
  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']
  candidato_id = request.session['candidato_id']
  situacao =  request.session['alm_desp_pessoal']

  candidato = Candidato.objects.get(id=candidato_id)
  lst_grupo_despesas = Grupo_despesa.objects.all().order_by('codigo','descricao')

  template = loader.get_template('financas/despesas/despesas_main.html') 
  context = {
              'ano_fiscal'        : ano_fiscal,
              'candidato'         : candidato,
              'lst_grupo_despesas'  : lst_grupo_despesas,
              'situacao'          : situacao,
              'msg'               : msg,
              'user'              : request.user,
            }
  
  return HttpResponse(template.render(context, request))

#------------------------------------------------------
def despesas_situacao(request):
  
  request.session['msg_status'] = chk_despesa_pessoal(request)

  return redirect('financas:pessoal_main')

#------------------------------------------------------
def despesas_lancamentos(request, candidato_id):
  
  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']

  candidato = Candidato.objects.get(id=candidato_id)
  lst_despesas = Despesas.objects.filter(candidato=candidato).order_by('data','grupo__codigo','grupo__descricao')

  template = loader.get_template('financas/despesas/despesas_lancamentos.html')
  context = {
                'ano_fiscal' : ano_fiscal,
                'candidato'  : candidato,
                'lst_despesas' : lst_despesas,
                'msg'        : msg,
                'user'       : request.user,
              }
  return HttpResponse(template.render(context, request))

#------------------------------------------------------
def despesas_incluir(request, candidato_id):
  
  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']

  candidato = Candidato.objects.get(id=candidato_id)

  if request.POST: 
      form = Despesa_Form(request.POST)    

      if form.is_valid():
        despesa = form.save(commit=False)
        despesa.candidato= candidato
        despesa.save()

        request.session['msg_status'] = 'doador incluído com sucesso!'
        return redirect('financas:despesas_lancamentos', candidato_id)
      else:
        request.session['msg_status'] = 'Falha inclusão !'
        return redirect('financas:despesas_lancamentos', candidato_id)

  else:
    
    template = loader.get_template('financas/despesas/despesas_editar_incluir.html')
    form = Despesa_Form( )  

    context = {
                'ano_fiscal' : ano_fiscal,
                'candidato'  : candidato,
                'form'       : form,
                'msg'        : msg,
                'user'       : request.user,
              }
    return HttpResponse(template.render(context, request))

#------------------------------------------------------
def despesas_editar(request, despesa_id):

  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']
  candidato_id = request.session['candidato_id']

  candidato = Candidato.objects.get(id= candidato_id)

  despesa = Despesas.objects.get(id=despesa_id)
  if request.POST: 
      form = Despesa_Form(request.POST, instance=despesa)    
      if form.is_valid():
        form.save()

        request.session['msg_status'] = 'doador incluído com sucesso!'
        return redirect('financas:despesas_lancamentos', candidato_id)
      else:
        request.session['msg_status'] = 'Falha inclusão !'
        return redirect('financas:despesas_lancamentos', candidato_id)

  else:
    
    template = loader.get_template('financas/despesas/despesas_editar_incluir.html')
    form = Despesa_Form(instance=despesa)  

    context = {
                'ano_fiscal' : ano_fiscal,
                'candidato'  : candidato,
                'form'       : form,
                'msg'        : msg,
                'user'       : request.user,
              }
    return HttpResponse(template.render(context, request))

#------------------------------------------------------
def despesas_excluir(request, despesa_id):
  
  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']

  candidato_id = request.session['candidato_id']  
 
  Despesas.objects.get(id=despesa_id).delete()
  request.session['msg_status'] = 'exclusão com sucesso!!!'

  return redirect('financas:despesas_lancamentos', candidato_id)

#-------------------------------------------------------
def despesa_atualiza_resumo(request):
  
  request.session['msg_status'] = totaliza_grupo_despesas(request)

  return redirect('financas:despesas_main')

#------------------------------------------------------
def grupo_despesa_editar(request, grupo_id):

  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']
  candidato_id = request.session['candidato_id']

  candidato = Candidato.objects.get(id= candidato_id)

  grupo_despesa = Grupo_despesa.objects.get(id=grupo_id)
  if request.POST: 
      form = Grupo_despesa_Form(request.POST, instance=grupo_despesa)    
      if form.is_valid():
        form.save()

        request.session['msg_status'] = 'doador incluído com sucesso!'
        return redirect('financas:despesas_lancamentos', candidato_id)
      else:
        request.session['msg_status'] = 'Falha inclusão !'
        return redirect('financas:despesas_lancamentos', candidato_id)

  else:
    
    template = loader.get_template('financas/despesas/grupo_despesa_editar.html')
    form = Grupo_despesa_Form(instance=grupo_despesa)  

    context = {
                'ano_fiscal' : ano_fiscal,
                'candidato'  : candidato,
                'grupo_despesa': grupo_despesa,
                'form'       : form,
                'msg'        : msg,
                'user'       : request.user,
              }
    return HttpResponse(template.render(context, request))