"""
import http
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index (request):
    return HttpResponse("Hola Pao.")
"""

from django.shortcuts import render

def cuentas(request):
    template_name = "programa2.html"
    ctx = {}
    return render(request, template_name, ctx)