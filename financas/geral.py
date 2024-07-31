


#-----------------------------------------------
def chk_autofinancimanto (candidato):
    report = 'normal'

    if (candidato.total_autofin_totalizado >= candidato.val_permitido_autofinanciamento ):
        report = 'LIMITE UTILIZADO DE AUTOFINANCIMENTO ULTRAPASSA LIMITE PERMITIDO'
    else:
        report = 'Normal'

    return report