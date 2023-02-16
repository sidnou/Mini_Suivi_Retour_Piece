from django import forms
from .models import SuiviRetourPieceHP


class SuiviTntForm(forms.ModelForm):
    class Meta:
        model = SuiviRetourPieceHP
        fields = "__all__"
