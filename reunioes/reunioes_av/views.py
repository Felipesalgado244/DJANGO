from django.shortcuts import render
from .models import ReuniaoAv

def index(request):
    reunioes_av = ReuniaoAv.objects.all()
    return render(request, 'reunioes_av/index.html',{ 'reunioes_av': reunioes_av })