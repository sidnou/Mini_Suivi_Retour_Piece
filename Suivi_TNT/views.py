import csv
import io
from .models import SuiviRetourPieceHP
from django.shortcuts import render ,redirect
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


def import_data(request):
    if request.method == "POST":
        fichier_csv = request.FILES["file"]
        data_set = fichier_csv.read().decode("UTF-8",'iso8859-1')
        io_string = io.StringIO(data_set)
        next(io_string)

        for colonne in csv.reader(io_string, delimiter=",", quotechar='"'):
            _, cree = SuiviRetourPieceHP.objects.get_or_create(id=colonne[0],
                                                               reference=colonne[1],
                                                               numero_commande=colonne[2],
                                                               numero_dossier=colonne[3],
                                                               numero_suivi=colonne[4],
                                                               date_creation=colonne[5]
                                                               )
        return redirect('index')
    return render(request, "Suivi_TNT/import.html")
