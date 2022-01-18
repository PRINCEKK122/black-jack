from typing import List
from deck import Deck
from player import Player
from enums.gamestatus import GameStatus
from enums.playerstatus import PlayerStatus


class Game():
    def __init__(self, players: List[Player]):
        print(*players)
        self.status = GameStatus.IN_PROGRESS
        self.deck = Deck()
        self.winners: List[Player] = []
        self.remainingPlayers: List[Player] = []
        self.players = []
        self.__setPlayers(players)

    # requirement number 2
    def __setPlayers(self, players: List[Player]) -> None:
            if len(players) == 0:
                self.players = [Player("player1"), Player("player2"), Player("player3")]
                self.start_game()
            elif (len(players) < 1) or (len(players) > 6):
                print("The number of players should be between 2 and 6 inclusive. Exiting!!")
                self.status = GameStatus.GAME_OVER
            else:
                for player in players:
                    self.players.append(Player(player))
                
                self.start_game()

    def deal_card(self) -> None:
        for player in self.remainingPlayers:
            if player.get_player_status() == PlayerStatus.HIT:
                player.accept_card(self.deck.cards.pop())
                player.set_player_status()

    def start_game(self) -> None:
        self.remainingPlayers = self.players.copy()
        self.deal_card()
        self.deal_card()

        while(self.status == GameStatus.IN_PROGRESS):
            self.checkWinners(self.remainingPlayers)

    def update_game_status(self, winners: List[Player]) -> None:
        if len(winners) == 0:
            print("******************No winner in this round*************")
            self.print_participants()
            self.status = GameStatus.GAME_OVER

        if len(winners) == 1:
            self.print_participants()
            print("***************Your winner*****************")
            for winner in winners:
                print(winner)

            self.status = GameStatus.GAME_OVER

        if len(winners) > 1:
            self.print_participants()
            print("*********************There was a tie!**************")

            for player in winners:
                print(player)

            self.status = GameStatus.GAME_OVER

    def checkWinners(self, players: List[Player]) -> None:
        self.remainingPlayers = [player for player in players if player.get_player_status() != PlayerStatus.BUSTED]

        # checks if the is winner
        for player in self.remainingPlayers:
            if player.get_player_status() == PlayerStatus.WINNER:
                self.winners.append(player)

        # checks if all the remaining players are of status STICK
        if all(player.get_player_status() == PlayerStatus.STICK for player in self.remainingPlayers):
            highest_score = max([player.get_total_cards_value() for player in self.remainingPlayers])
            winners = [player for player in self.remainingPlayers if player.get_total_cards_value() == highest_score]
            
            for player in winners:
                self.winners.append(player)

        if (len(self.winners) >= 1) or (len(self.remainingPlayers) == 1):
            self.update_game_status(self.winners)

        self.deal_card()

    def print_participants(self) -> None:
        print("****************Participants**************")
        for player in self.players:
            print(player)
