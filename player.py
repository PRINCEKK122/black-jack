from typing import List
from enums.playerstatus import PlayerStatus
from card import Card


class Player():
    def __init__(self, player_name: str):
        self.player_name = player_name
        self.player_status = PlayerStatus.HIT
        self.cards_in_hand: List[Card] = []

    def accept_card(self, card: Card):
        self.cards_in_hand.append(card)

    def get_total_cards_value(self):
        return sum([card.card_value._value_ for card in self.cards_in_hand])

    def get_cards_in_hand(self):
        return self.cards_in_hand

    def get_player_name(self):
        return self.player_name

    def set_player_status(self):
        if self.get_total_cards_value() < 17:
            self.player_status = PlayerStatus.HIT
        elif self.get_total_cards_value() < 21:
            self.player_status = PlayerStatus.STICK
        elif self.get_total_cards_value() == 21:
            self.player_status = PlayerStatus.WINNER
        else:
            self.player_status = PlayerStatus.BUSTED

    def get_player_status(self):
        return self.player_status

    def __str__(self):
        return f"Player name: {self.player_name}. Cards: {[str(card) for card in self.cards_in_hand]}. Total points: {self.get_total_cards_value()}. Player Status: {self.get_player_status()}" 
