import random
from repositories.uno_repository import uno_repository
from .cards_service import CardsService


class InvalidCardError(Exception):
    pass

class UnoService:
    """Sovelluksen toiminnallisuuksista vastaava luokka.
    
    Attributes:
        deck: Koko korttipakka
        player1: Pelaajan 1 kortit
        player2: Pelaajan 2 kortit
        stack: Korttipinon päällimmäinen kortti
        turn: Kertoo kenen vuoro on
        actions: Erikoiskorttien toiminnot
    """

    def __init__(self):
        """Pohjustaa sovelluslogiikasta vastaavan luokan."""
        self.repository = uno_repository
        self.deck = []
        self.player1 = []
        self.player2 = []
        self.stack = []
        self.turn = "player1"
        self.actions = ["r", "s", "d", "wild", "wild draw four"]
        self.win = False
        self.discard_pile = []

    def start_game(self):
        """Huolehtii tarvittavista asioista ennen pelin alkua."""
        creating = CardsService()
        self.deck = creating.create_deck()
        self.stack = creating.set_stack()
        dealing_cards = creating.deal_cards(self.deck)
        self.deck = dealing_cards[0]
        self.player1 = dealing_cards[1]
        self.player2 = dealing_cards[2]

    def play_card(self, card):
        """Kortin pelaaminen ja erikoiskortin tarkastus.
        
        Args:
            card: Pelattava kortti
        """
        action_card = True
        if card=="":
            raise InvalidCardError("Invalid card, try again")
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
                    return
        else:
            for i in self.player2:
                if i == card:
                    self.continue_to_play(action_card, i)
                    return
        raise InvalidCardError("Invalid card, try again")

    def draw_a_card(self):
        """Kortin nostaminen pakasta."""
        if len(self.deck)<=0:
            if self.shuffle_cards():
                return
        card = self.deck.pop()
        if self.turn == "player1":
            self.player1.append(card)
            self.turn = "player2"
        else:
            self.player2.append(card)
            self.turn = "player1"

    def check_action_card(self, action_card, card):
        """Tarkastaa onko kortti erikoiskortti.
        
        Args:
            action_card: Kertoo onko kortti erikoiskortti
            card: Kyseessä oleva kortti
        """
        if action_card:
            self.play_action_card(card)

    def play_action_card(self, card):
        """Erikoiskorttien toimintojen toteutus.
        
        Args:
            card: Pelattava kortti
        """
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
        """Tarkastus onko pelattavan kortin väri sama kuin pinossa olevan.
        
        Args:
            color: Kortin väri

        Returns:
            Palauttaa onko väri sama vai eri kuin keskipakassa olevan kortin.
        """
        if color == self.stack[1]:
            return True
        return False

    def check_number(self, number):
        """Tarkastus onko pelattavan kortin numero sama kuin pinossa olevan.
        
        Args:
            number: Kortin arvo
        
        Returns:
            Palauttaa onko arvo sama kuin keskipakassa olevan kortin.
        """
        if number == self.stack[0] or self.stack in self.actions[3:]:
            return True
        return False

    def continue_to_play(self, action_card, i):
        """Kortin pelaaminen.
        
        Args:
            action_card: Kertoo onko kortti erikoiskortti
            i: Pelattava kortti
        """
        if self.turn == "player1":
            if self.check_colors(i[1]) or self.check_number(i[0]) or i in self.actions[3:]:
                if self.stack[0]!="-":
                    self.discard_pile.append(self.stack)
                self.stack = i
                self.player1.remove(i)
                if self.check_winning(self.player1):
                    self.win = True
                    return
                self.turn = "player2"
                self.check_action_card(action_card, i)
                return
        else:
            if self.check_colors(i[1]) or self.check_number(i[0]) or i in self.actions[3:]:
                if self.stack[0]!="-":
                    self.discard_pile.append(self.stack)
                self.stack = i
                self.player2.remove(i)
                if self.check_winning(self.player2):
                    self.win = True
                    return
                self.turn = "player1"
                self.check_action_card(action_card, i)
                return
        raise InvalidCardError("Invalid card, try again")

    def choose_color(self, color):
        """Vaihdetaan haluttuun väriin.
        
        Args:
            color: Väri, johon halutaan vaihtaa
        """
        self.discard_pile.append(self.stack)
        self.stack = ("-", color)
        self.skip_turn()

    def check_winning(self, player):
        """Tarkastaa onko peli päättynyt.
        
        Args:
            player: Pelaaja kenen vuoro oli
        
        Returns:
            Palauttaa onko voittaja selvinnyt.
        """
        if len(player)==0:
            self.winner()
            return True
        return False

    def winner(self):
        """Lisää voiton."""
        self.repository.add_win(self.turn)

    def find_charts(self):
        """Hakee voittotilastot.
        
        Returns:
            Palauttaa pelattujen pelien tilastot.
        """
        return self.repository.find_wins()

    def shuffle_cards(self):
        """Sekoittaa pois pelatut kortit.
        
        Returns:
            Palauttaa jatketaanko pelaamista vai ei.
        """
        if not self.discard_pile:
            self.win=True
            return True
        self.deck = self.discard_pile
        random.shuffle(self.deck)
        self.discard_pile = []
        return False
