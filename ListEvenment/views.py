
from multiprocessing import context
from django.shortcuts import get_object_or_404, render, redirect
from .models import Evenment, Comment
# comments Form
from .forms import NewComment
# Filter
from .filters import Evenment_filter
# Create your views here.
from ListEvenment.views import Evenment


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
    comments = Detials.comments.filter()
    comment_from = NewComment()
    # new_comment = None      active=True
    context = {

        'Evenments': Detials,
        'Detials': Detials,
        'comments': comments,
        'comment_form': comment_from,
    }
    # teb3ath les donne men formulair ll base de donnee
    # if request.method == 'POST':
    #     comment_from = NewComment(data=request.POST)
    #     if comment_from.is_valid():
    #         new_comment = comment_from.save(commit=False)
    #         new_comment.Detials = Detials
    #         new_comment.save()
    #         comment_from = NewComment()
    #     else:
    #         comment_from = NewComment()

    return render(request, 'ListEvenment/page_Evenment.html', context)


def mes_evenment(request):
    Evenments = Evenment.objects.filter(author= request.user)
    return render(request, 'ListEvenment/mes_evenment.html', {
        'title': 'mes_evenment',
        'Evenments':Evenments,
    })
