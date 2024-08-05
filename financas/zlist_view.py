from django.db import models
from django.views.generic import ListView

from .models import *
from .geral import *
from .forms import *

class MovieListView(ListView):
    model = Receitas