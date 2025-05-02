from django.db import models

class Employe(models.Model):
    numEmp = models.IntegerField(unique=True)
    nom = models.CharField(max_length=100)
    nombre_jours = models.IntegerField()
    taux_journalier = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def salaire(self):
        return self.nombre_jours * self.taux_journalier

    def __str__(self):
        return f"{self.nom} - {self.numEmp}"
from django.db import models

