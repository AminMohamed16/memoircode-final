
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import UserCreationForm, LoginForm, UserUpdateForm, ProfilUpdateForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            # username = form.cleaned_data['username']
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            # messages.success(
            #    request, 'تهانينا {} لقد تمت عملية التسجيل بنجاح.'.format(username))
            messages.success(
                request, f'Inscription terminée avec {new_user} success.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'user/register.html', {
        'title': 'register',
        'form': form,
    })


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.warning(
                request, 'Il y a une erreur dans le nom d\'utilisateur ou le mot de passe.')

    return render(request, 'user/login.html', {
        'title': 'login',
    })


def logout_user(request):
    logout(request)
    context = {
        'title': 'logout',
    }
    return render(request, 'user/logout.html', context)


@login_required(login_url='login')
def profile(request):
    context = {
        'title': 'profile',
    }
    return render(request, 'user/profile/profile.html', context)


@login_required(login_url='login')
def profile_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfilUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid and profile_form.is_valid:
            user_form.save()
            profile_form.save()
            messages.success(request, 'تم تحديث الملف الشخصي.')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfilUpdateForm(instance=request.user.profile)

    context = {
        'title': 'edit profile page',
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, 'user/profile/profile_update.html', context)
