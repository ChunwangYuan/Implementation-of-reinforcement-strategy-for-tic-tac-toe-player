from board import Board

import time
from strategy import Q_learning
from player import Player
from board import Board
from game import Game
import pandas as pd
import matplotlib.pyplot as plt


#game_statistics: Printing statistics of the game in graph;

def game_statistics(player1_wins, player2_wins, draw_game, total_games,p1,p2):
    print(player1_wins,player2_wins, draw_game, total_games,'p1: ', p1.game_plan,'p2: ', p2.game_plan)

games=['q_learning', 'Random_strategy']


a=[['q_learning', 'Random_strategy'], ['Random_strategy','Random_strategy'],['q_learning','q_learning'],['Random_strategy','q_learning']]
for each in a:
    total_games = []
    player1_wins = []
    player2_wins = []
    draw_game = []
    total_games = 1000
    p1_wins = 0
    p2_wins = 0
    p3_draw = 0
    for i in range(1000):

        if each[0]=='q_learning':
            q_learning = Q_learning()
            each[0]=q_learning
        if each[1]=='q_learning':
            q_learning = Q_learning()
            each[1]=q_learning

        p1 = Player(each[0], 'o')
        p2 = Player(each[1] ,'x')



        b1=Board(3)
        play_game1= Game(p1,p2,b1)
        play_game1.play_game()
        if play_game1.winner=='player1':
            p1_wins +=1
        player1_wins.append(p1_wins)
        if play_game1.winner=='player2':
            p2_wins+=1
        player2_wins.append(p2_wins)
        if play_game1.winner=='draw':
            p3_draw+=1
        draw_game.append(p3_draw)


    dict={}
    dict["player1_wins"]= player1_wins
    dict['p2']= player2_wins
    dict['p3']= draw_game
    dict['games']=[x for x in range(1,1001)]
    df= pd.DataFrame(dict)

    plt.bar( [1],[p1_wins], color='green')
    plt.bar([2],[p2_wins], color='yellow')
    plt.bar([3],[p3_draw], color='crimson')
    plt.xlabel('1= {}; 2= {}'.format(p1.game_plan,p2.game_plan),color='green' )
    plt.ylabel('Number of games won by each player',color='orange')
    plt.show()

    game_statistics(player1_wins, player2_wins, draw_game, total_games, p1 ,p2)







