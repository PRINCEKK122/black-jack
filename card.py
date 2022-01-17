from enums.cardValue import CardValue
from enums.suit import Suit

class Card():
    def __init__(self, card_value: CardValue, suit: Suit):
        self.card_value = card_value
        self.suit = suit

    def __str__(self):
        # return "Name: " + self.cardValue.name  + " of " + self.suit.name
        return f"""Name: {self.card_value._name_}
Value: {self.card_value._value_}
Suit name: {self.suit.name}
Suit value: {self.suit.value}
    """
