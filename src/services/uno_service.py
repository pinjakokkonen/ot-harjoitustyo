import random

class UnoService:
    def __init__(self):
        self.deck = []
        self.player1 = []
        self.player2 = []
        self.stack = []
        self.turn = "player1"
        self.actions = ["r", "s", "d", "wild", "wild draw four"]

    def create_deck(self):
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        colors = ["green", "red", "blue", "yellow"]
        for i in numbers:
            for j in colors:
                self.deck.append((i,j))
        random.shuffle(self.deck)
        self.stack = self.deck.pop()

        for i in self.actions:
            if i in self.actions[:3]:
                for j in colors:
                    self.deck.append((i,j))
            else:
                self.deck.append(i)
        random.shuffle(self.deck)

    def deal_cards(self):
        self.player1 = self.deck[:7]
        self.deck = self.deck[7:]
        self.player2 = self.deck[:7]
        self.deck = self.deck[7:]

    def start_game(self):
        self.create_deck()
        self.deal_cards()

    def play_card(self, card):
        action_card = True
        if card=="":
            return
        if card[0] not in self.actions:
            action_card = False
        if card not in self.actions[3:]:
            card = (card[0], card[2:])
        else:
            action_card = True
        if self.turn == "player1":
            for i in self.player1:
                if i == card:
                    self.continue_to_play(action_card, i)
        else:
            for i in self.player2:
                if i == card:
                    self.continue_to_play(action_card, i)

    def draw_a_card(self):
        if len(self.deck)>0:
            card = self.deck.pop()
            if self.turn == "player1":
                self.player1.append(card)
                self.turn = "player2"
            else:
                self.player2.append(card)
                self.turn = "player1"

    def check_action_card(self, action_card, card):
        if action_card:
            self.play_action_card(card)

    def play_action_card(self, card):
        if card[0] in ["r", "s"] or card == "wild":
            self.skip_turn()
        elif card[0] == "d":
            if self.turn == "player1":
                for _ in range(2):
                    draw = self.deck.pop()
                    self.player1.append(draw)
            else:
                for _ in range(2):
                    draw = self.deck.pop()
                    self.player2.append(draw)
        elif card == "wild draw four":
            if self.turn == "player1":
                for _ in range(4):
                    draw = self.deck.pop()
                    self.player1.append(draw)
            else:
                for _ in range(4):
                    draw = self.deck.pop()
                    self.player2.append(draw)
            self.skip_turn()

    def skip_turn(self):
        if self.turn == "player1":
            self.turn = "player2"
        else:
            self.turn = "player1"

    def check_colors(self, color):
        if color == self.stack[1]:
            return True
        return False

    def check_number(self, number):
        if number == self.stack[0] or self.stack in self.actions[3:]:
            return True
        return False

    def continue_to_play(self, action_card, i):
        if self.turn == "player1":
            if self.check_colors(i[1]) or self.check_number(i[0]) or i in self.actions[3:]:
                self.stack = i
                self.player1.remove(i)
                self.turn = "player2"
                self.check_action_card(action_card, i)
        else:
            if self.check_colors(i[1]) or self.check_number(i[0]) or i in self.actions[3:]:
                self.stack = i
                self.player2.remove(i)
                self.turn = "player1"
                self.check_action_card(action_card, i)

    def choose_color(self, color):
        self.stack = ("-", color)
        self.skip_turn()
