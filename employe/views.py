from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Employe
from .serializers import EmployeSerializer  # <--- NE PAS OUBLIER D'IMPORTER LE SERIALIZER
from django.db.models import Sum, Max, Min, F, FloatField
from django.db.models.functions import Cast

class EmployeViewSet(viewsets.ModelViewSet):
    queryset = Employe.objects.all()
    serializer_class = EmployeSerializer  
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'])
    def salaire_stats(self, request):
        stats = Employe.objects.annotate(
            salaire_calcule=Cast(F('nombre_jours') * F('taux_journalier'), FloatField())
        ).aggregate(
            total=Sum('salaire_calcule'),
            minimum=Min('salaire_calcule'),
            maximum=Max('salaire_calcule')
        )

        return Response({
            'somme_salaires': stats['total'] or 0,
            'salaire_minimal': stats['minimum'] or 0,
            'salaire_maximal': stats['maximum'] or 0
        })
