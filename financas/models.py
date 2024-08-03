from django.db import models
import datetime

app_name = 'financas'

#--------------------------------------------------------------
# DEFINIÇÕES
#--------------------------------------------------------------

# Tipo do cargo
ITEM_CARGO_VEREADOR       = 1
ITEM_CARGO_PREFEITO       = 2 
ITEM_CARGO_VICE_PREFEITO  = 3 

# limites doacao
LIMITE_PERCENTUAL_DOACAO_SOBRE_RENDIMENTO_IRPF2024    = 10        #%
LIMITE_PERCENTUAL_AUTO_FINANCIAMENTO                  = 10        #%
LIMITE_RENDIMENTO_ISENTO                              =  30639.00
LIMITE_DOACAO_ESTIMAVEL                               =  40000.00
LIMITE_PERCENT_ALIMENTACAO                            = 10        #% = 10% *(total_contratado - (D2.1) - (D2.4) - (D2.43) - (fiscais??))
LIMITE_PERCENT_LOC_VEICULOS                           = 20        #% = 20% *(total_contratodo)

#limite pessoal
LIMITE_PESSOAL_VEREADOR =  225
LIMITE_PESSOAL_PREFEITO =  450 

# Tipo de doacao
TIPO_DOACAO_FINANCEIRA = 0
TIPO_DOACAO_ESTIMAVEL_VEICULOS = 1
TIPO_DOACAO_ESTIMAVEL_BENS = 3

# Tipo CONTABIL PESSOAL
PESSOAL_CONTABIL_CONTRATO = 0
PESSOAL_CONTABIL_CESSAO = 1

# REGRAS 
GRUPO_CONTRATACAO_PESSOAL = 'D2.1'
GRUPO_ALIMENTACAO = 'D2.16'
GRUPO_CONTRATACAO_S_ADVOCATICIOS = 'D2.42'
GRUPO_CONTRATACAO_S_CONTABEIS = 'D2.43'
GRUPO_LOC_VEICULOS = 'D2.33'
#------------------------------------------------
class limites(models.Model):
  
  def __str__(self):
    return f"{self}"

#------------------------------------------------
class Grupo_despesa(models.Model):
  
  codigo =  models.CharField(max_length=20, null=False, unique=True) 
  descricao = models.CharField(max_length=255, null=False, default="")

  total_contratado = models.FloatField(null=False, default=0) 
  total_estimavel = models.FloatField(null=False, default=0) 
  total_pago_FEFC = models.FloatField(null=False, default=0) 
  total_pago_fundo_partidario = models.FloatField(null=False, default=0) 
  total_pago_outros_rec = models.FloatField(null=False, default=0) 
  total_nao_pago  = models.FloatField(null=False, default=0) 
  limite_gastos  = models.FloatField(null=False, default=0) 

  def __str__(self):
    return f"{self.codigo} {self.descricao}"
  
#------------------------------------------------
class Cidade(models.Model):

  nome =  models.CharField(max_length=20, null=False, unique=True)
  estado =  models.CharField(max_length=20, null=False, unique= False)

  def __str__(self):
    return f"{self.nome}-{self.estado}"
  
#------------------------------------------------
class Pessoa(models.Model):
  cpf= models.CharField(max_length=255,null=False, unique=True)
  nome = models.CharField(max_length=255,null=False)
  cidade =  models.ForeignKey(Cidade, on_delete = models.CASCADE, null=False )
  profissao = models.CharField( max_length=255,null=True)
  dnascimento = models.DateField(null=True)
  endereco= models.CharField(max_length=255,null=True)
  cep= models.CharField(max_length=255,null=True) 
  fone= models.CharField(max_length=255,null=True) 
  email= models.CharField(max_length=255,null=True) 
  rendimento_bruto_irpf2024 = models.FloatField(null=False, default=0)
  
  def __str__(self):
    return f"{self.nome} "

#------------------------------------------------
class Cargo(models.Model):
  
  class Cargo_t(models.IntegerChoices):
      VEREADOR = ITEM_CARGO_VEREADOR, "VEREADOR"
      PREFEITO = ITEM_CARGO_PREFEITO, "PREFEITO"
      VICE_PREFEITO = ITEM_CARGO_VICE_PREFEITO, "VICE-PREFEITO"

  nome =  models.CharField(max_length=50, null=False, unique=True) 
  tipo_cargo =  models.PositiveSmallIntegerField(
                    choices=Cargo_t.choices, 
                    default=Cargo_t.VEREADOR
                  )  

  def __str__(self):
    return f"{self.nome}"
  
#------------------------------------------------
class Teto_gasto_cargo(models.Model):
  
  cidade =  models.ForeignKey(Cidade, on_delete = models.CASCADE, unique=False)
  cargo  =  models.ForeignKey(Cargo, on_delete = models.CASCADE, unique=False)
  valor  =   models.FloatField(null=False, default=0)

  def __str__(self):
    return f"{self.cidade} {self.cargo.nome}"

