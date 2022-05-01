from django.urls import path
from user.views import User, sigin, visiteur, utilisateur, utilisateur_agrre


urlpatterns = [
    path('',User,name="User"),
    path('sigin/',sigin,name='sigin'),
    path('visiteur/',visiteur,name='visiteur'),
    path('utilisateur/',utilisateur,name='utilisateur'),
    path('utilisateur_agrre/',utilisateur_agrre,name='utilisateur_agrre'),

]
