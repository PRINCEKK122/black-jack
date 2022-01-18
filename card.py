from enums.cardValue import CardValue
from enums.suit import Suit

class Card():
    def __init__(self, card_value: CardValue, suit: Suit):
        self.card_value = card_value
        self.suit = suit

    def __str__(self):
        # return "Name: " + self.cardValue.name  + " of " + self.suit.name
        return f"Suit: {self.suit.name} Value: {self.card_value._value_}"
