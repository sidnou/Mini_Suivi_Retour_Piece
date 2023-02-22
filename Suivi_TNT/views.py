from django.shortcuts import render
from .models import SuiviRetourPieceHP
from .forms import SuiviTntForm

# Create your views here.
AUTEUR = "Jacques-a S."
VERSION = "0.0.1beta"
ANNEE_CREATION = "2023"


def index(request):
    context = {
        'Auteur': AUTEUR,
        'Version': VERSION,
        'AnneeCreation': ANNEE_CREATION,
        'Titre': 'Suivi TNT',
        'DataTabSuiviTnts': SuiviRetourPieceHP.objects.all(),
    }
    return render(request, 'Suivi_TNT/index.html', context)


def add_suivi_tnt(request):
    context = {
        'Auteur': AUTEUR,
        'Version': VERSION,
        'AnneeCreation': ANNEE_CREATION,
        'Titre': 'Ajout Suivi TNT',
        'DataTabSuiviTnts': SuiviRetourPieceHP.objects.all(),
        'Forms': SuiviTntForm,
    }
    if request.method == "POST":
        forms_suivi_tnt = SuiviTntForm(request.POST)
        # print(forms_suivi_tnt.is_valid())

        if forms_suivi_tnt.is_valid():
            forms_suivi_tnt.save()
        else:
            context['Erreur'] = forms_suivi_tnt.errors
    return render(request, "Suivi_TNT/add-suivi-tnt.html", context)
