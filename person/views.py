
from django.shortcuts import render
# Create your views here.


def List_person(request):
    return render(request, 'person/Listperson.html')
