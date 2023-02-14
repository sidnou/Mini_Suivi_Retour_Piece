from django.shortcuts import render

# Create your views here.
AUTEUR = "Jacques-a S."
VERSION = "0.0.1beta"


def index(request):
    context = {
        'Auteur': AUTEUR,
        'Version': VERSION,
        'Titre': 'Suivi TNT',
    }
    return render(request, 'Suivi_TNT/index.html', context)
