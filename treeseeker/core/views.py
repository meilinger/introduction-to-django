from django.shortcuts import render
from django.views.generic import ListView, DetailView
from core.models import TreeSpecies, TreeSample

# Create your views here.

class TreeSpeciesList(ListView):
    model = TreeSpecies
    template_name = 'index.html'

class TreeSampleDetail(DetailView):
    model = TreeSample
