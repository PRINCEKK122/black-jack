import pytest
import sys

# set path to parent directory
sys.path.append('..')

from enums.suit import Suit
from enums.cardValue import CardValue
from enums.playerstatus import PlayerStatus
from card import Card
from player import Player


class TestPlayer:
    @pytest.fixture(scope='package')
    def test_player(self):
        test_player = Player("Test Player")
        test_player.accept_card(Card(CardValue(2), Suit(1)))
        test_player.accept_card(Card(CardValue(3), Suit(1)))
        test_player.accept_card(Card(CardValue(4), Suit(1)))
        test_player.accept_card(Card(CardValue(10), Suit(1)))

        yield test_player
        del test_player

    def test_get_total_cards_value(self, test_player: Player):
        assert test_player.get_total_cards_value() == 19

    def test_set_player_status(self, test_player: Player):
        assert test_player.get_player_status() == PlayerStatus.STICK