#------------------------------------------------
class Partido(models.Model):

  sigla =  models.CharField(max_length=20, null=False, unique=True)
  nome =  models.CharField(max_length=250, null=False, unique= False)

  def __str__(self):
    return f"{self.sigla}"

#------------------------------------------------
class Rec_outros_candidatos(models.Model):

  FEFC =   models.FloatField(null=False, default=0)
  fundo_partidario =   models.FloatField(null=False, default=0)
  outros =   models.FloatField(null=False, default=0)


  def __str__(self):
    return f"{self.id}"
  
#------------------------------------------------
class Rec_partido_politico(models.Model):

  FEFC =   models.FloatField(null=False, default=0)
  outros =   models.FloatField(null=False, default=0)
  doacoes_internet =   models.FloatField(null=False, default=0)

  def __str__(self):
    return f"{self.id}"

#------------------------------------------------
class Comerc_bens_realiz_eventos(models.Model):

  com_bens_FEFC =   models.FloatField(null=False, default=0)
  com_bens_FP =   models.FloatField(null=False, default=0)
  com_bens_OR =   models.FloatField(null=False, default=0)

  def __str__(self):
    return f"{self.id}"

#------------------------------------------------
class Rend_aplic_financeiras(models.Model):

  FEFC  = models.FloatField(null=False, default=0)
  fundo_partidario= models.FloatField(null=False, default=0)
  outros = models.FloatField(null=False, default=0)

  def __str__(self):
    return f"{self.id}"


#------------------------------------------------
class Rec_outras_receitas(models.Model):

  comerc_bens_realiz_eventos  =  models.ForeignKey(Comerc_bens_realiz_eventos, on_delete = models.CASCADE, unique=False)
  rend_aplic_financeiras  =  models.ForeignKey(Rend_aplic_financeiras, on_delete = models.CASCADE, unique=False)
  #- Recursos de origens não identificadas
  rec_ori_nao_identificada = models.FloatField(null=False, default=0)

  def __str__(self):
    return f"{self.id}"

       
#------------------------------------------------
class Receita_estimavel(models.Model):

  #autofinanciamento
  rec_proprios =   models.FloatField(null=False, default=0)
  #doações
  rec_pessoas_fisicas =   models.FloatField(null=False, default=0)

  rec_outros_candidatos = models.ForeignKey(Rec_outros_candidatos, on_delete = models.CASCADE, unique=False)
  rec_partido_politico = models.ForeignKey(Rec_partido_politico, on_delete = models.CASCADE, unique=False)
  rec_outras_receitas = models.ForeignKey(Rec_outras_receitas, on_delete = models.CASCADE, unique=False)
  
  aquisicao_doacao_bens_moveis_imoveis   =   models.FloatField(null=False, default=0)
  rec_financiamento_coletivo  =   models.FloatField(null=False, default=0)
  devolucao_receitas =   models.FloatField(null=False, default=0)
  devolucao_rec_orig_nao_identificadoas  =   models.FloatField(null=False, default=0)

  total =   models.FloatField(null=False, default=0)

  def __str__(self):
    return f"{self.total}"

#------------------------------------------------
class Receita_financeiro(models.Model):

  #autofinanciamento
  rec_proprios =   models.FloatField(null=False, default=0)
  #doações
  rec_pessoas_fisicas =   models.FloatField(null=False, default=0)

  rec_outros_candidatos = models.ForeignKey(Rec_outros_candidatos, on_delete = models.CASCADE, unique=False)
  rec_partido_politico = models.ForeignKey(Rec_partido_politico, on_delete = models.CASCADE, unique=False)
  rec_outras_receitas = models.ForeignKey(Rec_outras_receitas, on_delete = models.CASCADE, unique=False)
  
  aquisicao_doacao_bens_moveis_imoveis   =   models.FloatField(null=False, default=0)
  rec_financiamento_coletivo  =   models.FloatField(null=False, default=0)
  devolucao_receitas =   models.FloatField(null=False, default=0)
  devolucao_rec_orig_nao_identificadoas  =   models.FloatField(null=False, default=0)

  total =   models.FloatField(null=False, default=0)

  def __str__(self):
    return f"{self.total}"
  
#------------------------------------------------
class Receita(models.Model):
  
  rec_estimavel = models.ForeignKey(Receita_estimavel, on_delete = models.CASCADE, unique=True)
  rec_financeira = models.ForeignKey(Receita_financeiro, on_delete = models.CASCADE, unique=True)
  total =   models.FloatField(null=False, default=0)
  def __str__(self):
    return f"{self.total}"

