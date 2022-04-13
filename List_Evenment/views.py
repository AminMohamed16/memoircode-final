
from django.shortcuts import render
# Create your views here.


def List_Evenment(request):
    return render(request, 'listevenment/listevenment.html')
