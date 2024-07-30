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

ITEM_DOACAO_FINANCEIRA = 0
ITEM_DOACAO_ESTIMAVEL  = 1

# limites doacao
LIMITE_PERCENTUAL_DOACAO_SOBRE_RENDIMENTO_IRPF2024    = 10        #%
LIMITE_PERCENTUAL_AUTO_FINANCIAMENTO                  = 10        #%
LIMITE_RENDIMENTO_ISENTO                              =  30639.90 
LIMITE_DOACAO_ESTIMAVEL                               =  40000.00

#------------------------------------------------
class limites(models.Model):
  
  def __str__(self):
    return f"{self}"

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
  cidade =  models.ForeignKey(Cidade, on_delete = models.CASCADE, unique=False)
  profissão = models.CharField(null=True, max_length=255)
  dnascimento = models.DateField(null=True)
  endereco= models.CharField(max_length=255,null=True)
  cep= models.CharField(max_length=255,null=True) 
  fone= models.CharField(max_length=255,null=True) 
  email= models.CharField(max_length=255,null=True) 
  status = models.IntegerField(null=True)
  rendimento_bruto_irpf2024 = models.FloatField(null=True, default=0)
  

  def __str__(self):
    return f"{self.nome} "

#------------------------------------------------
class Cargo(models.Model):
  
  class Cargo_t(models.IntegerChoices):
      VEREADOR = ITEM_CARGO_VEREADOR, "VEREADOR"
      PREFEITOVICE = ITEM_CARGO_PREFEITO, "PREFEITO"
      VICE_PREFEITO = ITEM_CARGO_VICE_PREFEITO, "VICE-PREFEITO"

  nome =  models.CharField(max_length=50, null=False, unique=True) 
  tipo_cargo =  models.PositiveSmallIntegerField(
                    choices=Cargo_t.choices, 
                    default=Cargo_t.VEREADOR
                  )  

  def __str__(self):
    return f"{self.nome}"
  
#------------------------------------------------
class Limite_gasto_cargo(models.Model):
  
  cidade  =  models.ForeignKey(Cidade, on_delete = models.CASCADE, unique=False)
  cargo  =  models.ForeignKey(Cargo, on_delete = models.CASCADE, unique=False)
  valor =   models.FloatField(null=False, default=0)

  def __str__(self):
    return f"{self.cidade}"

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
class doacoes(models.Model):

  class doacao_t(models.IntegerChoices):
      FINANCEIRA = ITEM_DOACAO_FINANCEIRA,  "FINANCEIRA"
      ESTIMAVEL = ITEM_DOACAO_ESTIMAVEL,    "ESTIMAVEL/CESSAO"

  pessoa = models.ForeignKey(Pessoa, on_delete = models.CASCADE, unique=True)

  tipo_doacao =  models.PositiveSmallIntegerField(
                    choices=doacao_t.choices, 
                    default=doacao_t.FINANCEIRA
  )

  valor =   models.FloatField(null=False, default=0)  


  def __str__(self):
    return f"{self.valor}"
        
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
class grupo_despesa(models.Model):
  
  codigo =  models.CharField(max_length=20, null=False, unique=True) 
  descricao = models.CharField(max_length=255, null=False, default="")
  limite = models.FloatField(null=False, default=0)

  def __str__(self):
    return f"{self.codigo}"

#------------------------------------------------
class item_despesa(models.Model):
  
  grupo = models.ForeignKey(grupo_despesa, on_delete = models.CASCADE)
  codigo =  models.CharField(max_length=20, null=False, unique=True) 
  descricao = models.CharField(max_length=255, null=False, default="")

  def __str__(self):
    return f"{self.codigo} {self.descricao}"
  
#------------------------------------------------
class Despesa(models.Model):

  item  = models.ForeignKey(item_despesa, on_delete = models.CASCADE)
  valor = models.FloatField(null=False, default=0)

  def __str__(self):
    return f"{self.item.grupo.codigo} {self.item.descricao}"
  
#------------------------------------------------
class Candidato(models.Model):

  codigo = models.CharField(max_length=255, null=False, default="")
  pessoa = models.ForeignKey(Pessoa, on_delete = models.CASCADE, unique=True)
  partido = models.ForeignKey(Partido, on_delete = models.CASCADE, null=True)
  cargo  =  models.ForeignKey(Cargo, on_delete = models.CASCADE,   null=True)
  receita = models.ForeignKey(Receita, on_delete = models.CASCADE, null=True)
  despesa = models.ForeignKey(Despesa, on_delete = models.CASCADE, null=True)

  def __str__(self):
    return f"{self.codigo} {self.pessoa.nome}" 