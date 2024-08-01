from .models import *
from django.http import HttpResponse, FileResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages

#-----------------------------------------------
def chk_autofinancimanto (request):
    
    resultado = 'normal'

    autofin_atualiza_conta(request)

    candidadto_id = request.session['candidato_id']
    candidato = Candidato.objects.get(id=candidadto_id)
    
    if (candidato.total_autofin_totalizado >= candidato.val_permitido_autofinanciamento ):
        resultado = 'LIMITE UTILIZADO DE AUTOFINANCIMENTO ULTRAPASSA LIMITE PERMITIDO'
    else:
        resultado = 'Normal'

    request.session['alm_autofinanciamento'] = resultado 

    return 

#-----------------------------------------------
def autofin_atualiza_conta (request):
    
    resultado = 'normal'

    candidadto_id = request.session['candidato_id']
    doador_id = request.session['auto_doador_id']
    
    candidato = Candidato.objects.get(id=candidadto_id)   
    lst_doacoes = Doacoes.objects.filter(doador = doador_id )

    candidato.total_autofin_financeiro = 0
    candidato.total_autofin_estimavel_veiculos = 0

    # totaliza doações
    for doacao in lst_doacoes:
        if (doacao.tipo_doacao == TIPO_DOACAO_FINANCEIRA):
            candidato.total_autofin_financeiro += doacao.valor

        elif (doacao.tipo_doacao == TIPO_DOACAO_ESTIMAVEL_BENS):
            candidato.total_autofin_estimavel_bens += doacao.valor 

        elif (doacao.tipo_doacao == TIPO_DOACAO_ESTIMAVEL_VEICULOS):
            candidato.total_autofin_estimavel_veiculos += doacao.valor 

        candidato.total_autofin_totalizado = candidato.total_autofin_financeiro + \
                                                candidato.total_autofin_estimavel_bens + \
                                                candidato.total_autofin_estimavel_veiculos

    # Atualiza conta candidato
    candidato.save()

    return 


#-----------------------------------------------
# Totaliza as doações e salva na tabela doador
def chk_doacoes (request):

    mensagem = 'Sucesso na verifiação das doações'

    candidadto_id = request.session['candidato_id']
    auto_doador_id = request.session['auto_doador_id']
    
    candidato = Candidato.objects.get(id=candidadto_id)   
    lst_doadores =  Doador.objects.filter(candidato = candidato).exclude(id=auto_doador_id)
        
    try:
        for doador in lst_doadores:
            
            doador.total_doacao_financeira = 0
            doador.total_doacao_estimavel  = 0

            lst_doacoes = Doacoes.objects.filter(doador = doador)

            for doacao in lst_doacoes:

                if(doacao.tipo_doacao == TIPO_DOACAO_FINANCEIRA):
                        doador.total_doacao_financeira += doacao.valor
                else:
                    doador.total_doacao_estimavel += doacao.valor 

                doador.total_doacao_totalizado = doador.total_doacao_financeira + doador.total_doacao_estimavel 

            #---------------------------------------------------------------    
            if (doador.total_doacao_totalizado >= doador.val_limite_total ):
                situacao = 'TOTAL DOACAO ULTRAPASSA LIMITE PERMITIDO'
            else:
                situacao = 'Normal'

            doador.situacao = situacao
            # save
            doador.save()
    except:
         mensagem ='FALHA TOTALIZAÇÃO'

    return mensagem

#-----------------------------------------------
def chk_despesa_pessoal (request):
    
    resultado = 'normal'

    candidadto_id = request.session['candidato_id']
    candidato = Candidato.objects.get(id=candidadto_id)
    
    despesa_pessoal = Despesa_pessoal.objects.get(candidato=candidato) 
    lst_Pessoas = Pessoa_contratada.objects.filter(despesa_pessoal = despesa_pessoal)

    despesa_pessoal.total_valor_contratado = 0
    despesa_pessoal.total_valor_cessao = 0
    despesa_pessoal.total = 0
    despesa_pessoal.qte_pessoal = 0
    for pessoa in lst_Pessoas:

        despesa_pessoal.total_valor_contratado += pessoa.valor_contratado
        despesa_pessoal.total_valor_cessao += pessoa.valor_cessao
        despesa_pessoal.total = despesa_pessoal.total_valor_contratado + despesa_pessoal.total_valor_cessao
        despesa_pessoal.qte_pessoal += 1 

    limite_pessoal = 0
    if (candidato.cargo.tipo_cargo == ITEM_CARGO_VEREADOR ):
        limite_pessoal = LIMITE_PESSOAL_VEREADOR
    elif (candidato.cargo.tipo_cargo == ITEM_CARGO_PREFEITO ):      
        limite_pessoal = LIMITE_PESSOAL_PREFEITO

    if (despesa_pessoal.qte_pessoal > limite_pessoal):
        despesa_pessoal.situacao = 'ULTRAPASSA LIMITE DE PESSOAL PARA O CARGO'
        resultado = 'ULTRAPASSA LIMITE DE PESSOAL PARA O CARGO'
    else:
        despesa_pessoal.situacao = 'Normal' 
    
    despesa_pessoal.save()
    return resultado


