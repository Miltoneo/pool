from django_tables2 import tables, Table, Column, LinkColumn
from django_tables2.utils import A
from django.db import models
from django.views.generic import ListView

from .models import *
from .geral import *
from .forms import *

#-----------------------------------
class ReceitasTable(tables.Table):

    edit = LinkColumn('financas:receitas_main', text='Edit', orderable=False, empty_values=())
    excluir = LinkColumn('financas:receitas_main', text='Excluir',orderable=False, empty_values=())
    #edit = tables.LinkColumn('item_edit', text='Edit', args=[A('pk')], orderable=False, empty_values=())

    class Meta:
        model = Grupo_receitas
        template_name = "django_tables2/bootstrap.html"
        #fields = ("codigo", "descricao", "total_financeiro", "total_estimavel", "total",)
        orderable = True
        sequence = ("edit", "excluir", )
        #exclude = ("user", )

#-----------------------------------
class Receita_Candidato_Table(tables.Table):

    lancamentos = LinkColumn('financas:receitas_editar', text='Atualizar', args=[A('pk')],orderable=False, empty_values=())

    class Meta:
        model = Receita_Candidato
        template_name = "django_tables2/bootstrap.html"
        orderable = True
        sequence = ("lancamentos", )

#-----------------------------------
class Cad_Receitas_Table(tables.Table):

    edit = LinkColumn('financas:grupo_receitas_editar', text='Edit', args=[A('pk')],orderable=False, empty_values=())
    excluir = LinkColumn('financas:grupo_receitas_excluir', text='Excluir',args=[A('pk')],orderable=False, empty_values=())

    class Meta:
        model = Grupo_receitas
        template_name = "django_tables2/bootstrap.html"
        orderable = True
        sequence = ("edit", "excluir", )

#-------------------------------------
# exemplo
class ReceitasTable2(Table):
    codigo = Column(
        accessor='codigo',
        verbose_name='Código1')

    descricao = Column(
        accessor='descricao',
        verbose_name='Descricao1')

    class Meta:
        attrs = {"class": "table is-bordered"}