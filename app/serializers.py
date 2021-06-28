from rest_framework import serializers
from .models import Opettaja, Kurssi

class OpettajaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opettaja
        fields = ['id', 'nimi', 'puhelin']

class KurssiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kurssi
        fields = ['id', 'nimi', 'laajuus', 'opettaja']
