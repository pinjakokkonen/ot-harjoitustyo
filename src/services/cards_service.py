import random

class CardsService:
    """Pelin alustamisesta huolehtiva luokka."""

    def __init__(self):
        self.stack = []

    def create_deck(self):
        """Luo korttipakan."""
        deck = []
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        colors = ["green", "red", "blue", "yellow"]
        for i in numbers:
            for j in colors:
                deck.append((i,j))
                deck.append((i,j))
        random.shuffle(deck)
        self.stack = deck.pop()

        actions = ["r", "s", "d", "wild", "wild draw four"]

        for i in actions:
            if i in actions[:3]:
                for j in colors:
                    deck.append((i,j))
                    deck.append((i,j))
            else:
                deck.append(i)
                deck.append(i)
        random.shuffle(deck)
        return deck

    def set_stack(self):
        """Palauttaa keskipakan päällimmäisen kortin."""
        return self.stack

    def deal_cards(self, deck):
        """Jakaa kortit pelaajille.
        
        Args:
            deck: Koko korttipakka
        """
        player1 = deck[:7]
        deck = deck[7:]
        player2 = deck[:7]
        deck = deck[7:]
        return deck, player1, player2
