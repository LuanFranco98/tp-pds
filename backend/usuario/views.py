from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    usuarios = []
    return JsonResponse(usuarios, safe=False)