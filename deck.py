import random
from enums.suit import Suit
from enums.cardValue import CardValue
from card import Card

class Deck():
    def __init__(self):
        self.cards = []
        self.__initialize_cards()
        
    def __initialize_cards(self):
        for suit in Suit:
            for card in CardValue:
                self.cards.append(Card(card, suit))

        self.__shuffle()        

    def __shuffle(self):
        random.shuffle(self.cards)

    def __str__(self):
        display_result = ""

        for card in self.cards:
            display_result += str(card) + "\n"

        # print(len(self.cards))
        return display_result
