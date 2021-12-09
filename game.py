import copy
# import pandas as pd
import random
import time
from strategy import Q_learning
from player import Player
from board import Board

class Game:

    def __init__(self, player1, player2, board):
        self.player1 = player1
        self.player2 = player2
        self.board = board
        self.playerXWins = 0
        self.playerOWins = 0
        self.draws = 0
        self.winner=None

    def play_game(self):
        random_list=[self.player1,self.player2]
        current_player= random_list[random.randrange(0,2)]
        while(self.board.game_result()=='Game_not_ended'):
            available_moves=self.board.available_moves()
            move= current_player.move(available_moves, self.board)
            self.board.move(move, current_player.player_value)
            # print(self.board.print_board())
            # time.sleep(1)
            if current_player == self.player1:
                current_player = self.player2
            else:
                current_player = self.player1
        if self.board.game_result() == self.player1.player_value:
            self.winner='player1'
            self.player1.reward(1)
            self.player2.reward(-1)

        elif self.board.game_result() == self.player2.player_value:
            self.winner='player2'
            self.player1.reward(-1)
            self.player2.reward(1)

        else:
            self.winner= 'draw'
            self.player2.reward(0.1)
            self.player2.reward(0.1)


if __name__=='__main__':
    # p1=Player('Random_strategy','x')
    q_strategy=Q_learning()
    p1=Player(q_strategy,'x')
    p2=Player('Random_strategy','o')
    b1=Board(3)
    pg=Game(p1,p2,b1)
    pg.play_game()
