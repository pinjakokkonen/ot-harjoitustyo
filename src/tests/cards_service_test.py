import unittest
from services.cards_service import CardsService

class TestCardsService(unittest.TestCase):
    def setUp(self):
        self.cards_service = CardsService()

    def test_create_deck(self):
        deck = self.cards_service.create_deck()
        self.assertEqual(len(deck), 107)
    
    def test_set_stack(self):
        stack = self.cards_service.set_stack()
        self.assertEqual(stack, [])

    def test_deal_cards(self):
        deck = self.cards_service.create_deck()
        cards = self.cards_service.deal_cards(deck)
        self.assertEqual(len(cards[1]), 7)
        self.assertEqual(len(cards[2]), 7)
