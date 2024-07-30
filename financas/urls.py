from django.contrib import admin
from django.urls import include, path, re_path
from django.contrib.auth import views as auth_views
from . import views
from . import views_cadastro
app_name='financas'

urlpatterns = [
    path('', views.index, name='index'),
    path('main/', views.index, name='index'),

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
]
 