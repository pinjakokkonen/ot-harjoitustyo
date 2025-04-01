import random

class UnoService:
    def __init__(self):
        self.deck = []
        self.player1 = []
        self.player2 = []
        self.stack = []
        self.turn = "player1"

    def create_deck(self):
        numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        colors = ["green", "red", "blue", "yellow"]
        for i in numbers:
            for j in colors:
                self.deck.append((i,j))
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
        if self.turn == "player1":
            play = (int(card[0]), card[2:])
            for i in self.player1:
                if i == play:
                    self.stack = i
                    self.player1.remove(i)
                    self.turn = "player2"
        else:
            play = (int(card[0]), card[2:])
            for i in self.player2:
                if i == play:
                    self.stack = i
                    self.player2.remove(i)
                    self.turn = "player1"
