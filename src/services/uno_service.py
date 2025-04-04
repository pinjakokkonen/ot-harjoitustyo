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
        if card[0] not in self.actions:
            action_card = False
        if card not in self.actions[3:]:
            card = (card[0], card[2:])
        else:
            action_card = True
        print(action_card, card)
        if self.turn == "player1":
            for i in self.player1:
                if i == card:
                    self.stack = i
                    self.player1.remove(i)
                    self.turn = "player2"
                    if action_card:
                        self.play_action_card(i)
        else:
            for i in self.player2:
                if i == card:
                    self.stack = i
                    self.player2.remove(i)
                    self.turn = "player1"
                    if action_card:
                        self.play_action_card(i)
    
    def draw_a_card(self):
        card = self.deck.pop()
        if self.turn == "player1":
            self.player1.append(card)
            self.turn = "player2"
        else:
            self.player2.append(card)
            self.turn = "player1"
    
    def play_action_card(self, card):
        if card[0] == "r" or card[0] == "s":
            if self.turn == "player1":
                self.turn = "player2"
            else:
                self.turn = "player1"
        elif card[0] == "d":
            if self.turn == "player1":
                for i in range(2):
                    draw = self.deck.pop()
                    self.player1.append(draw)
            else:
                for i in range(2):
                    draw = self.deck.pop()
                    self.player2.append(draw)
        elif card == "wild draw four":
            if self.turn == "player1":
                for i in range(4):
                    draw = self.deck.pop()
                    self.player1.append(draw)
            else:
                for i in range(4):
                    draw = self.deck.pop()
                    self.player2.append(draw)
        else:
            # wild
            pass
