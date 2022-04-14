
from django.shortcuts import render
# Create your views here.


def sigin(request):
    return render(request, '/sigin.html')


# def login(request):
#     return render(request, '/authontificatino/login.html')


# def logout(request):
#     return render(request, '/authontificatino/logout.html')
