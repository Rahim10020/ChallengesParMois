from django.shortcuts import render, get_object_or_404

from ChallengesApp.models import Challenge


def index(request):     # vue pour la page d'accueil
    return render(request, "ChallengesApp/index.html")


def mes_challenges(request):    # vue pour tous les challenges

    mois = Challenge.objects.all()
    return render(request, "ChallengesApp/challenges.html", {'mois': mois})


def challenges_par_mois(request, mois):     # vue pour tous les challenges par moi

    # on recupere un objet de la classe Challenge dont le mois est egale a la variable mois passe en parametre
    challenge = get_object_or_404(Challenge, mois = mois.capitalize())
    return render(request, "ChallengesApp/challenges_par_mois.html", {'challenge': challenge})
