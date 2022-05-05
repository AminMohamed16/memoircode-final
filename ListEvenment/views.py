
from multiprocessing import context
from django.shortcuts import get_object_or_404, render
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


def page_Evenment(request, id):
    Detials = get_object_or_404(Evenment,pk=id)
    context = {
        'Evenments': Detials,
        'Detials': Detials
    }
    return render(request, 'ListEvenment/page_Evenment.html', {'Detials': Detials})
    # return HttpResponse("page_event")
