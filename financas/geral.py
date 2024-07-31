from .models import *


#-----------------------------------------------
def chk_autofinancimanto (candidato):
    report = 'normal'

    if (candidato.total_autofin_totalizado >= candidato.val_permitido_autofinanciamento ):
        report = 'LIMITE UTILIZADO DE AUTOFINANCIMENTO ULTRAPASSA LIMITE PERMITIDO'
    else:
        report = 'Normal'

    return report

#-----------------------------------------------
# Totaliza as doações e salva na tabela doador
def totaliza_doacoes (doador_id):

    mensagem = 'NAO ENTROU'

    doador = Doador.objects.get(id = doador_id)
    doador.total_doacao_financeira = 0
    doador.total_doacao_estimavel  = 0

    lst_doacoes = Doacoes.objects.all()

    try:
        for doacao in lst_doacoes:


            if(doacao.tipo_doacao == TIPO_DOACAO_FINANCEIRA):
                doador.total_doacao_financeira += doacao.valor
            else:
                doador.total_doacao_estimavel += doacao.valor 

            doador.total_doacao_totalizado = doador.total_doacao_financeira + doador.total_doacao_estimavel 

            #---------------------------------------------------------------    
            if (doador.total_doacao_totalizado >= doador.val_limite_total ):
                mensagem = 'TOTAL DOACAO ULTRAPASSA LIMITE PERMITIDO'
            else:
                mensagem = 'Normal'

            doador.situacao = mensagem
            # save
            doador.save()
    except:
       mensagem ='FALHA TOTALIZAÇÃO'

    return mensagem