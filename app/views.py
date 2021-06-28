from rest_framework import viewsets
from .models import Opettaja, Kurssi
from .serializers import OpettajaSerializer, KurssiSerializer

'''Ao. metodi osaa tehdä kaikki crud toiminnot ja hakea opettajat:
    -kaikki opettajat: /api/opettajat
    -opettajan id:llä /api/opettajat/id
    -opettajan nimellä: /api/opettajat/?nimi=joku_nimi
'''

class OpettajaViewSet(viewsets.ModelViewSet):
    serializer_class = OpettajaSerializer
    def get_queryset(self):
        queryset = Opettaja.objects.all()
        nimi = self.request.query_params.get("nimi")
        if nimi is not None:
            queryset = queryset.filter(nimi__icontains=nimi)
        return queryset

'''Ao. metodi osaa tehdä kaikki crud toiminnot ja hakea kurssit:
    -kaikki kurssit: /api/kurssit
    -kurssin id:llä /api/kurssit/id
    -kurssin nimellä: /api/kurssit/?nimi=joku_nimi
    -kurssit opettajan id:llä: /api/kurssit/?opettaja=opettaja_id
'''

class KurssiViewSet(viewsets.ModelViewSet):
    serializer_class = KurssiSerializer
    def get_queryset(self):
        queryset = Kurssi.objects.all()
        nimi = self.request.query_params.get("nimi")
        opettaja = self.request.query_params.get("opettaja")
        if nimi is not None:
            queryset = queryset.filter(nimi=nimi)
        if opettaja is not None:
            queryset = queryset.filter(opettaja=opettaja)
        return queryset
