
from multiprocessing import context
from django.shortcuts import get_object_or_404, render
from .models import Evenment, Comment
# comments Form
from .forms import NewComment
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
    Detials = get_object_or_404(Evenment, pk=id)
    comments = Detials.comments.filter(active=True)
    comment_from = NewComment()
    context = {

        'Evenments': Detials,
        'Detials': Detials,
        'comments': comments,
        'comment_form': comment_from,
    }
    return render(request, 'ListEvenment/page_Evenment.html', context)
