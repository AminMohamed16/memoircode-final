
# from django.shortcuts import redirect, render
# from django.contrib.auth import authenticate, login
# from users.form import UserForm
# # Create your views here.


# def users(request):
#     error = ''
#     if request.method == "POST":
#         email = request.POST['email']
#         password = request.POST['password']
#         user = authenticate(request, email=email, password=password)
#         if user is not None:
#             login(request, user)
#             if user.is_visiteur:
#                 return redirect('visiteur')

#             elif user.is_utilisateur:
#                 return redirect('utilisateur')
#             else:
#                 return redirect('utilisateur_agrre')
#         else:
#             error = 'email ou password est incorrect '

#     return render(request, 'authontificatino/login.html', {'error': error})


# def sigin(request):
#     form = UserForm()
#     if request.method == "POST":
#         form = UserForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('users')
#     return render(request, 'authontificatino/Sigin.html', {'form': form})


# def visiteur(request):

#     return render(request, 'user/visiteur.html')


# def utilisateur(request):

#     return render(request, 'user/utilisateur.html')


# def utilisateur_agrre(request):

#     return render(request, 'user/utilisateur_agrre.html')
