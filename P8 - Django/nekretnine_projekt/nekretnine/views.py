from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
from .models import Nekretnina


def lista_nekretnina(request):

    nekretnine = Nekretnina.objects.all()

    context = {'nekretnine': nekretnine }

    return render(request, 'nekretnine/main.html', context)