#------------------------------------------------
class Candidato(models.Model):

  codigo = models.CharField(max_length=255, null=False, default="")
  pessoa = models.ForeignKey(Pessoa, on_delete = models.CASCADE, unique=True)
  partido = models.ForeignKey(Partido, on_delete = models.CASCADE, null=True)
  cargo  =  models.ForeignKey(Cargo, on_delete = models.CASCADE,   null=True)

  val_percent_permitido_autofinanciamento = models.FloatField(null=False, default=0) # sobre o teto de gasto para o cargo
  val_permitido_autofinanciamento       = models.FloatField(null=False, default=0)   # val_percent * teto de gasto
  total_autofin_financeiro = models.FloatField(null=False, default=0) 
  total_autofin_estimavel_bens = models.FloatField(null=False, default=0) 
  total_autofin_estimavel_veiculos = models.FloatField(null=False, default=0) 
  total_autofin_totalizado=  models.FloatField(null=False, default=0) 

  def __str__(self):
    return f"{self.codigo} {self.pessoa.nome}" 

#------------------------------------------------
class Doador(models.Model):

  pessoa = models.ForeignKey(Pessoa, on_delete = models.CASCADE, null=False)
  candidato = models.ForeignKey(Candidato, on_delete = models.CASCADE, null=False)

  val_limite_doacao_financeira = models.FloatField(null=False, default=0) 
  val_limite_doacao_estimavel = models.FloatField(null=False, default=0) 
  val_limite_total  = models.FloatField(null=False, default=0) 
  total_doacao_financeira = models.FloatField(null=False, default=0) 
  total_doacao_estimavel = models.FloatField(null=False, default=0) 
  total_doacao_totalizado=  models.FloatField(null=False, default=0) 
  situacao = models.CharField(max_length=255,null=False,  default='Normal')

  def __str__(self):
    return f"{self.pessoa.cpf} {self.pessoa.nome}" 
  
#------------------------------------------------
class Doacoes(models.Model):

  class tipo_t(models.IntegerChoices):
      FINANCEIRO          = TIPO_DOACAO_FINANCEIRA, "FINANCEIRO"
      ESTIMAVEL_VEICULOS  = TIPO_DOACAO_ESTIMAVEL_VEICULOS,  "CESSÃO DE VEICULOS "
      ESTIMAVEL_BENS      = TIPO_DOACAO_ESTIMAVEL_BENS,  "CESSÃO DE BENS "

  doador = models.ForeignKey(Doador, on_delete = models.CASCADE, null=True)
  data = models.DateField(null=True)
  valor = models.FloatField(null=False, default=0) 
  tipo_doacao=  models.PositiveSmallIntegerField(
                    choices=tipo_t.choices, 
                    default=tipo_t.FINANCEIRO
                      )

  def __str__(self):
    return f"{self.tipo_doacao}" 

#------------------------------------------------
class Despesa_pessoal(models.Model):

  candidato = models.ForeignKey(Candidato, on_delete = models.CASCADE, null=False)
  qte_pessoal =  models.IntegerField(null=False, default=0) 
  total_valor_contratado = models.FloatField(null=False, default=0) 
  total_valor_cessao = models.FloatField(null=False, default=0) 
  total = models.FloatField(null=False, default=0)  
  situacao = models.CharField(max_length=255,  default='Normal', null=False)

  def __str__(self):
    return f"{self.candidato}" 

#------------------------------------------------
class Pessoa_contratada(models.Model):

  class tipo_t(models.IntegerChoices):
      CONTRATO  = PESSOAL_CONTABIL_CONTRATO, "CONTRATO"
      CESSAO      = PESSOAL_CONTABIL_CESSAO,   "CESSÃO "


  despesa_pessoal = models.ForeignKey(Despesa_pessoal, on_delete = models.CASCADE, null=False)
  data = models.DateField(null=False)
  nome = models.CharField(max_length=255,  default='-', null=False)
  funcao = models.CharField(max_length=255,  default='-', null=False)
  grupo_despesa = models.ForeignKey(Grupo_despesa, on_delete = models.CASCADE, null=False)

  tipo_contabil=  models.PositiveSmallIntegerField(
                      choices=tipo_t.choices, 
                      default=tipo_t.CONTRATO
                      )
  valor_contratado = models.FloatField(null=False, default=0) 
  valor_cessao = models.FloatField(null=False, default=0) 
  valor_total = models.FloatField(null=False, default=0)  

  def __str__(self):
    return f"{self.nome}" 
  

#------------------------------------------------
class Despesas(models.Model):

  data = models.DateField(null=False)
  candidato = models.ForeignKey(Candidato, on_delete = models.CASCADE, null=False)
  grupo = models.ForeignKey(Grupo_despesa, on_delete = models.CASCADE)
  valor_contratado = models.FloatField(null=False, default=0) 
  valor_estimavel = models.FloatField(null=False, default=0) 
  valor_pago_FEFC = models.FloatField(null=False, default=0) 
  valor_pago_fundo_partidario = models.FloatField(null=False, default=0) 
  valor_pago_outros_rec = models.FloatField(null=False, default=0) 
  valor_nao_pago  = models.FloatField(null=False, default=0) 
  limite_gastos  = models.FloatField(null=False, default=0) 

  def __str__(self):
    return f"{self.candidato}"
  
