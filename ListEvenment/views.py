
from multiprocessing import context
from django.shortcuts import render
from .models import Evenment

from django.http import HttpResponse
# Create your views here.


def List_Evenment(request, *args, **kwargs):
    Evenments = Evenment.objects.all()
    context = {
        'Evenments': Evenments
    }

    return render(request, 'ListEvenment/ListEvenment.html', context)


def page_Evenment(request):
    Evenments = Evenment.objects.all()
    context = {
        'Evenments': Evenments
    }


    return render(request, 'ListEvenment/page_Evenment.html',context)
    # return HttpResponse("page_event")
