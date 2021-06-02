# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 10:26:30 2020

@author: jakei
"""

import CABO as cabo
Scores = [[],[]]
def game():
    cabo.deal()
    for i in range(20):
        if cabo.PlayerCards[0] != [] or cabo.PlayerCards[1] !=0:
            cabo.turn()
            Scores[0].append(0)
            Scores[1].append(cabo.PlayerCards[1])
        if cabo.PlayerCards[0] == []:
            print("Player 1 wins after",i,"turns.")
            break
        if cabo.PlayerCards[1] == []:
            print("Player 2 wins after",i,"turns.")
            Scores[1].append(0)
            Scores[0].append(cabo.PlayerCards[0])
            break
    print("Player 1's final score is",sum(cabo.PlayerCards[0]),"and Player 2's score is",sum(cabo.PlayerCards[1]))
    Scores[0].append(cabo.PlayerCards[0])
    Scores[1].append(cabo.PlayerCards[1])


def scores():
    for n in range(100):
        game()
        global Deck
        Deck = [0,0,0,0,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11,12,12,12,12,13,13,-1,-1]
        global PlayerCards
        PlayerCards = [[],[]]
        global PlayerUnknownCards
        PlayerUnknownCards = [[],[],[],[]]
        global PlayerKnownCards
        PlayerKnownCards = [[],[],[],[]]