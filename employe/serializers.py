from rest_framework import serializers
from .models import Employe

class EmployeSerializer(serializers.ModelSerializer):
    salaire = serializers.ReadOnlyField()
    id = serializers.IntegerField(read_only=True) # Add this line

    class Meta:
        model = Employe
        fields = ['id', 'numEmp', 'nom', 'nombre_jours', 'taux_journalier', 'salaire'] # Make sure 'id' is the first field here 