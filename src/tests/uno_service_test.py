import unittest
from services.uno_service import UnoService, InvalidCardError

class FakeUnoRepository:
    def __init__(self):
        self.users = {"player1": 0, "player2": 0}

    def find_wins(self):
        return self.users

    def add_win(self, user):
        wins = self.users[user]
        self.users[user]=wins+1

class TestUnoService(unittest.TestCase):
    def setUp(self):
        self.uno_service = UnoService(FakeUnoRepository())
        self.error = InvalidCardError()

    def test_start_game(self):
        self.uno_service.start_game()
        self.assertEqual(len(self.uno_service.deck), 93)

    def test_play_card(self):
        self.uno_service.stack = ("1", "red")
        self.uno_service.player1 = [("3", "red"), ("2", "green")]
        self.uno_service.player2 = [("3", "green")]
        with self.assertRaises(Exception):
            self.uno_service.play_card("0 red")
        self.assertEqual(self.uno_service.stack, ("1", "red"))
        self.uno_service.play_card("3 red")
        self.assertEqual(self.uno_service.stack, ("3", "red"))
        with self.assertRaises(Exception):
            self.uno_service.play_card("4 red")
        self.assertEqual(self.uno_service.stack, ("3", "red"))
        self.uno_service.play_card("3 green")
        self.assertEqual(self.uno_service.stack, ("3", "green"))
        with self.assertRaises(Exception):
            self.uno_service.play_card("")
        self.assertEqual(self.uno_service.stack, ("3", "green"))

    def test_draw_a_card(self):
        self.uno_service.draw_a_card()
        self.assertEqual(len(self.uno_service.player1), 0)
        self.test_start_game()
        self.assertEqual(len(self.uno_service.player1), 7)
        self.uno_service.draw_a_card()
        self.assertEqual(len(self.uno_service.player1), 8)
        self.uno_service.draw_a_card()
        self.assertEqual(len(self.uno_service.player2), 8)

    def test_play_action_card_wild_draw_four(self):
        self.test_start_game()
        self.uno_service.player1 = [("r", "red"), ("s", "red"), ("wild"), ("wild draw four")]
        self.uno_service.player2 = [("d", "green")]
        with self.assertRaises(Exception):
            self.uno_service.play_card(("r", "red"))
        self.assertEqual(self.uno_service.turn, "player1")
        self.uno_service.play_card(("wild draw four"))
        self.assertEqual(len(self.uno_service.player2), 5)

    def test_skip_turn(self):
        self.uno_service._skip_turn()
        self.assertEqual(self.uno_service.turn, "player2")
        self.uno_service._skip_turn()
        self.assertEqual(self.uno_service.turn, "player1")

    def test_choose_color(self):
        self.uno_service.stack = ("1", "red")
        self.uno_service.choose_color("green")
        self.assertEqual(self.uno_service.stack, ("-", "green"))
        self.assertEqual(self.uno_service.turn, "player2")
