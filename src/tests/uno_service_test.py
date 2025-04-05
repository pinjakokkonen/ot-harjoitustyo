import unittest
from services.uno_service import UnoService

class TestUnoService(unittest.TestCase):
    def setUp(self):
        self.uno_service = UnoService()

    def test_create_deck(self):
        self.uno_service.create_deck()
        self.assertEqual(len(self.uno_service.deck), 53)

    def test_deal_cards(self):
        self.uno_service.create_deck()
        self.uno_service.deal_cards()
        self.assertEqual(len(self.uno_service.player1), 7)
        self.assertEqual(len(self.uno_service.player2), 7)

    def test_play_card(self):
        self.uno_service.player1 = [("3", "red")]
        self.uno_service.play_card("0 red")
        self.assertEqual(self.uno_service.stack, [])
        self.uno_service.play_card("3 red")
        self.assertEqual(self.uno_service.stack, ("3", "red"))
        self.assertEqual(self.uno_service.player1, [])
        self.uno_service.player2 = [("0", "green")]
        self.uno_service.play_card("4 red")
        self.assertEqual(self.uno_service.stack, ("3", "red"))
        self.uno_service.play_card("0 green")
        self.assertEqual(self.uno_service.stack, ("0", "green"))
        self.assertEqual(self.uno_service.player2, [])
