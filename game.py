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
        self.winners: List[Player] = []
        self.remainingPlayers: List[Player] = []
        self.players = [
            Player("player1"),
            Player("player2"),
            Player("player3")
        ]

    def deal_card(self):
        print("Winner: Inside deal")
        for player in self.remainingPlayers:
            if player.get_player_status() == PlayerStatus.HIT:
                player.accept_card(self.deck.cards.pop())
                player.set_player_status()

    def start_game(self):
        print("Winner: Inside: start game")

        self.remainingPlayers = self.players.copy()        
        self.deal_card()
        self.deal_card()

        print("**********************Remaining players*****************")
        for player in self.remainingPlayers:
            print(player)

        while(self.status == GameStatus.IN_PROGRESS):
            self.checkWinners(self.remainingPlayers)

    def update_game_status(self, winners: List[Player]):
        if len(winners) == 0:
            print("No winner in this round")
            self.status = GameStatus.GAME_OVER

        if len(winners) == 1:
            print("Original Players:")
            for player in self.players:
                print(player)

            for winner in winners:
                print(winner)

            self.status = GameStatus.GAME_OVER

        if len(winners) > 1:
            print("Original Players:")
            for player in self.players:
                print(player)
                
            print("There was a tie!")

            for player in winners:
                print(player)

            self.status = GameStatus.GAME_OVER

    def checkWinners(self, players: List[Player]):
        self.remainingPlayers = [
            player for player in self.players if player.get_player_status() != PlayerStatus.BUSTED]

        # checks if the is winner
        for player in self.remainingPlayers:
            if player.get_player_status() == PlayerStatus.WINNER:
                print("*********************We have a winner*****************")
                self.winners.append(player)
                self.update_game_status(self.winners)

        # checks if all the remaining players are of status STICK
        if all(player.get_player_status() == PlayerStatus.STICK for player in self.remainingPlayers):
            highest_score = max([player.get_total_cards_value()
                               for player in self.remainingPlayers])
            print("***************All Players are STICK***************")
           
            self.winners.append(
                [player for player in self.remainingPlayers if player.get_total_cards_value() == highest_score])

            self.update_game_status(self.winners)
        
        if len(self.remainingPlayers) == 0:
            print("***************No winners*****************")
            self.update_game_status(self.winners)

        self.deal_card()
        # self.status = GameStatus.GAME_OVER
