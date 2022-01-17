# player name
# list of cards
# player status


# accept_card()
# get_cards_value()
# set_player_staus()
#

from enums.playerstatus import PlayerStatus
from typing import List
from card import Card


class Player():
    def __init__(self, player_name: str):
        self.player_name = player_name
        self.player_status = PlayerStatus.HIT
        self.cards_in_hand: List[Card] = []

    def accept_card(self, card: Card):
        self.cards_in_hand.append(card)

    def get_total_cards_value(self):
        if(len(self.cards_in_hand) == 0):
            return 0
        return sum([card.cardValue._value_ for card in self.cards_in_hand])

    def get_cards_in_hand(self):
        return self.cards_in_hand

    def __set_player_status(self):
        if(self.get_total_cards_value() < 17):
            self.player_status = PlayerStatus.HIT
        elif(self.get_total_cards_value() < 21):
            self.player_status = PlayerStatus.STICK
        else:
            self.player_status = PlayerStatus.BUSTED

    def get_player_status(self):
        return self.player_status
