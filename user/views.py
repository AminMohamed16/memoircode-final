
from turtle import title
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import UserCreationForm, LoginForm
from django.contrib.auth import login, authenticate, logout

def register(request):
    if request.method == 'POST':
        forms = UserCreationForm(request.POST)
        if forms.is_valid():
            new_user = forms.save(commit=False)
            username = forms.cleaned_data['username']
            new_user.set_password(forms.cleaned_data['password1'])
            new_user.save()
            # messages.success(
            #    request, 'Inscription terminée avec {new_user} success'.format(username))
            messages.success(
                request, f'Inscription terminée avec {new_user} success ')
            return redirect('List_Evenment')
    else:
        forms = UserCreationForm()
    return render(request, 'user/register.html', {
        'title': 'register',
        'form': forms,
    })


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('List_Evenment')
        else:
            messages.warning(
                request, 'Il y a une erreur dans le nom d\'utilisateur ou le mot de passe.')

    return render(request, 'user/login.html', {
        'title': 'login',
    })


def logout_user(request):
    logout(request)
    return render(request, 'user/logout.html', {
        'title': 'logout'
    })


def profile(request):
    return render(request, 'user/profile/profile.html', {
        'title': 'profile',
    })

