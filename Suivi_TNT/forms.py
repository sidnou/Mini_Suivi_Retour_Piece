from django import forms
from .models import SuiviRetourPieceHP


class SuiviTntForm(forms.ModelForm):
    class Meta:
        model = SuiviRetourPieceHP
        fields = "__all__"
        labels = {
            'reference': '',
            'numero_commande': '',
            'numero_dossier': '',
            'numero_suivi': '',
        }
        widgets = {
            'reference': forms.TextInput(attrs={'class': 'form-control mb-1', 'placeholder': 'Référence'}),
            'numero_commande': forms.TextInput(
                attrs={'class': 'form-control mb-1', 'placeholder': 'Numéro Commande'}),
            'numero_dossier': forms.TextInput(attrs={'class': 'form-control mb-1', 'placeholder': 'Numéro Dossier'}),
            'numero_suivi': forms.TextInput(attrs={'class': 'form-control mb-1', 'placeholder': 'Numèro Suivi TNT'})
        }
