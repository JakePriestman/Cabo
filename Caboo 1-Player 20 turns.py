    # -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 14:09:49 2019

@author: jakei
"""

import random as rand
import time as time


Deck = [0,0,0,0,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11,12,12,12,12,13,13,-1,-1]
PlayerCards = []
PlayerKnownCards = []
PlayerUnknownCards = []

Scores = []
Scoreses = []

def deal(Deck):
    rand.seed(time.time())
    rand.shuffle(Deck)
    PlayerCards.append(Deck[51])
    PlayerCards.append(Deck[50])
    PlayerCards.append(Deck[49])
    PlayerCards.append(Deck[48])
    PlayerKnownCards.append(Deck[49])
    PlayerKnownCards.append(Deck[48])
    PlayerUnknownCards.append(Deck[51])
    PlayerUnknownCards.append(Deck[50])
    del Deck[-1]
    del Deck[-1]
    del Deck[-1]
    del Deck[-1]
    print("Your known cards are",PlayerKnownCards)

def turn():
    if reducescore():
        del Deck[-1]
        return
    else:
        if snap():
            del Deck[-1]
            return
        else:
            if lookatown():
                del Deck[-1]
                return
            else:
                print(Deck[-1])
                del Deck[-1]
        
        

def reducescore():
    for i in range(len(PlayerKnownCards)):
        if Deck[-1] < PlayerKnownCards[i]:
            print(Deck[-1])
            PlayerCards.remove(PlayerKnownCards[i])
            del PlayerKnownCards[i]
            PlayerKnownCards.append(Deck[-1])
            PlayerCards.append(Deck[-1])
            print("Your known cards are now",PlayerKnownCards,"you have",len(PlayerCards),"cards left")
            return True
        break
    else:
        return False
    

def lookatown():
    if Deck[-1] == 7 or Deck[-1] == 8:
        if len(PlayerUnknownCards) != 0:
            print(Deck[-1])
            PlayerKnownCards.append(PlayerUnknownCards[-1])
            del PlayerUnknownCards[-1]
            print("Your known cards are now",PlayerKnownCards,"you have",len(PlayerCards),"cards left")
        return True
    else:
        return False

def snap():
    for i in range(len(PlayerKnownCards)):
        if Deck[-1] == PlayerKnownCards[i]:
            print(Deck[-1])
            PlayerCards.remove(PlayerKnownCards[i])
            del PlayerKnownCards[i]
            print("Your known cards are now",PlayerKnownCards,"you have",len(PlayerCards),"cards left")
            return True
        break
    else:
        return False

def cabo():
    deal(Deck)
    for i in range(20):
        if PlayerCards != []:
            turn()
        else:
            print("You got rid of all your cards in",i,"Turns! Your score is 0!")
            Scores.append(0)
            break
    print("Your score after 20 turns is",sum(PlayerCards))
    Scores.append(sum(PlayerCards))
    

def scores():
    for j in range(100):
        cabo()
        global Deck
        Deck = [0,0,0,0,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11,12,12,12,12,13,13,-1,-1]
        global PlayerCards
        PlayerCards = []
        global PlayerUnknownCards
        PlayerUnknownCards = []
        global PlayerKnownCards
        PlayerKnownCards = []