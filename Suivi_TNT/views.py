from django.shortcuts import render
from .models import SuiviRetourPieceHP

# Create your views here.
AUTEUR = "Jacques-a S."
VERSION = "0.0.1beta"


def index(request):
    context = {
        'Auteur': AUTEUR,
        'Version': VERSION,
        'Titre': 'Suivi TNT',
        'DataTabSuiviTnts': SuiviRetourPieceHP.objects.all(),
    }
    return render(request, 'Suivi_TNT/index.html', context)


def add_suivi_tnt(request):
    context = {
        'Auteur': AUTEUR,
        'Version': VERSION,
        'Titre': 'Ajout Suivi TNT',
        'DataTabSuiviTnts': SuiviRetourPieceHP.objects.all(),
    }
    return render(request, "Suivi_TNT/add-suivi-tnt.html", context)
