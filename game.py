# creating a game class
# Create a deck of cards
# Create a list of players
# Shuffle the cards
# Assign 2 cards to each Player
# Update Player status
# if player status == HIT: make a deal
# if player status == stick : no deal
#  if player status == busted : eject from game

# condition to end game
# All players stick, the one closet to 21 wins
# any player hit exactly 21
# all players go bust except 1
from typing import List
from deck import Deck
from player import Player
from enums.gamestatus import GameStatus
from enums.playerstatus import PlayerStatus


class Game():
    def __init__(self):
        self.status = GameStatus.IN_PROGRESS
        self.deck = Deck()
        #self.winners: List[Player] = []
        #self.remainingPlayers: List[Player] = []
        self.players = [
            Player("player1"),
            Player("player2"),
            Player("player3")
        ]

    def deal_card(self):
        print("Winner: Inside deal")
        for player in self.players:
            if player.get_player_status() == PlayerStatus.HIT:
                player.accept_card(self.deck.cards.pop())
                player.set_player_status()

    def start_game(self):
        print("Winner: Inside: start game")
        self.deal_card()
        self.deal_card()

        while self.status == GameStatus.IN_PROGRESS:
            self.update_game_status()
            self.deal_card()
            for player in self.players:
                print(player)

        if self.status == GameStatus.GAME_OVER:
            print("\nGame over")
            print("\nWinners")
            for player in self.get_winners():
                print(player)


    def update_game_status(self):
        busted_players = [player for player in self.players if player.get_player_status() == PlayerStatus.BUSTED]
        stuck_players = [player for player in self.players if player.get_player_status() == PlayerStatus.STICK]

        # set game status to GAME OVER when on player hit exactly 21
        if any(player.get_total_cards_value() == 21 for player in self.players):
            self.status = GameStatus.GAME_OVER
            print("A Player reached 21") #active

        # set game status to GAME OVER when all players go bust except 1
        elif (len(self.players) - 1) == len(busted_players):
            self.status = GameStatus.GAME_OVER
            print("Only one Player left") # active

        # set game status to GAME OVER when all players stick
        elif len(stuck_players) == len(self.players):
            self.status = GameStatus.GAME_OVER
            print("All players stuck") #active

        # All Players do not have a stick status
        elif len(stuck_players)+ len(busted_players) == len(self.players):
            self.status = GameStatus.GAME_OVER
            print("No player has a stick status") #active


    def get_winners(self)->List[Player]:
        winners = [player for player in self.players if player.get_player_status() == PlayerStatus.WINNER]
        if not winners:
            max_score = max([player.get_total_cards_value() for player in self.players])
            winners = [player for player in self.players if player.get_total_cards_value() == max_score]
        return winners

