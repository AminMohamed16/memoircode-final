
from multiprocessing import context
from django.shortcuts import render
from .models import Evenment

from django.http import HttpResponse

# Filter
from .filters import Evenment_filter
# Create your views here.


def List_Evenment(request, *args, **kwargs):
    # filter
    Evenments = Evenment.objects.all()
    myFilter = Evenment_filter(request.GET, queryset=Evenments)
    Evenments = myFilter.qs
    context = {
        'Evenments': Evenments,
        'myFilter': myFilter
    }
    return render(request, 'ListEvenment/ListEvenment.html', context)


def page_Evenment(request, pk):
    Detials = Evenment.objects.get(id=pk)
    context = {
        'nomevenments': Detials.nomevenment,
        'date_creations': Detials.date_creation,
        'Descriptinos': Detials.Descriptinos,
        'images': Detials.image,
        'Evenments': Detials
    }

    return render(request, 'ListEvenment/page_Evenment.html', context)
    # return HttpResponse("page_event")
