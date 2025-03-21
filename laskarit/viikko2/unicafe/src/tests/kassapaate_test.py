import unittest
from maksukortti import Maksukortti
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)
    
    def test_luotu_kassapaate_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
    
    def test_kateisosto_edullinen_toimii_kun_riittava_summa(self):
        maksu = self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002.4)
        self.assertEqual(maksu, 0)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_kateisosto_edullinen_ei_toimi_kun_ei_tarpeeksi_rahaa(self):
        maksu = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
        self.assertEqual(maksu, 200)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kateisosto_maukas_toimii(self):
        maksu = self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1004)
        self.assertEqual(maksu, 0)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_kateisosto_maukas_ei_toimi_kun_ei_tarpeeksi_rahaa(self):
        maksu = self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
        self.assertEqual(maksu, 300)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_korttiosto_edullinen_toimii_kun_riittava_summa(self):
        maksu = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 760)
        self.assertEqual(maksu, True)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_korttiosto_edullinen_ei_toimi_kun_ei_tarpeeksi_rahaa(self):
        kortti = Maksukortti(200)
        maksu = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 200)
        self.assertEqual(maksu, False)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_korttiosto_maukas_toimii_kun_riittava_summa(self):
        maksu = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 600)
        self.assertEqual(maksu, True)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_korttiosto_maukas_ei_toimi_kun_ei_tarpeeksi_rahaa(self):
        kortti = Maksukortti(200)
        maksu = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 200)
        self.assertEqual(maksu, False)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_rahan_lataaminen_onnistuu(self):
        lataus = self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)
        self.assertEqual(self.maksukortti.saldo, 1500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100500)
    
    def test_rahan_lataaminen_ei_onnistu_negatiivisella_arvolla(self):
        lataus = self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -500)
        self.assertEqual(self.maksukortti.saldo, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)