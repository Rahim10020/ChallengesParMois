from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('ChallengesApp.urls')),   # url pour la page d'acceuil
    path('admin/', admin.site.urls),
]
