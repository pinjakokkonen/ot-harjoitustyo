import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_alkusaldo_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10)
    
    def test_saldon_lataaminen_onnistuu(self):
        self.maksukortti.lataa_rahaa(500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 15)
    
    def test_saldo_vähenee_oikein_jos_rahaa(self):
        self.maksukortti.ota_rahaa(500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 5)
    
    def test_saldo_ei_muutu_jos_kortilla_ei_tarpeeksi_rahaa(self):
        self.maksukortti.ota_rahaa(1500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 10)

    def test_ota_rahaa_palauttaa_true_jos_onnistuu(self):
        self.assertEqual(self.maksukortti.ota_rahaa(500), True)
    
    def test_ota_rahaa_palauttaa_false_jos_epäonnistuu(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1500), False)
    
    def test_kortin_rahasumma_tulostuu_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")