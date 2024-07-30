from django.contrib import admin
from django.urls import include, path, re_path
from django.contrib.auth import views as auth_views
from . import views
from . import views_cadastro_candidato
from . import views_cadastro_cidade
app_name='financas'

urlpatterns = [
    path('', views.index, name='index'),
    path('main/', views.index, name='index'),

    # cadastro 
    path('cadastro_main/', views_cadastro_candidato.cadastro_main, name='cadastro_main'),

    # cadastro candidato
    path('cadastro_candidato/', views_cadastro_candidato.cadastro_candidato, name='cadastro_candidato'),
    path('candidato_incluir/', views_cadastro_candidato.candidato_incluir, name='candidato_incluir'),
    path('candidato_editar/', views_cadastro_candidato.candidato_editar, name='candidato_editar'),
    path('candidato_excluir/', views_cadastro_candidato.candidato_excluir, name='candidato_excluir'),

    # cadastro cidade
    path('cadastro_cidade/', views_cadastro_cidade.cadastro_cidade, name='cadastro_cidade'),
    path('cidade_incluir/', views_cadastro_cidade.cidade_incluir, name='cidade_incluir'),
    path('cidade_editar/<int:cidade_id>/', views_cadastro_cidade.cidade_editar, name='cidade_editar'),
    path('cidade_excluir/<int:cidade_id>/', views_cadastro_cidade.cidade_excluir, name='cidade_excluir'),

]
 