from django.urls import path

from ChallengesApp.views import index, mes_challenges, challenges_par_mois

urlpatterns = [
    path('', index, name = "page_acceuil"),
    path('challenges/', mes_challenges, name = "challenge_page"),  # url pour la liste de tous les challenges
    path('challenges/<slug:mois>/', challenges_par_mois, name="challenges_par_mois")       # url pour afficher la
    # liste des chalenges en
    # fonction du mois
]
