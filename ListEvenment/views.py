
from pdb import post_mortem
from django.shortcuts import get_object_or_404, render
from .models import Evenment
from ListEvenment.views import Evenment
# from .views import PostCreateForm
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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


class Creatnew_evenment(LoginRequiredMixin, CreateView):

    model = Evenment
    template_name = 'ListEvenment/add_evenment.html'
    fields = '__all__'

    def form_invalid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class edit_evenment(UpdateView):
    # UserPassesTestMixin, LoginRequiredMixin,
    model = Evenment
    template_name = 'ListEvenment/edite_evenment.html'
    fields = '__all__'

    # def form_invalid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)

    # def test_func(self):
    #     post = self.get_object()
    #     if self.request.user == post.author:
    #         return True
    #     else:
    #         return False
