from enums.cardValue import CardValue
from enums.suit import Suit

class Card():
  def __init__(self, cardValue: CardValue, suit: Suit):
    self.cardValue = cardValue
    self.suit = suit

  def __str__(self):
    # return "Name: " + self.cardValue.name  + " of " + self.suit.name
    return f"""Name: {self.cardValue._name_}
Value: {self.cardValue._value_}
Suit name: {self.suit.name}
Suit value: {self.suit.value}
    """  
  