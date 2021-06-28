from django.test import TestCase
from rest_framework.test import APIRequestFactory
from django.urls import reverse
from .views import KurssiViewSet, OpettajaViewSet
from .models import Kurssi, Opettaja


class ViewSetTest(TestCase):
    def test_opettaja_view_set(self):
        '''Opettajan lisäys ja haku onnistuu'''
        request = APIRequestFactory().get("")
        ope_set = OpettajaViewSet.as_view({'get': 'retrieve'})

        ope = Opettaja.objects.create(nimi="Pena", puhelin="1234567")

        # pk tarkoittaa pääavainta eli id:tä
        response = ope_set(request, pk=ope.pk)

        # Testataan että tulee oikea statuskoodi
        self.assertEqual(response.status_code, 200)
        # Testataan että objekti luotiin juuri sellaiseksi kuin oli tarkoitus
        self.assertEqual(response.data, {'id': 1, 'nimi': 'Pena', 'puhelin': "1234567"})


    def test_kurssi_view_set(self):
            '''Kurssin lisäys ja haku onnistuu'''
            request = APIRequestFactory().get("")

            # Kurssin lisääminen vaatii tässä ensiksi luotavan opettajan
            ope_set = OpettajaViewSet.as_view({'get': 'retrieve'})
            ope = Opettaja.objects.create(nimi="Pekka", puhelin="1234567")

            kurssi_set = KurssiViewSet.as_view({'get': 'retrieve'})
            kurssi = Kurssi.objects.create(nimi="Ohjelmontikurssi",
            laajuus=8, opettaja_id=ope.pk)

            response = kurssi_set(request, pk=kurssi.pk)

            # Testataan että tulee oikea statuskoodi
            self.assertEqual(response.status_code, 200)
            
            # Testataan että objekti luotiin juuri sellaiseksi kuin oli tarkoitus
            self.assertEqual(response.data, {'id': 1, 'nimi': 'Ohjelmontikurssi', 'laajuus': 8, 'opettaja': 1})
