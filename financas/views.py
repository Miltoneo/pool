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
# UTILIZA COMO ENTRADA PARA PREPARAR AMBIENTE
#---------------------------------------------------------
def candidato_receitas(request, candidato_id):
  
  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']
  request.session['candidato_id'] =   candidato_id
  request.session['alm_autofinanciamento'] = 'Pendente'
  request.session['alm_desp_pessoal'] = 'Normal'

  candidato= Candidato.objects.get(id=candidato_id)
  pessoa = Pessoa.objects.get(id=candidato.pessoa.id)

  # RECUPERA DOADOR PARA AUTOFINANCIAMENTO
  doador = Doador.objects.get(pessoa=pessoa, candidato=candidato)
  request.session['auto_doador_id'] =   doador.id

  # VERIFICA DESPESA DE PESSOAL
  despesa_pessoal = Despesa_pessoal.objects.get_or_create(candidato=candidato)
  #despesas = Despesas.objects.get_or_create(candidato=candidato)

  template = loader.get_template('financas/receitas/receitas.html')
  context = {
              'ano_fiscal'        : ano_fiscal,

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
  candidato_id = request.session['candidato_id']
  auto_doador_id = request.session['auto_doador_id']

  candidato = Candidato.objects.get(id=candidato_id)
  lst_doadores =  Doador.objects.filter(candidato = candidato).exclude(id=auto_doador_id)

  template = loader.get_template('financas/doacoes_pessoa_fisica/doacoes_main.html') 
  context = {
              'ano_fiscal'        : ano_fiscal,
              'candidato'         : candidato,
              'lst_doadores'      : lst_doadores,
              
              'msg'               : msg,
              'user'              : request.user,
            }
  return HttpResponse(template.render(context, request))

#------------------------------------------------------
def lst_doacoes_doador(request, doador_id):
  
  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']
  candidato_id = request.session['candidato_id']
  request.session['doador_id'] = doador_id

  candidato = Candidato.objects.get(id=candidato_id)
  doador = Doador.objects.get(id=doador_id)
  lst_doacoes = Doacoes.objects.filter(doador = doador_id).order_by('data').order_by('tipo_doacao')

  template = loader.get_template('financas/doacoes_pessoa_fisica/doacoes_doador.html')
  context = {
              'ano_fiscal'        : ano_fiscal,
              'doador'            : doador,
              'candidato'         : candidato,
              'lst_doacoes'       : lst_doacoes,
              'msg'               : msg,
              'user'              : request.user,
            }
  
  return HttpResponse(template.render(context, request))

#------------------------------------------------------
def doacao_incluir(request, doador_id):
  
  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']
  
  doador = Doador.objects.get(id=doador_id)
  if request.POST: 
      form = Doacao_Form(request.POST)    

      if form.is_valid():
        
        doacao = form.save(commit= False)
        doacao.doador = doador
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

#------------------------------------------------------
def doacao_editar(request, doacao_id):

  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']
  candidato_id = request.session['candidato_id']  
  doador_id = request.session['doador_id']

  candidato = Candidato.objects.get(id=candidato_id)
  doador = Doador.objects.get(id=doador_id)
  doacao = Doacoes.objects.get(id = doacao_id)

  if request.method == 'POST':

    form = Doacao_Form(request.POST, instance = doacao)
    if form.is_valid():
      form.save()
      request.session['msg_status'] = 'Edição com sucesso!!!'

      return redirect('financas:lst_doacoes_doador', doador_id) 
    else:
      request.session['msg_status'] = 'Falha na edição dos dados'
      return redirect('financas:lst_doacoes_doador', doador_id) 
    
  else:

    form = Doacao_Form(instance = doacao)
    template = loader.get_template('financas/doacoes_pessoa_fisica/doacao_editar_incluir.html')
    context = {
                'ano_fiscal'  : ano_fiscal,
                'candidato'   : candidato,
                'form'        : form,
                'msg'         : msg,
                'user'        : request.user,
              }
  
    return HttpResponse(template.render(context, request))

#------------------------------------------------------
def doacao_excluir(request, doacao_id):
  
  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']
  doador_id = request.session['doador_id']

  doacao = Doacoes.objects.get(id=doacao_id)
  doacao.delete()

  request.session['msg_status'] = 'exclusão com sucesso!!!'

  return redirect('financas:lst_doacoes_doador', doador_id)  

#------------------------------------------------------
def verificar_doacoes(request):
  
  request.session['msg_status'] = chk_doacoes(request)

  return redirect('financas:doacoes_main')
  
#-------------------------------------------------------
# AutoFinanciamento
#-------------------------------------------------------
def autofinancia_main(request):
  
  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']
  candidadto_id = request.session['candidato_id']
  situacao =  request.session['alm_autofinanciamento']

  candidato = Candidato.objects.get(id=candidadto_id)
  pessoa = candidato.pessoa

  teto_gasto = Teto_gasto_cargo.objects.get(cidade=candidato.pessoa.cidade, cargo=candidato.cargo).valor

  template = loader.get_template('financas/autofinancia/autofinancia_main.html') 
  context = {
              'ano_fiscal'        : ano_fiscal,
              'candidato'         : candidato,
              'teto_gasto'        : teto_gasto,
              'situacao'          : situacao,
              'msg'               : msg,
              'user'              : request.user,
            }
  
  return HttpResponse(template.render(context, request))

#---------------------------------------------------------
def verificar_autofinanciamento(request):
  
  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']
  candidadto_id = request.session['candidato_id']

  chk_autofinancimanto(request)

  return redirect('financas:autofinancia_main')

#------------------------------------------------------
def autofinancia_lancamentos(request, candidato_id):
  
  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']
  auto_doador_id = request.session['auto_doador_id']

  candidato = Candidato.objects.get(id=candidato_id)
  auto_doador = Doador.objects.get(id=auto_doador_id)

  lst_lancamentos = Doacoes.objects.filter(doador = auto_doador ).order_by('data')

  template = loader.get_template('financas/autofinancia/autofinancia_lancamentos.html')
  context = {
                'ano_fiscal' : ano_fiscal,
                'candidato'  : candidato,
                'lst_lancamentos'       : lst_lancamentos,
                'msg'        : msg,
                'user'       : request.user,
              }
  return HttpResponse(template.render(context, request))

#------------------------------------------------------
def autofinanciameto_incluir(request, candidato_id):
  
  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']
  auto_doador_id = request.session['auto_doador_id']

  doador = Doador.objects.get(id=auto_doador_id)

  candidato = Candidato.objects.get(id=candidato_id)
  if request.POST: 
      form = Doacao_Form(request.POST)    

      if form.is_valid():
        doacao = form.save(commit=False)
        doacao.doador = doador
        doacao.save()

        request.session['msg_status'] = 'doador incluído com sucesso!'
        return redirect('financas:autofinancia_lancamentos', candidato_id)
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

#------------------------------------------------------
def autofinanciameto_editar(request, doacao_id):

  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']
  candidato_id = request.session['candidato_id']  

  candidato = Candidato.objects.get(id=candidato_id)
  doacao = Doacoes.objects.get(id=doacao_id)
  if request.method == 'POST':

    form = Doacao_Form(request.POST, instance = doacao)
    if form.is_valid():
      form.save()
      request.session['msg_status'] = 'Edição com sucesso!!!'
      return redirect('financas:autofinancia_lancamentos', candidato_id)  

    else:
      request.session['msg_status'] = 'Falha na edição dos dados'
      return redirect('financas:autofinancia_lancamentos', candidato_id)  
    
  else:

    form = Doacao_Form(instance = doacao)
    template = loader.get_template('financas/autofinancia/autofinancia_editar_incluir.html')
    context = {
                'ano_fiscal'  : ano_fiscal,
                'candidato'     : candidato,
                'form'        : form,
                'msg'         : msg,
                'user'        : request.user,
              }
  
    return HttpResponse(template.render(context, request))

#------------------------------------------------------
def autofinanciameto_excluir(request, doacao_id):
  
  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']

  candidato_id = request.session['candidato_id']  
  candidato = Candidato.objects.get(id=candidato_id)

  doacao = Doacoes.objects.get(id=doacao_id)
  doacao.delete()
  request.session['msg_status'] = 'exclusão com sucesso!!!'

  return redirect('financas:autofinancia_lancamentos', candidato_id)  

#-------------------------------------------------------
# CONTRATACAO PESSOAL
#-------------------------------------------------------
def pessoal_main(request):
  
  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']
  candidato_id = request.session['candidato_id']
  situacao =  request.session['alm_desp_pessoal']

  candidato = Candidato.objects.get(id=candidato_id)

  desp_pessoal = Despesa_pessoal.objects.get(candidato = candidato_id)

  template = loader.get_template('financas/pessoal/pessoal_main.html') 
  context = {
              'ano_fiscal'        : ano_fiscal,
              'candidato'         : candidato,
              'desp_pessoal'      : desp_pessoal,
              'situacao'          : situacao,
              'msg'               : msg,
              'user'              : request.user,
            }
  
  return HttpResponse(template.render(context, request))

#------------------------------------------------------
def desp_pessoal_situacao(request):
  
  request.session['msg_status'] = chk_despesa_pessoal(request)

  return redirect('financas:pessoal_main')

#------------------------------------------------------
def desp_pessoal_lancamentos(request, candidato_id):
  
  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']
  auto_doador_id = request.session['auto_doador_id']

  candidato = Candidato.objects.get(id=candidato_id)
  desp_pessoal = Despesa_pessoal.objects.get(candidato=candidato)

  lst_pessoas_contratada = Pessoa_contratada.objects.filter(despesa_pessoal = desp_pessoal ).order_by('data')

  template = loader.get_template('financas/pessoal/pessoal_lancamentos.html')
  context = {
                'ano_fiscal' : ano_fiscal,
                'candidato'  : candidato,
                'lst_pessoas_contratada' : lst_pessoas_contratada,
                'msg'        : msg,
                'user'       : request.user,
              }
  return HttpResponse(template.render(context, request))

#------------------------------------------------------
def desp_pessoal_incluir(request, candidato_id):
  
  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']
  auto_doador_id = request.session['auto_doador_id']

  candidato = Candidato.objects.get(id=candidato_id)
  desp_pessoal = Despesa_pessoal.objects.get(candidato=candidato)

  #pessoa_contatrada = Pessoa_contratada.objects.get(despesa_pessoal=desp_pessoal)

  if request.POST: 
      form = Pessoa_contrato_Form(request.POST)    

      if form.is_valid():
        pessoa_contatrada = form.save(commit=False)
        pessoa_contatrada.despesa_pessoal= desp_pessoal
        pessoa_contatrada.save()

        request.session['msg_status'] = 'doador incluído com sucesso!'
        return redirect('financas:desp_pessoal_lancamentos', candidato_id)
      else:
        request.session['msg_status'] = 'Falha inclusão !'
        return redirect('financas:desp_pessoal_lancamentos', candidato_id)

  else:
    
    template = loader.get_template('financas/pessoal/pessoal_editar_incluir.html')
    form = Pessoa_contrato_Form( )  

    context = {
                'ano_fiscal' : ano_fiscal,
                'candidato'  : candidato,
                'form'       : form,
                'msg'        : msg,
                'user'       : request.user,
              }
    return HttpResponse(template.render(context, request))

#------------------------------------------------------
def desp_pessoal_editar(request, doacao_id):

  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']
  candidato_id = request.session['candidato_id']  

  candidato = Candidato.objects.get(id=candidato_id)
  doacao = Doacoes.objects.get(id=doacao_id)
  if request.method == 'POST':

    form = Doacao_Form(request.POST, instance = doacao)
    if form.is_valid():
      form.save()
      request.session['msg_status'] = 'Edição com sucesso!!!'
      return redirect('financas:desp_pessoal_lancamentos', candidato_id)

    else:
      request.session['msg_status'] = 'Falha na edição dos dados'
      return redirect('financas:desp_pessoal_lancamentos', candidato_id)
    
  else:

    form = Doacao_Form(instance = doacao)
    template = loader.get_template('financas/pessoal/pessoal_editar_incluir.html')
    context = {
                'ano_fiscal'  : ano_fiscal,
                'candidato'     : candidato,
                'form'        : form,
                'msg'         : msg,
                'user'        : request.user,
              }
  
    return HttpResponse(template.render(context, request))

#------------------------------------------------------
def desp_pessoal_excluir(request, doacao_id):
  
  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']

  candidato_id = request.session['candidato_id']  
  candidato = Candidato.objects.get(id=candidato_id)

  doacao = Doacoes.objects.get(id=doacao_id)
  doacao.delete()
  request.session['msg_status'] = 'exclusão com sucesso!!!'

  return redirect('financas:desp_pessoal_lancamentos', candidato_id)

#-------------------------------------------------------
# DESPESAS
#-------------------------------------------------------
def despesas_main(request):
  
  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']
  candidato_id = request.session['candidato_id']
  situacao =  request.session['alm_desp_pessoal']

  candidato = Candidato.objects.get(id=candidato_id)

  despesas = Despesa.objects.get(candidato = candidato_id)

  template = loader.get_template('financas/despesas/despesas_main.html') 
  context = {
              'ano_fiscal'        : ano_fiscal,
              'candidato'         : candidato,
              'desp_pessoal'      : desp_pessoal,
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
  auto_doador_id = request.session['auto_doador_id']

  candidato = Candidato.objects.get(id=candidato_id)
  despesas = Despesa.objects.get(candidato=candidato)

  lst_pessoas_contratada = Pessoa_contratada.objects.filter(despesa_pessoal = desp_pessoal ).order_by('data')

  template = loader.get_template('financas/despesas/despesas_lancamentos.html')
  context = {
                'ano_fiscal' : ano_fiscal,
                'candidato'  : candidato,
                'lst_pessoas_contratada' : lst_pessoas_contratada,
                'msg'        : msg,
                'user'       : request.user,
              }
  return HttpResponse(template.render(context, request))

#------------------------------------------------------
def despesas_incluir(request, candidato_id):
  
  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']
  auto_doador_id = request.session['auto_doador_id']

  candidato = Candidato.objects.get(id=candidato_id)
  despesas = Despesa.objects.get(candidato=candidato)

  #pessoa_contatrada = Pessoa_contratada.objects.get(despesa_pessoal=desp_pessoal)

  if request.POST: 
      form = Pessoa_contrato_Form(request.POST)    

      if form.is_valid():
        pessoa_contatrada = form.save(commit=False)
        pessoa_contatrada.despesa_pessoal= desp_pessoal
        pessoa_contatrada.save()

        request.session['msg_status'] = 'doador incluído com sucesso!'
        return redirect('financas:despesas_lancamentos', candidato_id)
      else:
        request.session['msg_status'] = 'Falha inclusão !'
        return redirect('financas:despesas_lancamentos', candidato_id)

  else:
    
    template = loader.get_template('financas/despesas/despesas_editar_incluir.html')
    form = Pessoa_contrato_Form( )  

    context = {
                'ano_fiscal' : ano_fiscal,
                'candidato'  : candidato,
                'form'       : form,
                'msg'        : msg,
                'user'       : request.user,
              }
    return HttpResponse(template.render(context, request))

#------------------------------------------------------
def despesas_editar(request, doacao_id):

  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']
  candidato_id = request.session['candidato_id']  

  candidato = Candidato.objects.get(id=candidato_id)
  doacao = Doacoes.objects.get(id=doacao_id)
  if request.method == 'POST':

    form = Doacao_Form(request.POST, instance = doacao)
    if form.is_valid():
      form.save()
      request.session['msg_status'] = 'Edição com sucesso!!!'
      return redirect('financas:despesas_lancamentos', candidato_id)

    else:
      request.session['msg_status'] = 'Falha na edição dos dados'
      return redirect('financas:despesas_lancamentos', candidato_id)
    
  else:

    form = Doacao_Form(instance = doacao)
    template = loader.get_template('financas/autofinancia/autofinancia_editar_incluir.html')
    context = {
                'ano_fiscal'  : ano_fiscal,
                'candidato'     : candidato,
                'form'        : form,
                'msg'         : msg,
                'user'        : request.user,
              }
  
    return HttpResponse(template.render(context, request))

#------------------------------------------------------
def despesas_excluir(request, doacao_id):
  
  msg =  request.session['msg_status']
  ano_fiscal = request.session['ano_fiscal']

  candidato_id = request.session['candidato_id']  
  candidato = Candidato.objects.get(id=candidato_id)

  doacao = Doacoes.objects.get(id=doacao_id)
  doacao.delete()
  request.session['msg_status'] = 'exclusão com sucesso!!!'

  return redirect('financas:despesas_lancamentos', candidato_id)

#-------------------------------------------------------