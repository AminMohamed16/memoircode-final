
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from user.form import UserForm
# Create your views here.


def User(request):
    error = ''
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        User = authenticate(request, email=email, password=password)
        if User is not None:
            login(request, User)
            if User.is_visiteur:
                return redirect('visiteur')

            elif User.is_utilisateur:
                return redirect('utilisateur')
            else:
                return redirect('utilisateur_agrre')
        else:
            error = 'email ou password est incorrect '

    return render(request, 'authontificatino/login.html', {'error': error})


def sigin(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('User')
    return render(request, 'authontificatino/Sigin.html', {'form': form})


def visiteur(request):

    return render(request, 'user/visiteur.html')


def utilisateur(request):

    return render(request, 'user/utilisateur.html')


def utilisateur_agrre(request):

    return render(request, 'user/utilisateur_agrre.html')
