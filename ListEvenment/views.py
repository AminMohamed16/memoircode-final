
from multiprocessing import context
from django.shortcuts import render
from .models import Evenment
from django.http import HttpResponse
# from List_Evenment.models import Evenment

# Create your views here.


def List_Evenment(request, *args, **kwargs):
    Evenments = Evenment.objects.all()
    context = {
        'Evenments': Evenments
    }

    return render(request, 'ListEvenment/ListEvenment.html', context)


def page_Evenment(request):

    return render(request, 'ListEvenment/page_Evenment.html')
    # return HttpResponse("page_event") 