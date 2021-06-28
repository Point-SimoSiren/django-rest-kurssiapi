from django.db import models

class Opettaja(models.Model):
    nimi = models.CharField(max_length=100, default='')
    puhelin = models.CharField(max_length=20, default='')

    class Meta:
        ordering = ['nimi']

class Kurssi(models.Model):
    nimi = models.CharField(max_length=100, default='')
    laajuus = models.IntegerField()
    opettaja = models.ForeignKey(Opettaja, on_delete=models.CASCADE)

    class Meta:
        ordering = ['nimi']
