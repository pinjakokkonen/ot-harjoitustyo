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

    def test_start_game(self):
        self.uno_service.start_game()
        self.assertEqual(len(self.uno_service.deck), 39)

    def test_play_card(self):
        self.uno_service.stack = ("1", "red")
        self.uno_service.player1 = [("3", "red")]
        self.uno_service.play_card("0 red")
        self.assertEqual(self.uno_service.stack, ("1", "red"))
        self.uno_service.play_card("3 red")
        self.assertEqual(self.uno_service.stack, ("3", "red"))
        self.assertEqual(self.uno_service.player1, [])
        self.uno_service.player2 = [("3", "green")]
        self.uno_service.play_card("4 red")
        self.assertEqual(self.uno_service.stack, ("3", "red"))
        self.uno_service.play_card("3 green")
        self.assertEqual(self.uno_service.stack, ("3", "green"))
        self.assertEqual(self.uno_service.player2, [])

    def test_draw_a_card(self):
        self.test_deal_cards()
        self.assertEqual(len(self.uno_service.player1), 7)
        self.uno_service.draw_a_card()
        self.assertEqual(len(self.uno_service.player1), 8)
        self.uno_service.draw_a_card()
        self.assertEqual(len(self.uno_service.player2), 8)

    def test_play_action_card_wild_draw_four(self):
        self.test_create_deck()
        self.uno_service.player1 = [("r", "red"), ("s", "red"), ("wild"), ("wild draw four")]
        self.uno_service.player2 = [("d", "green")]
        self.uno_service.play_card(("r", "red"))
        self.assertEqual(self.uno_service.turn, "player1")
        self.uno_service.play_card(("s", "red"))
        self.assertEqual(self.uno_service.turn, "player1")
        self.uno_service.play_card(("wild draw four"))
        self.assertEqual(len(self.uno_service.player2), 5)
        self.uno_service.play_card(("d", "green"))
        self.assertEqual(len(self.uno_service.player1), 3)

    def test_skip_turn(self):
        self.uno_service.skip_turn()
        self.assertEqual(self.uno_service.turn, "player2")
        self.uno_service.skip_turn()
        self.assertEqual(self.uno_service.turn, "player1")

    def test_choose_color(self):
        self.uno_service.stack = ("1", "red")
        self.uno_service.choose_color("green")
        self.assertEqual(self.uno_service.stack, ("-", "green"))
        self.assertEqual(self.uno_service.turn, "player2")
