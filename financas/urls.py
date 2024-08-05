from django.contrib import admin
from django.urls import include, path, re_path
from django.contrib.auth import views as auth_views

from . import views, views_cadastro, views_despesas, views_receitas

from .views_receitas import *

app_name='financas'

urlpatterns = [
    path('', views.index, name='index'),
    path('main/', views.index, name='index'),

  
  # menu
    path('config_main/<int:candidato_id>/', views.config_main, name='config_main'),

  #---------------------------------------------------------------------------------------
  # VIEWS_CADASTRO
  #---------------------------------------------------------------------------------------
    path('cadastro_main/', views_cadastro.cadastro_main, name='cadastro_main'),
    # cadastro cidade
    path('cadastro_cidade/', views_cadastro.cadastro_cidade, name='cadastro_cidade'),
    path('cidade_incluir/', views_cadastro.cidade_incluir, name='cidade_incluir'),
    path('cidade_editar/<int:cidade_id>/', views_cadastro.cidade_editar, name='cidade_editar'),
    path('cidade_excluir/<int:cidade_id>/', views_cadastro.cidade_excluir, name='cidade_excluir'),

    # cadastro pessoa
    path('cadastro_pessoa/', views_cadastro.cadastro_pessoa, name='cadastro_pessoa'),
    path('pessoa_incluir/', views_cadastro.pessoa_incluir, name='pessoa_incluir'),
    path('pessoa_editar/<int:pessoa_id>/', views_cadastro.pessoa_editar, name='pessoa_editar'),
    path('pessoa_excluir/<int:pessoa_id>/', views_cadastro.pessoa_excluir, name='pessoa_excluir'),

    # cadastro partido
    path('cadastro_partido/', views_cadastro.cadastro_partido, name='cadastro_partido'),
    path('partido_incluir/', views_cadastro.partido_incluir, name='partido_incluir'),
    path('partido_editar/<int:partido_id>/', views_cadastro.partido_editar, name='partido_editar'),
    path('partido_excluir/<int:partido_id>/', views_cadastro.partido_excluir, name='partido_excluir'),

    # cadastro cargo
    path('cadastro_cargo/', views_cadastro.cadastro_cargo, name='cadastro_cargo'),
    path('cargo_incluir/', views_cadastro.cargo_incluir, name='cargo_incluir'),
    path('cargo_editar/<int:cargo_id>/', views_cadastro.cargo_editar, name='cargo_editar'),
    path('cargo_excluir/<int:cargo_id>/', views_cadastro.cargo_excluir, name='cargo_excluir'),

   # cadastro candidato
    path('cadastro_candidato/', views_cadastro.cadastro_candidato, name='cadastro_candidato'),
    path('candidato_incluir/', views_cadastro.candidato_incluir, name='candidato_incluir'),
    path('candidato_editar/<int:candidato_id>/', views_cadastro.candidato_editar, name='candidato_editar'),
    path('candidato_excluir/<int:candidato_id>/', views_cadastro.candidato_excluir, name='candidato_excluir'),

  # cadastro grupo despesas
    path('cadastro_grupo_despesas/', views_cadastro.cadastro_grupo_despesas, name='cadastro_grupo_despesas'),
    path('grupo_despesas_incluir/', views_cadastro.grupo_despesas_incluir, name='grupo_despesas_incluir'),
    path('grupo_despesas_editar/<int:grupo_despesas_id>/', views_cadastro.grupo_despesas_editar, name='grupo_despesas_editar'),
    path('grupo_despesas_excluir/<int:grupo_despesas_id>/', views_cadastro.grupo_despesas_excluir, name='grupo_despesas_excluir'),

  # cadastro doador
    path('doador_incluir/', views_cadastro.doador_incluir, name='doador_incluir'),
    path('doador_editar/<int:doador_id>/', views_cadastro.doador_editar, name='doador_editar'),
    path('doador_excluir/<int:doador_id>/', views_cadastro.doador_excluir, name='doador_excluir'),

  # cadastro TETO DE GASTOS
    path('teto_gatos_main/', views_cadastro.teto_gatos_main, name='teto_gatos_main'),
    path('tgastos_incluir/', views_cadastro.tgastos_incluir, name='tgastos_incluir'),
    path('tgastos_editar/<int:tgastos_id>/', views_cadastro.tgastos_editar, name='tgastos_editar'),
    path('tgastos_excluir/<int:tgastos_id>/', views_cadastro.tgastos_excluir, name='tgastos_excluir'),

  # Menu RECEITAS
    path("cadastro_receitas_main_TableView/", views_cadastro.cadastro_receitas_main_TableView.as_view(), name='cadastro_receitas_main_TableView'),
    path('grupo_receitas_incluir/', views_cadastro.grupo_receitas_incluir, name='grupo_receitas_incluir'),
    path('grupo_receitas_editar/<int:grupo_receitas_id>/', views_cadastro.grupo_receitas_editar, name='grupo_receitas_editar'),
    path('grupo_receitas_excluir/<int:grupo_receitas_id>/', views_cadastro.grupo_receitas_excluir, name='grupo_receitas_excluir'),

  #---------------------------------------------------------------------------------------
  # VIEWS
  #---------------------------------------------------------------------------------------

  # Menu doacoes
    path('doacoes_main/', views.doacoes_main, name='doacoes_main'),
    path('lst_doacoes_doador/<int:doador_id>', views.lst_doacoes_doador, name='lst_doacoes_doador'),    
    path('doacao_incluir/<int:doador_id>/', views.doacao_incluir, name='doacao_incluir'),
    path('doacao_editar/<int:doacao_id>/', views.doacao_editar, name='doacao_editar'),
    path('doacao_excluir/<int:doacao_id>/', views.doacao_excluir, name='doacao_excluir'),
    path('verificar_doacoes/', views.verificar_doacoes, name='verificar_doacoes'),

  # Menu autofinacimento
    path('autofinancia_main/', views.autofinancia_main, name='autofinancia_main'),
    path('lst_doacoes_doador/<int:doador_id>', views.lst_doacoes_doador, name='lst_doacoes_doador'),    
    path('verificar_autofinanciamento/', views.verificar_autofinanciamento, name='verificar_autofinanciamento'),

    path('autofinancia_lancamentos/<int:candidato_id>/', views.autofinancia_lancamentos, name='autofinancia_lancamentos'),
    path('autofinanciameto_incluir/<int:candidato_id>/', views.autofinanciameto_incluir, name='autofinanciameto_incluir'),
    path('autofinanciameto_editar/<int:doacao_id>/', views.autofinanciameto_editar, name='autofinanciameto_editar'),
    path('autofinanciameto_excluir/<int:doacao_id>/', views.autofinanciameto_excluir, name='autofinanciameto_excluir'),

  # Menu gestao pessoal 
    path('pessoal_main/', views.pessoal_main, name='pessoal_main'),
    path('desp_pessoal_situacao/', views.desp_pessoal_situacao, name='desp_pessoal_situacao'),
    path('desp_pessoal_lancamentos/<int:candidato_id>/', views.desp_pessoal_lancamentos, name='desp_pessoal_lancamentos'),

    path('desp_pessoal_incluir/<int:candidato_id>/', views.desp_pessoal_incluir, name='desp_pessoal_incluir'),
    path('desp_pessoal_editar/<int:doacao_id>/', views.desp_pessoal_editar, name='desp_pessoal_editar'),
    path('desp_pessoal_excluir/<int:doacao_id>/', views.desp_pessoal_excluir, name='desp_pessoal_excluir'),

  #---------------------------------------------------------------------------------------
  # VIEWS_DESPESAS
  #---------------------------------------------------------------------------------------
    path('despesas_main/', views_despesas.despesas_main, name='despesas_main'),
    path('despesas_situacao/', views_despesas.despesas_situacao, name='despesas_situacao'),
    path('despesas_lancamentos/<int:candidato_id>/', views_despesas.despesas_lancamentos, name='despesas_lancamentos'),

    path('despesas_incluir/<int:candidato_id>/', views_despesas.despesas_incluir, name='despesas_incluir'),
    path('despesas_editar/<int:despesa_id>/', views_despesas.despesas_editar, name='despesas_editar'),
    path('despesas_excluir/<int:despesa_id>/', views_despesas.despesas_excluir, name='despesas_excluir'),
    path('despesa_atualiza_resumo/', views_despesas.despesa_atualiza_resumo, name='despesa_atualiza_resumo'),
    path('grupo_despesa_editar/<int:grupo_id>/', views_despesas.grupo_despesa_editar, name='grupo_despesa_editar'),

   #---------------------------------------------------------------------------------------
  # VIEWS_RECEITAS
  #---------------------------------------------------------------------------------------   

  # Menu receitas
    path('receitas_main/', views_receitas.receitas_main, name='receitas_main'),
    path('receitas_atualiza_resumo/', views_receitas.receitas_atualiza_resumo, name='receitas_atualiza_resumo'),
    path('receitas_editar/<int:receita_id>/', views_receitas.receitas_editar, name='receitas_editar'),
    path("Receitas_main_TableView/", Receitas_main_TableView.as_view(), name='Receitas_main_TableView'),
]
 