from django import forms
from .models import SuiviRetourPieceHP


class SuiviTntForm(forms.ModelForm):
    class Meta:
        model = SuiviRetourPieceHP
        fields = "__all__"
        widgets = {
            'reference': forms.TextInput(attrs={'class': 'form-control mb-1'}),
            'numero_commande': forms.TextInput(attrs={'class': 'form-control mb-1'}),
            'numero_dossier': forms.TextInput(attrs={'class': 'form-control mb-1'}),
            'numero_suivi': forms.TextInput(attrs={'class': 'form-control mb-1'})
        }
