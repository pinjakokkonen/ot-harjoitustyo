import unittest
from services.uno_service import UnoService

class TestUnoService(unittest.TestCase):
    def setUp(self):
        self.uno_service = UnoService()

    def test_create_deck(self):
        self.uno_service.create_deck()
        self.assertEqual(len(self.uno_service.deck), 40)
