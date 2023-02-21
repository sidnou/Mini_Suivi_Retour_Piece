from django.db import models


# Create your models here.

class SuiviRetourPieceHP(models.Model):
    reference = models.CharField(max_length=10)
    numero_commande = models.CharField(max_length=10, null=False)
    numero_dossier = models.CharField(max_length=15, null=False)
    numero_suivi = models.CharField(max_length=20, unique=True, null=False)
    date_creation = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.reference} {self.numero_commande} {self.numero_dossier} {self.numero_suivi} {self.date_creation}'
