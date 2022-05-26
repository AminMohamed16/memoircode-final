
from multiprocessing import context
from django.shortcuts import get_object_or_404, render, redirect
from .models import Evenment
# from .views import PostCreateForm
# from django.views.generic import CreateView
# comments Form
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
    context = {

        'Evenments': Detials,
        'Detials': Detials,
    }

    return render(request, 'ListEvenment/page_Evenment.html', context)


def mes_evenment(request):
    Evenments = Evenment.objects.filter(author=request.user)
    return render(request, 'ListEvenment/mes_evenment.html', {
        'title': 'mes_evenment',
        'Evenments': Evenments,
    })


# class Creatnew_evenment(CreateView):

#     model = Evenment
#     fields = ['nomevenment', 'country', 'porte', 'type_evenment', 'organisateur',
#               'Descriptinos', 'date_creation_evenment', 'date_fine_evenment', 'image']
#     template_name = 'ListEvenment/new_post.html'
#     # form_class = PostCreateForm

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)
