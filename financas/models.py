from django.db import models
import datetime

app_name = 'milenio'

#--------------------------------------------------------------
# DEFINIÇÕES
#--------------------------------------------------------------
# Tipo do cargo
ITEM_CARGO_VEREADOR = 1
ITEM_CARGO_PREFEITO = 2 
ITEM_CARGO_VICE_PREFEITO = 3 

#------------------------------------------------
class Cidade(models.Model):

  nome =  models.CharField(max_length=20, null=False, unique=True)
  estado =  models.CharField(max_length=20, null=False, unique= False)

  def __str__(self):
    return f"{self.nome}"
  
#------------------------------------------------
class Pessoa(models.Model):
  cpf= models.CharField(max_length=255,null=False, unique=True)
  nome = models.CharField(max_length=255,null=False)
  cidade =  models.ForeignKey(Cidade, on_delete = models.CASCADE, unique=False)
  profissão = models.CharField(null=True, max_length=255)
  dnascimento = models.DateField(null=True)
  endereco= models.CharField(max_length=255,null=True)
  cep= models.CharField(max_length=255,null=True) 
  cidade= models.CharField(max_length=255,null=True) 
  fone= models.CharField(max_length=255,null=True) 
  email= models.CharField(max_length=255,null=True) 
  status = models.IntegerField(null=True)

  def __str__(self):
    return f"{self.name}"

#------------------------------------------------
class Cargo(models.Model):
  
  class Cargo_t(models.IntegerChoices):
      VEREADOR = ITEM_CARGO_VEREADOR, "VEREADOR"
      PREFEITOVICE = ITEM_CARGO_PREFEITO, "PREFEITO"
      VICE_PREFEITO = ITEM_CARGO_VICE_PREFEITO, "VICE-PREFEITO"

  codigo =  models.CharField(max_length=20, null=False, unique=True) 
  descricao = models.CharField(max_length=255, null=False, default="")
  tipo_cargo =  models.PositiveSmallIntegerField(
                    choices=Cargo_t.choices, 
                    default=Cargo_t.VEREADOR
                  )  

  def __str__(self):
    return f"{self.codigo}"
  
#------------------------------------------------
class Limite_gasto_cargo(models.Model):
  
  cidade  =  models.ForeignKey(Cidade, on_delete = models.CASCADE, unique=False)
  cargo  =  models.ForeignKey(Cargo, on_delete = models.CASCADE, unique=False)
  valor =   models.FloatField(null=False, default=0)

  def __str__(self):
    return f"{self.cidade}"

#------------------------------------------------
class Candidato(models.Model):

  pessoa = models.ForeignKey(Pessoa, on_delete = models.CASCADE, unique=False)
  cargo  =  models.ForeignKey(Cargo, on_delete = models.CASCADE, unique=False)

  def __str__(self):
    return f"{self.cargo}"
  

#------------------------------------------------
class Receita_estimavel(models.Model):

  candidato = models.ForeignKey(Candidato, on_delete = models.CASCADE, unique=True)
Recursos próprios
Recursos de pessoas físicas
Recursos de outros candidatos
- Fundo Especial de Financiamento de Campanha(FEFC)
- Fundo Partidário
- Outros Recursos
Recursos de partido político
- Fundo Especial de Financiamento de Campanha(FEFC)
- Outros Recursos
Doações pela Internet
Outras receitas
- Comercialização de bens ou realização de eventos
Comercialização de Bens com FEFC
Comercialização de Bem com FP
Comercialização de Bem com OR
- Rendimentos de aplicações financeiras
Fundo Especial de Financiamento de Campanha(FEFC)
- Recursos de origens não identificadas
Recursos de Financiamento Coletivo
Devolução de Receita
 Devolução de Recursos de Origens não Identificadas
  total =   models.FloatField(null=False, default=0)

  def __str__(self):
    return f"{self.candidato}"


#------------------------------------------------
class Receita(models.Model):

  rec_estimavel = models.ForeignKey(Receita_estimavel, on_delete = models.CASCADE, unique=True)



  def __str__(self):
    return f"{self.candidato}"
  
  