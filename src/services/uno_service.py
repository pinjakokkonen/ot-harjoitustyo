import random
from repositories.uno_repository import uno_repository

class UnoService:
    """Sovelluksen toiminnallisuuksista vastaava luokka."""

    def __init__(self):
        """Pohjustaa sovelluslogiikasta vastaavan luokan.
        
        Args:
            deck: Koko korttipakka
            player1: Pelaajan 1 kortit
            player2: Pelaajan 2 kortit
            stack: Korttipinon päällimmäinen kortti
            turn: Kertoo kenen vuoro on
            actions: Erikoiskorttien toiminnot
        """
        self.repository = uno_repository
        self.deck = []
        self.player1 = []
        self.player2 = []
        self.stack = []
        self.turn = "player1"
        self.actions = ["r", "s", "d", "wild", "wild draw four"]
        self.win = False

    def create_deck(self):
        """Luo korttipakan."""
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
        """Jakaa kortit pelaajille."""
        self.player1 = self.deck[:7]
        self.deck = self.deck[7:]
        self.player2 = self.deck[:7]
        self.deck = self.deck[7:]

    def start_game(self):
        """Huolehtii tarvittavista asioista ennen pelin alkua."""
        self.create_deck()
        self.deal_cards()

    def play_card(self, card):
        """Kortin pelaaminen ja erikoiskortin tarkastus."""
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
        """Kortin nostaminen pakasta."""
        if len(self.deck)>0:
            card = self.deck.pop()
            if self.turn == "player1":
                self.player1.append(card)
                self.turn = "player2"
            else:
                self.player2.append(card)
                self.turn = "player1"

    def check_action_card(self, action_card, card):
        """Tarkastaa onko kortti erikoiskortti."""
        if action_card:
            self.play_action_card(card)

    def play_action_card(self, card):
        """Erikoiskorttien toimintojen toteutus."""
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
        """Vuoro ei vaihdu seuraavalle pelaajalle."""
        if self.turn == "player1":
            self.turn = "player2"
        else:
            self.turn = "player1"

    def check_colors(self, color):
        """Tarkastus onko pelattavan kortin väri sama kuin pinossa olevan."""
        if color == self.stack[1]:
            return True
        return False

    def check_number(self, number):
        """Tarkastus onko pelattavan kortin numero sama kuin pinossa olevan."""
        if number == self.stack[0] or self.stack in self.actions[3:]:
            return True
        return False

    def continue_to_play(self, action_card, i):
        """Kortin pelaaminen."""
        if self.turn == "player1":
            if self.check_colors(i[1]) or self.check_number(i[0]) or i in self.actions[3:]:
                self.stack = i
                self.player1.remove(i)
                if self.check_winning(self.player1):
                    self.win = True
                    return
                self.turn = "player2"
                self.check_action_card(action_card, i)
        else:
            if self.check_colors(i[1]) or self.check_number(i[0]) or i in self.actions[3:]:
                self.stack = i
                self.player2.remove(i)
                if self.check_winning(self.player2):
                    self.win = True
                    return
                self.turn = "player1"
                self.check_action_card(action_card, i)

    def choose_color(self, color):
        """Vaihdetaan haluttuun väriin."""
        self.stack = ("-", color)
        self.skip_turn()

    def check_winning(self, player):
        if len(player)==0:
            self.winner()
            return True
        return False

    def winner(self):
        self.repository.add_win(self.turn)

    def find_charts(self):
        return self.repository.find_wins()
