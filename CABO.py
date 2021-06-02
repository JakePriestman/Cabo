# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 14:09:49 2019

@author: jakei
"""

import random as rand
import time

Deck = [0,0,0,0,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11,12,12,12,12,13,13,-1,-1]
PlayerCards = [[],[]]
PlayerKnownCards = [[],[],[],[]]
PlayerUnknownCards = [[],[],[],[]]
Scores = [[],[]]
MeanScores = [[],[]]


def deal():
    rand.seed(time.time())
    rand.shuffle(Deck)
    for i in range(8):
        if i % 2 == 0:
            PlayerCards[0].append(Deck[-1])
            del Deck[-1]
        if i % 2 != 0:
            PlayerCards[1].append(Deck[-1])
            del Deck[-1]
    PlayerKnownCards[0].append(PlayerCards[0][-1])
    PlayerKnownCards[0].append(PlayerCards[0][-2])
    PlayerKnownCards[1].append(PlayerCards[1][-1])
    PlayerKnownCards[1].append(PlayerCards[1][-2])
    PlayerUnknownCards[0].append(PlayerCards[0][0])
    PlayerUnknownCards[0].append(PlayerCards[0][1])
    PlayerUnknownCards[1].append(PlayerCards[1][0])
    PlayerUnknownCards[1].append(PlayerCards[1][1])
    PlayerUnknownCards[3].append(PlayerCards[0][0])
    PlayerUnknownCards[3].append(PlayerCards[0][1])
    PlayerUnknownCards[3].append(PlayerCards[0][2])
    PlayerUnknownCards[3].append(PlayerCards[0][3])
    PlayerUnknownCards[2].append(PlayerCards[1][0])
    PlayerUnknownCards[2].append(PlayerCards[1][1])
    PlayerUnknownCards[2].append(PlayerCards[1][2])
    PlayerUnknownCards[2].append(PlayerCards[1][3])
    print("Player 1's known cards are",PlayerKnownCards[0])
    print("Player 2's known cards are", PlayerKnownCards[1])

def turn():
    for i in range(2):
        for j in range(len(PlayerKnownCards[i])):
            if lookatanothers(i,j):
                del Deck[-1]
                break
            else:
                if blindswap(i,j):
                    del Deck[-1]
                    break
                else:
                    if lookswap(i):
                        del Deck[-1]
                        break
                    else:
                        if reducescore(i,j):
                            del Deck[-1]
                            break
                        else:
                            if snap(i,j):
                                del Deck[-1]
                                break
                            else:
                                if lookatown(i,j):
                                    del Deck[-1]
                                    break
        else:
            print(Deck[-1])
            del Deck[-1]
                            
            
            
def snap(i,j): #Snap Check
        if Deck[-1] == PlayerKnownCards[i][j]:
            print(Deck[-1])
            PlayerCards[i].remove(PlayerKnownCards[i][j])
            if i % 2 == 0:
                if PlayerUnknownCards[i+3].count(Deck[-1]) == 0:
                    PlayerKnownCards[i+3].remove(Deck[-1])
                    del PlayerKnownCards[i][j]
                    print("Player",i+1,"'s known cards are",PlayerKnownCards[i],"you have",len(PlayerCards[i]),"cards left")
                    return True
                if PlayerKnownCards[i+3].count(Deck[-1]) == 0:
                    PlayerUnknownCards[i+3].remove(Deck[-1])
                    del PlayerKnownCards[i][j]
                    print("Player",i+1,"'s known cards are",PlayerKnownCards[i],"you have",len(PlayerCards[i]),"cards left")
                    return True
                else:
                    PlayerKnownCards[i+3].remove(Deck[-1])
                    PlayerUnknownCards[i+3].append(Deck[-1])
                    del PlayerKnownCards[i][j]
                    print("Player",i+1,"'s known cards are",PlayerKnownCards[i],"you have",len(PlayerCards[i]),"cards left")
                    return True
            if i % 2 != 0:
                if PlayerUnknownCards[i+1].count(Deck[-1]) == 0:
                    PlayerKnownCards[i+1].remove(Deck[-1])
                    del PlayerKnownCards[i][j]
                    print("Player",i+1,"'s known cards are",PlayerKnownCards[i],"you have",len(PlayerCards[i]),"cards left")
                    return True
                if PlayerKnownCards[i+1].count(Deck[-1]) == 0:
                    PlayerUnknownCards[i+1].remove(Deck[-1])
                    del PlayerKnownCards[i][j]
                    print("Player",i+1,"'s known cards are",PlayerKnownCards[i],"you have",len(PlayerCards[i]),"cards left")
                    return True
                else:
                    PlayerKnownCards[i+1].remove(Deck[-1])
                    del PlayerKnownCards[i][j]
                    print("Player",i+1,"'s known cards are",PlayerKnownCards[i],"you have",len(PlayerCards[i]),"cards left")
                    return True
        else:
            return False


def reducescore(i,j): #Reduce Score Check
        if Deck[-1] < PlayerKnownCards[i][j]:
            print(Deck[-1])
            PlayerCards[i].remove(PlayerKnownCards[i][j])
            if i % 2 == 0:
                if PlayerUnknownCards[3].count(PlayerKnownCards[i][j]) == 0:
                    PlayerKnownCards[3].remove(PlayerKnownCards[i][j])
                    PlayerUnknownCards[3].append(Deck[-1])
                    del PlayerKnownCards[i][j]
                    PlayerKnownCards[i].append(Deck[-1])
                    PlayerCards[i].append(Deck[-1])
                    print("Player",i+1,"'s known cards are",PlayerKnownCards[i],"you have",len(PlayerCards[i]),"cards left")
                    return True
                if PlayerKnownCards[3].count(PlayerKnownCards[i][j]) == 0:
                    PlayerUnknownCards[3].remove(PlayerKnownCards[i][j])
                    PlayerUnknownCards[3].append(Deck[-1])
                    del PlayerKnownCards[i][j]
                    PlayerKnownCards[i].append(Deck[-1])
                    PlayerCards[i].append(Deck[-1])
                    print("Player",i+1,"'s known cards are",PlayerKnownCards[i],"you have",len(PlayerCards[i]),"cards left")
                    return True
                else:
                    PlayerKnownCards[3].remove(PlayerKnownCards[i][j])
                    PlayerUnknownCards[3].append(Deck[-1])
                    del PlayerKnownCards[i][j]
                    PlayerKnownCards[i].append(Deck[-1])
                    PlayerCards[i].append(Deck[-1])
                    print("Player",i+1,"'s known cards are",PlayerKnownCards[i],"you have",len(PlayerCards[i]),"cards left")
                    return True
            if i % 2 != 0:
                if PlayerUnknownCards[2].count(PlayerKnownCards[i][j]) == 0:
                    PlayerKnownCards[2].remove(PlayerKnownCards[i][j])
                    PlayerUnknownCards[2].append(Deck[-1])
                    del PlayerKnownCards[i][j]
                    PlayerKnownCards[i].append(Deck[-1])
                    PlayerCards[i].append(Deck[-1])
                    print("Player",i+1,"'s known cards are",PlayerKnownCards[i],"you have",len(PlayerCards[i]),"cards left")
                    return True
                if PlayerKnownCards[2].count(PlayerKnownCards[i][j]) == 0:
                    PlayerUnknownCards[2].remove(PlayerKnownCards[i][j])
                    PlayerUnknownCards[2].append(Deck[-1])
                    del PlayerKnownCards[i][j]
                    PlayerKnownCards[i].append(Deck[-1])
                    PlayerCards[i].append(Deck[-1])
                    print("Player",i+1,"'s known cards are",PlayerKnownCards[i],"you have",len(PlayerCards[i]),"cards left")
                    return True
                else:
                    PlayerKnownCards[i+1].remove(PlayerKnownCards[i][j])
                    PlayerUnknownCards[i+1].append(Deck[-1])
                    del PlayerKnownCards[i][j]
                    PlayerKnownCards[i].append(Deck[-1])
                    PlayerCards[i].append(Deck[-1])
                    print("Player",i+1,"'s known cards are",PlayerKnownCards[i],"you have",len(PlayerCards[i]),"cards left")
                    return True
        else:
            return False
    

def lookatown(i,j): #Look at own Special Cards
        if Deck[-1] == 7 or Deck[-1] == 8:
            '''if Deck[-1] == PlayerKnownCards[i][j] and len(PlayerUnknownCards[i]) == 0:
                print(Deck[-1])
                PlayerCards[i].remove(PlayerKnownCards[i][j])
                del PlayerKnownCards[i][j]
                print("Player",i+1,"'s known cards are",PlayerKnownCards[i],"you have",len(PlayerCards[i]),"cards left")
                return True'''
            if len(PlayerUnknownCards[i]) != 0:
                print (Deck[-1])
                PlayerKnownCards[i].append(PlayerUnknownCards[i][-1])
                del PlayerUnknownCards[i][-1]
                print("Player",i+1,"'s known cards are",PlayerKnownCards[i],"you have",len(PlayerCards[i]),"cards left")
                return True
        else:
            return False


def lookatanothers(i,j): #Look at another's Special Cards
        if Deck[-1] == 9 or Deck[-1] == 10:
            '''if Deck[-1] == PlayerKnownCards[i][j] and len(PlayerUnknownCards[i+2])== 0:
                print(Deck[-1])
                PlayerCards[i].remove(PlayerKnownCards[i][j])
                del PlayerKnownCards[i][j]
                print("Player",i+1,"'s known cards are",PlayerKnownCards[i],"you have",len(PlayerCards[i]),"cards left")
                return True'''
            if len(PlayerUnknownCards[i+2]) != 0:
                print(Deck[-1])
                PlayerKnownCards[i+2].append(PlayerUnknownCards[i+2][-1])
                del PlayerUnknownCards[i+2][-1]
                print("Player",i+1,"knows the other player has",PlayerKnownCards[i+2])
                return True
        else:
            return False

def blindswap(i,j): #Blind Swap Special Cards
        if Deck[-1] == 11 or Deck[-1] == 12:
            if PlayerKnownCards[i+2] != []:
                for n in range(len(PlayerKnownCards[i+2])):
                    if PlayerKnownCards[i+2][n] < PlayerKnownCards[i][j]:
                        print(Deck[-1])
                        PlayerCards[i].remove(PlayerKnownCards[i][j])
                        PlayerCards[i].append(PlayerKnownCards[i+2][n])
                        PlayerKnownCards[i].append(PlayerKnownCards[i+2][n])
                        PlayerKnownCards[i+2].append(PlayerKnownCards[i][j])
                        if i % 2 == 0: #Player 1
                            if PlayerUnknownCards[i+1].count(PlayerKnownCards[i+2][n]) == 0:
                                PlayerKnownCards[i+1].remove(PlayerKnownCards[i+2][n])
                                PlayerUnknownCards[i+1].append(PlayerKnownCards[i][j])
                                if PlayerUnknownCards[i+3].count(PlayerKnownCards[i][j]) == 0:
                                    PlayerKnownCards[i+3].remove(PlayerKnownCards[i][j])
                                    PlayerUnknownCards[i+3].append(PlayerKnownCards[i+2][n])
                                    PlayerCards[i+1].remove(PlayerKnownCards[i+2][n])
                                    PlayerCards[i+1].append(PlayerKnownCards[i][j])
                                    del PlayerKnownCards[i+2][n]
                                    del PlayerKnownCards[i][j]
                                    print("Player",i+1,"swapped so their known cards are now",PlayerKnownCards[i],"you have",len(PlayerCards[i]),"cards left")
                                    return True
                                if PlayerKnownCards[i+3].count(PlayerKnownCards[i][j]) == 0:
                                    PlayerUnknownCards[i+3].remove(PlayerKnownCards[i][j])
                                    PlayerUnknownCards[i+3].append(PlayerKnownCards[i+2][n])
                                    PlayerCards[i+1].remove(PlayerKnownCards[i+2][n])
                                    PlayerCards[i+1].append(PlayerKnownCards[i][j])
                                    del PlayerKnownCards[i+2][n]
                                    del PlayerKnownCards[i][j]
                                    print("Player",i+1,"swapped so their known cards are now",PlayerKnownCards[i],"you have",len(PlayerCards[i]),"cards left")
                                    return True
                                else:
                                    PlayerKnownCards[i+3].remove(PlayerKnownCards[i][j])
                                    PlayerUnknownCards[i+3].append(PlayerKnownCards[i+2][n])
                                    PlayerCards[i+1].remove(PlayerKnownCards[i+2][n])
                                    PlayerCards[i+1].append(PlayerKnownCards[i][j])
                                    del PlayerKnownCards[i+2][n]
                                    del PlayerKnownCards[i][j]
                                    print("Player",i+1,"swapped so their known cards are now",PlayerKnownCards[i],"you have",len(PlayerCards[i]),"cards left")
                                    return True
                            if PlayerKnownCards[i+1].count(PlayerKnownCards[i+2][n]) == 0:
                                PlayerUnknownCards[i+1].remove(PlayerKnownCards[i+2][n])
                                PlayerUnknownCards[i+1].append(PlayerKnownCards[i][j])
                                if PlayerUnknownCards[i+3].count(PlayerKnownCards[i][j]) == 0:
                                    PlayerKnownCards[i+3].remove(PlayerKnownCards[i][j])
                                    PlayerUnknownCards[i+3].append(PlayerKnownCards[i+2][n])
                                    PlayerCards[i+1].remove(PlayerKnownCards[i+2][n])
                                    PlayerCards[i+1].append(PlayerKnownCards[i][j])
                                    del PlayerKnownCards[i+2][n]
                                    del PlayerKnownCards[i][j]
                                    print("Player",i+1,"swapped so their known cards are now",PlayerKnownCards[i],"you have",len(PlayerCards[i]),"cards left")
                                    return True
                                if PlayerKnownCards[i+3].count(PlayerKnownCards[i][j]) == 0:
                                    PlayerUnknownCards[i+3].remove(PlayerKnownCards[i][j])
                                    PlayerUnknownCards[i+3].append(PlayerKnownCards[i+2][n])
                                    PlayerCards[i+1].remove(PlayerKnownCards[i+2][n])
                                    PlayerCards[i+1].append(PlayerKnownCards[i][j])
                                    del PlayerKnownCards[i+2][n]
                                    del PlayerKnownCards[i][j]
                                    print("Player",i+1,"swapped so their known cards are now",PlayerKnownCards[i],"you have",len(PlayerCards[i]),"cards left")
                                    return True
                                else:
                                    PlayerKnownCards[i+3].remove(PlayerKnownCards[i][j])
                                    PlayerUnknownCards[i+3].append(PlayerKnownCards[i+2][n])
                                    PlayerCards[i+1].remove(PlayerKnownCards[i+2][n])
                                    PlayerCards[i+1].append(PlayerKnownCards[i][j])
                                    del PlayerKnownCards[i+2][n]
                                    del PlayerKnownCards[i][j]
                                    print("Player",i+1,"swapped so their known cards are now",PlayerKnownCards[i],"you have",len(PlayerCards[i]),"cards left")
                                    return True
                            else:
                                PlayerKnownCards[i+1].remove(PlayerKnownCards[i+2][n])
                                PlayerUnknownCards[i+1].append(PlayerKnownCards[i][j])
                                if PlayerUnknownCards[i+3].count(PlayerKnownCards[i][j]) == 0:
                                    PlayerKnownCards[i+3].remove(PlayerKnownCards[i][j])
                                    PlayerUnknownCards[i+3].append(PlayerKnownCards[i+2][n])
                                    PlayerCards[i+1].remove(PlayerKnownCards[i+2][n])
                                    PlayerCards[i+1].append(PlayerKnownCards[i][j])
                                    del PlayerKnownCards[i+2][n]
                                    del PlayerKnownCards[i][j]
                                    print("Player",i+1,"swapped so their known cards are now",PlayerKnownCards[i],"you have",len(PlayerCards[i]),"cards left")
                                    return True
                                if PlayerKnownCards[i+3].count(PlayerKnownCards[i][j]) == 0:
                                    PlayerUnknownCards[i+3].remove(PlayerKnownCards[i][j])
                                    PlayerUnknownCards[i+3].append(PlayerKnownCards[i+2][n])
                                    PlayerCards[i+1].remove(PlayerKnownCards[i+2][n])
                                    PlayerCards[i+1].append(PlayerKnownCards[i][j])
                                    del PlayerKnownCards[i+2][n]
                                    del PlayerKnownCards[i][j]
                                    print("Player",i+1,"swapped so their known cards are now",PlayerKnownCards[i],"you have",len(PlayerCards[i]),"cards left")
                                    return True
                                else:
                                    PlayerKnownCards[i+3].remove(PlayerKnownCards[i][j])
                                    PlayerUnknownCards[i+3].append(PlayerKnownCards[i+2][n])
                                    PlayerCards[i+1].remove(PlayerKnownCards[i+2][n])
                                    PlayerCards[i+1].append(PlayerKnownCards[i][j])
                                    del PlayerKnownCards[i+2][n]
                                    del PlayerKnownCards[i][j]
                                    print("Player",i+1,"swapped so their known cards are now",PlayerKnownCards[i],"you have",len(PlayerCards[i]),"cards left")
                                    return True
                            break
                        if i % 2 != 0: #Player 2
                            if PlayerUnknownCards[i-1].count(PlayerKnownCards[i+2][n]) == 0:
                                PlayerKnownCards[0].remove(PlayerKnownCards[i+2][n])
                                PlayerUnknownCards[i-1].append(PlayerKnownCards[i][j])
                                if PlayerUnknownCards[i+1].count(PlayerKnownCards[i][j]) == 0:
                                    PlayerKnownCards[i+1].remove(PlayerKnownCards[i][j])
                                    PlayerUnknownCards[i+1].append(PlayerKnownCards[i+2][n])
                                    PlayerCards[i-1].remove(PlayerKnownCards[i+2][n])
                                    PlayerCards[i-1].append(PlayerKnownCards[i][j])
                                    del PlayerKnownCards[i+2][n]
                                    del PlayerKnownCards[i][j]
                                    print("Player",i+1,"swapped so their known cards are now",PlayerKnownCards[i],"you have",len(PlayerCards[i]),"cards left")
                                    return True
                                if PlayerKnownCards[i+1].count(PlayerKnownCards[i][j]) == 0:
                                    PlayerUnknownCards[i+1].remove(PlayerKnownCards[i][j])
                                    PlayerUnknownCards[i+1].append(PlayerKnownCards[i+2][n])
                                    PlayerCards[i-1].remove(PlayerKnownCards[i+2][n])
                                    PlayerCards[i-1].append(PlayerKnownCards[i][j])
                                    del PlayerKnownCards[i+2][n]
                                    del PlayerKnownCards[i][j]
                                    print("Player",i+1,"swapped so their known cards are now",PlayerKnownCards[i],"you have",len(PlayerCards[i]),"cards left")
                                    return True
                                else:
                                    PlayerKnownCards[i+1].remove(PlayerKnownCards[i][j])
                                    PlayerUnknownCards[i+1].append(PlayerKnownCards[i+2][n])
                                    PlayerCards[i-1].remove(PlayerKnownCards[i+2][n])
                                    PlayerCards[i-1].append(PlayerKnownCards[i][j])
                                    del PlayerKnownCards[i+2][n]
                                    del PlayerKnownCards[i][j]
                                    print("Player",i+1,"swapped so their known cards are now",PlayerKnownCards[i],"you have",len(PlayerCards[i]),"cards left")
                                    return True
                            if PlayerKnownCards[i-1].count(PlayerKnownCards[i+2][n]) == 0:
                                PlayerUnknownCards[i-1].remove(PlayerKnownCards[i+2][n])
                                PlayerUnknownCards[i-1].append(PlayerKnownCards[i][j])
                                if PlayerUnknownCards[i+1].count(PlayerKnownCards[i][j]) == 0:
                                    PlayerKnownCards[i+1].remove(PlayerKnownCards[i][j])
                                    PlayerUnknownCards[i+1].append(PlayerKnownCards[i+2][n])
                                    PlayerCards[i-1].remove(PlayerKnownCards[i+2][n])
                                    PlayerCards[i-1].append(PlayerKnownCards[i][j])
                                    del PlayerKnownCards[i+2][n]
                                    del PlayerKnownCards[i][j]
                                    print("Player",i+1,"swapped so their known cards are now",PlayerKnownCards[i],"you have",len(PlayerCards[i]),"cards left")
                                    return True
                                if PlayerKnownCards[i+1].count(PlayerKnownCards[i][j]) == 0:
                                    PlayerUnknownCards[i+1].remove(PlayerKnownCards[i][j])
                                    PlayerUnknownCards[i+1].append(PlayerKnownCards[i+2][n])
                                    PlayerCards[i-1].remove(PlayerKnownCards[i+2][n])
                                    PlayerCards[i-1].append(PlayerKnownCards[i][j])
                                    del PlayerKnownCards[i+2][n]
                                    del PlayerKnownCards[i][j]
                                    print("Player",i+1,"swapped so their known cards are now",PlayerKnownCards[i],"you have",len(PlayerCards[i]),"cards left")
                                    return True
                                else:
                                    PlayerKnownCards[i+1].remove(PlayerKnownCards[i][j])
                                    PlayerUnknownCards[i+1].append(PlayerKnownCards[i+2][n])
                                    PlayerCards[i-1].remove(PlayerKnownCards[i+2][n])
                                    PlayerCards[i-1].append(PlayerKnownCards[i][j])
                                    del PlayerKnownCards[i+2][n]
                                    del PlayerKnownCards[i][j]
                                    print("Player",i+1,"swapped so their known cards are now",PlayerKnownCards[i],"you have",len(PlayerCards[i]),"cards left")
                                    return True
                            else:
                                PlayerKnownCards[i-1].remove(PlayerKnownCards[i+2][n])
                                PlayerUnknownCards[i-1].append(PlayerKnownCards[i][j])
                                if PlayerUnknownCards[i+1].count(PlayerKnownCards[i][j]) == 0:
                                    PlayerKnownCards[i+1].remove(PlayerKnownCards[i][j])
                                    PlayerUnknownCards[i+1].append(PlayerKnownCards[i+2][n])
                                    PlayerCards[i-1].remove(PlayerKnownCards[i+2][n])
                                    PlayerCards[i-1].append(PlayerKnownCards[i][j])
                                    del PlayerKnownCards[i+2][n]
                                    del PlayerKnownCards[i][j]
                                    print("Player",i+1,"swapped so their known cards are now",PlayerKnownCards[i],"you have",len(PlayerCards[i]),"cards left")
                                    return True
                                if PlayerKnownCards[i+1].count(PlayerKnownCards[i][j]) == 0:
                                    PlayerUnknownCards[i+1].remove(PlayerKnownCards[i][j])
                                    PlayerUnknownCards[i+1].append(PlayerKnownCards[i+2][n])
                                    PlayerCards[i-1].remove(PlayerKnownCards[i+2][n])
                                    PlayerCards[i-1].append(PlayerKnownCards[i][j])
                                    del PlayerKnownCards[i+2][n]
                                    del PlayerKnownCards[i][j]
                                    print("Player",i+1,"swapped so their known cards are now",PlayerKnownCards[i],"you have",len(PlayerCards[i]),"cards left")
                                    return True
                                else:
                                    PlayerKnownCards[i+1].remove(PlayerKnownCards[i][j])
                                    PlayerUnknownCards[i+1].append(PlayerKnownCards[i+2][n])
                                    PlayerCards[i-1].remove(PlayerKnownCards[i+2][n])
                                    PlayerCards[i-1].append(PlayerKnownCards[i][j])
                                    del PlayerKnownCards[i+2][n]
                                    del PlayerKnownCards[i][j]
                                    print("Player",i+1,"swapped so their known cards are now",PlayerKnownCards[i],"you have",len(PlayerCards[i]),"cards left")
                                    return True
                            break
            else:
                return False

def lookswap(i): #Look Swap Special Card
    if Deck[-1] == 13:
        if len(PlayerUnknownCards[i+2]) != 0:
            if len(PlayerUnknownCards[i]) != 0:
                PlayerKnownCards[i+2].append(PlayerUnknownCards[i+2][-1])
                PlayerKnownCards[i].append(PlayerUnknownCards[i][-1])
                del PlayerUnknownCards[i+2][-1]
                del PlayerUnknownCards[i][-1]
                if PlayerKnownCards[i+2][-1] < PlayerKnownCards[i][-1]:
                    print(Deck[-1])
                    PlayerCards[i].remove(PlayerKnownCards[i][-1])
                    PlayerCards[i].append(PlayerKnownCards[i+2][-1])
                    PlayerKnownCards[i].append(PlayerKnownCards[i+2][-1])
                    PlayerKnownCards[i+2].append(PlayerKnownCards[i][-2])
                    if i % 2 == 0: # Player 1
                        if PlayerUnknownCards[i+1].count(PlayerKnownCards[i][-1]) == 0:
                            PlayerKnownCards[i+1].remove(PlayerKnownCards[i][-1])
                            PlayerUnknownCards[i+1].append(PlayerKnownCards[i][-2])
                            if PlayerUnknownCards[i+3].count(PlayerKnownCards[i][-2]) == 0:
                                PlayerKnownCards[i+3].remove(PlayerKnownCards[i][-2])
                                PlayerUnknownCards[i+3].append(PlayerKnownCards[i][-1])
                                PlayerCards[i+1].remove(PlayerKnownCards[i][-1])
                                PlayerCards[i+1].append(PlayerKnownCards[i][-2])
                                del PlayerKnownCards[i+2][-2]
                                del PlayerKnownCards[i][-2]
                                print("Player",i+1,"swapped a",PlayerKnownCards[i+2][-1],"for a",PlayerKnownCards[i][-1])
                                print("Player",i+1,"'s known cards are now",PlayerKnownCards[i],"you have",len(PlayerCards[i]),"cards left")
                                return True
                            if PlayerKnownCards[i+3].count(PlayerKnownCards[i][-2]) == 0:
                                PlayerUnknownCards[i+3].remove(PlayerKnownCards[i][-2])
                                PlayerUnknownCards[i+3].append(PlayerKnownCards[i][-1])
                                PlayerCards[i+1].remove(PlayerKnownCards[i][-1])
                                PlayerCards[i+1].append(PlayerKnownCards[i][-2])
                                del PlayerKnownCards[i+2][-2]
                                del PlayerKnownCards[i][-2]
                                print("Player",i+1,"swapped a",PlayerKnownCards[i+2][-1],"for a",PlayerKnownCards[i][-1])
                                print("Player",i+1,"'s known cards are now",PlayerKnownCards[i],"you have",len(PlayerCards[i]),"cards left")
                                return True
                            else: 
                                PlayerKnownCards[i+3].remove(PlayerKnownCards[i][-2])
                                PlayerUnknownCards[i+3].append(PlayerKnownCards[i][-1])
                                PlayerCards[i+1].remove(PlayerKnownCards[i][-1])
                                PlayerCards[i+1].append(PlayerKnownCards[i][-2])
                                del PlayerKnownCards[i+2][-2]
                                del PlayerKnownCards[i][-2]
                                print("Player",i+1,"swapped a",PlayerKnownCards[i+2][-1],"for a",PlayerKnownCards[i][-1])
                                print("Player",i+1,"'s known cards are now",PlayerKnownCards[i],"you have",len(PlayerCards[i]),"cards left")
                                return True
                        if PlayerKnownCards[i+1].count(PlayerKnownCards[i][-1]) == 0:
                            PlayerUnknownCards[i+1].remove(PlayerKnownCards[i][-1])
                            PlayerUnknownCards[i+1].append(PlayerKnownCards[i][-2])
                            if PlayerUnknownCards[i+3].count(PlayerKnownCards[i][-2]) == 0:
                                PlayerKnownCards[i+3].remove(PlayerKnownCards[i][-2])
                                PlayerUnknownCards[i+3].append(PlayerKnownCards[i][-1])
                                PlayerCards[i+1].remove(PlayerKnownCards[i][-1])
                                PlayerCards[i+1].append(PlayerKnownCards[i][-2])
                                del PlayerKnownCards[i+2][-2]
                                del PlayerKnownCards[i][-2]
                                print("Player",i+1,"swapped a",PlayerKnownCards[i+2][-1],"for a",PlayerKnownCards[i][-1])
                                print("Player",i+1,"'s known cards are now",PlayerKnownCards[i],"you have",len(PlayerCards[i]),"cards left")
                                return True
                            if PlayerKnownCards[i+3].count(PlayerKnownCards[i][-2]) == 0:
                                PlayerUnknownCards[i+3].remove(PlayerKnownCards[i][-2])
                                PlayerUnknownCards[i+3].append(PlayerKnownCards[i][-1])
                                PlayerCards[i+1].remove(PlayerKnownCards[i][-1])
                                PlayerCards[i+1].append(PlayerKnownCards[i][-2])
                                del PlayerKnownCards[i+2][-2]
                                del PlayerKnownCards[i][-2]
                                print("Player",i+1,"swapped a",PlayerKnownCards[i+2][-1],"for a",PlayerKnownCards[i][-1])
                                print("Player",i+1,"'s known cards are now",PlayerKnownCards[i],"you have",len(PlayerCards[i]),"cards left")
                                return True
                            else: 
                                PlayerKnownCards[i+3].remove(PlayerKnownCards[i][-2])
                                PlayerUnknownCards[i+3].append(PlayerKnownCards[i][-1])
                                PlayerCards[i+1].remove(PlayerKnownCards[i][-1])
                                PlayerCards[i+1].append(PlayerKnownCards[i][-2])
                                del PlayerKnownCards[i+2][-2]
                                del PlayerKnownCards[i][-2]
                                print("Player",i+1,"swapped a",PlayerKnownCards[i+2][-1],"for a",PlayerKnownCards[i][-1])
                                print("Player",i+1,"'s known cards are now",PlayerKnownCards[i],"you have",len(PlayerCards[i]),"cards left")
                                return True
                        else:
                            PlayerKnownCards[i+1].remove(PlayerKnownCards[i][-1])
                            PlayerUnknownCards[i+1].append(PlayerKnownCards[i][-2])
                            if PlayerUnknownCards[i+3].count(PlayerKnownCards[i][-2]) == 0:
                                PlayerKnownCards[i+3].remove(PlayerKnownCards[i][-2])
                                PlayerUnknownCards[i+3].append(PlayerKnownCards[i][-1])
                                PlayerCards[i+1].remove(PlayerKnownCards[i][-1])
                                PlayerCards[i+1].append(PlayerKnownCards[i][-2])
                                del PlayerKnownCards[i+2][-2]
                                del PlayerKnownCards[i][-2]
                                print("Player",i+1,"swapped a",PlayerKnownCards[i+2][-1],"for a",PlayerKnownCards[i][-1])
                                print("Player",i+1,"'s known cards are now",PlayerKnownCards[i],"you have",len(PlayerCards[i]),"cards left")
                                return True
                            if PlayerKnownCards[i+3].count(PlayerKnownCards[i][-2]) == 0:
                                PlayerUnknownCards[i+3].remove(PlayerKnownCards[i][-2])
                                PlayerUnknownCards[i+3].append(PlayerKnownCards[i][-1])
                                PlayerCards[i+1].remove(PlayerKnownCards[i][-1])
                                PlayerCards[i+1].append(PlayerKnownCards[i][-2])
                                del PlayerKnownCards[i+2][-2]
                                del PlayerKnownCards[i][-2]
                                print("Player",i+1,"swapped a",PlayerKnownCards[i+2][-1],"for a",PlayerKnownCards[i][-1])
                                print("Player",i+1,"'s known cards are now",PlayerKnownCards[i],"you have",len(PlayerCards[i]),"cards left")
                                return True
                            else: 
                                PlayerKnownCards[i+3].remove(PlayerKnownCards[i][-2])
                                PlayerUnknownCards[i+3].append(PlayerKnownCards[i][-1])
                                PlayerCards[i+1].remove(PlayerKnownCards[i][-1])
                                PlayerCards[i+1].append(PlayerKnownCards[i][-2])
                                del PlayerKnownCards[i+2][-2]
                                del PlayerKnownCards[i][-2]
                                print("Player",i+1,"swapped a",PlayerKnownCards[i+2][-1],"for a",PlayerKnownCards[i][-1])
                                print("Player",i+1,"'s known cards are now",PlayerKnownCards[i],"you have",len(PlayerCards[i]),"cards left")
                                return True
                    if i % 2 != 0: #Player 2
                        if PlayerUnknownCards[i-1].count(PlayerKnownCards[i][-1]) == 0:
                            PlayerKnownCards[i-1].remove(PlayerKnownCards[i][-1])
                            PlayerUnknownCards[i-1].append(PlayerKnownCards[i][-2])
                            if PlayerUnknownCards[i+1].count(PlayerKnownCards[i][-2]) == 0:
                                PlayerKnownCards[i+1].remove(PlayerKnownCards[i][-2])
                                PlayerUnknownCards[i+1].append(PlayerKnownCards[i][-1])
                                PlayerCards[i-1].remove(PlayerKnownCards[i][-1])
                                PlayerCards[i-1].append(PlayerKnownCards[i][-2])
                                del PlayerKnownCards[i+2][-2]
                                del PlayerKnownCards[i][-2]
                                print("Player",i+1,"swapped a",PlayerKnownCards[i+2][-1],"for a",PlayerKnownCards[i][-1])
                                print("Player",i+1,"'s known cards are now",PlayerKnownCards[i],"you have",len(PlayerCards[i]),"cards left")
                                return True
                            if PlayerKnownCards[i+1].count(PlayerKnownCards[i][-2]) == 0:
                                PlayerUnknownCards[i+1].remove(PlayerKnownCards[i][-2])
                                PlayerUnknownCards[i+1].append(PlayerKnownCards[i][-1])
                                PlayerCards[i-1].remove(PlayerKnownCards[i][-1])
                                PlayerCards[i-1].append(PlayerKnownCards[i][-2])
                                del PlayerKnownCards[i+2][-2]
                                del PlayerKnownCards[i][-2]
                                print("Player",i+1,"swapped a",PlayerKnownCards[i+2][-1],"for a",PlayerKnownCards[i][-1])
                                print("Player",i+1,"'s known cards are now",PlayerKnownCards[i],"you have",len(PlayerCards[i]),"cards left")
                                return True
                            else: 
                                PlayerKnownCards[i+1].remove(PlayerKnownCards[i][-2])
                                PlayerUnknownCards[i+1].append(PlayerKnownCards[i][-1])
                                PlayerCards[i-1].remove(PlayerKnownCards[i][-1])
                                PlayerCards[i-1].append(PlayerKnownCards[i][-2])
                                del PlayerKnownCards[i+2][-2]
                                del PlayerKnownCards[i][-2]
                                print("Player",i+1,"swapped a",PlayerKnownCards[i+2][-1],"for a",PlayerKnownCards[i][-1])
                                print("Player",i+1,"'s known cards are now",PlayerKnownCards[i],"you have",len(PlayerCards[i]),"cards left")
                                return True
                        if PlayerKnownCards[i-1].count(PlayerKnownCards[i][-1]) == 0:
                            PlayerUnknownCards[i-1].remove(PlayerKnownCards[i][-1])
                            PlayerUnknownCards[i-1].append(PlayerKnownCards[i][-2])
                            if PlayerUnknownCards[i+1].count(PlayerKnownCards[i][-2]) == 0:
                                PlayerKnownCards[i+1].remove(PlayerKnownCards[i][-2])
                                PlayerUnknownCards[i+1].append(PlayerKnownCards[i][-1])
                                PlayerCards[i-1].remove(PlayerKnownCards[i][-1])
                                PlayerCards[i-1].append(PlayerKnownCards[i][-2])
                                del PlayerKnownCards[i+2][-2]
                                del PlayerKnownCards[i][-2]
                                print("Player",i+1,"swapped a",PlayerKnownCards[i+2][-1],"for a",PlayerKnownCards[i][-1])
                                print("Player",i+1,"'s known cards are now",PlayerKnownCards[i],"you have",len(PlayerCards[i]),"cards left")
                                return True
                            if PlayerKnownCards[i+1].count(PlayerKnownCards[i][-2]) == 0:
                                PlayerUnknownCards[i+1].remove(PlayerKnownCards[i][-2])
                                PlayerUnknownCards[i+1].append(PlayerKnownCards[i][-1])
                                PlayerCards[i-1].remove(PlayerKnownCards[i][-1])
                                PlayerCards[i-1].append(PlayerKnownCards[i][-2])
                                del PlayerKnownCards[i+2][-2]
                                del PlayerKnownCards[i][-2]
                                print("Player",i+1,"swapped a",PlayerKnownCards[i+2][-1],"for a",PlayerKnownCards[i][-1])
                                print("Player",i+1,"'s known cards are now",PlayerKnownCards[i],"you have",len(PlayerCards[i]),"cards left")
                                return True
                            else: 
                                PlayerKnownCards[i+1].remove(PlayerKnownCards[i][-2])
                                PlayerUnknownCards[i+1].append(PlayerKnownCards[i][-1])
                                PlayerCards[i-1].remove(PlayerKnownCards[i][-1])
                                PlayerCards[i-1].append(PlayerKnownCards[i][-2])
                                del PlayerKnownCards[i+2][-2]
                                del PlayerKnownCards[i][-2]
                                print("Player",i+1,"swapped a",PlayerKnownCards[i+2][-1],"for a",PlayerKnownCards[i][-1])
                                print("Player",i+1,"'s known cards are now",PlayerKnownCards[i],"you have",len(PlayerCards[i]),"cards left")
                                return True
                        else:
                            PlayerKnownCards[i-1].remove(PlayerKnownCards[i][-1])
                            PlayerUnknownCards[i-1].append(PlayerKnownCards[i+2][-1])
                            if PlayerUnknownCards[i+1].count(PlayerKnownCards[i][-2]) == 0:
                                PlayerKnownCards[i+1].remove(PlayerKnownCards[i][-2])
                                PlayerUnknownCards[i+1].append(PlayerKnownCards[i][-1])
                                PlayerCards[i-1].remove(PlayerKnownCards[i][-1])
                                PlayerCards[i-1].append(PlayerKnownCards[i][-2])
                                del PlayerKnownCards[i+2][-2]
                                del PlayerKnownCards[i][-2]
                                print("Player",i+1,"swapped a",PlayerKnownCards[i+2][-1],"for a",PlayerKnownCards[i][-1])
                                print("Player",i+1,"'s known cards are now",PlayerKnownCards[i],"you have",len(PlayerCards[i]),"cards left")
                                return True
                            if PlayerKnownCards[i+1].count(PlayerKnownCards[i][-2]) == 0:
                                PlayerUnknownCards[i+1].remove(PlayerKnownCards[i][-2])
                                PlayerUnknownCards[i+1].append(PlayerKnownCards[i][-1])
                                PlayerCards[i-1].remove(PlayerKnownCards[i][-1])
                                PlayerCards[i-1].append(PlayerKnownCards[i][-2])
                                del PlayerKnownCards[i+2][-2]
                                del PlayerKnownCards[i][-2]
                                print("Player",i+1,"swapped a",PlayerKnownCards[i+2][-1],"for a",PlayerKnownCards[i][-1])
                                print("Player",i+1,"'s known cards are now",PlayerKnownCards[i],"you have",len(PlayerCards[i]),"cards left")
                                return True
                            else: 
                                PlayerKnownCards[i+1].remove(PlayerKnownCards[i][-2])
                                PlayerUnknownCards[i+1].append(PlayerKnownCards[i][-1])
                                PlayerCards[i-1].remove(PlayerKnownCards[i][-1])
                                PlayerCards[i-1].append(PlayerKnownCards[i][-2])
                                del PlayerKnownCards[i+2][-2]
                                del PlayerKnownCards[i][-2]
                                print("Player",i+1,"swapped a",PlayerKnownCards[i+2][-1],"for a",PlayerKnownCards[i][-1])
                                print("Player",i+1,"'s known cards are now",PlayerKnownCards[i],"you have",len(PlayerCards[i]),"cards left")
                                return True
                else:
                    print("Player",i+1,"decided not to swap")
                    print("Player",i+1,"'s known cards are",PlayerKnownCards[i])
                    return False






def game():
    deal()
    for i in range(20):
        if PlayerCards[0] != [] or PlayerCards[1] !=0:
            turn()
        if PlayerCards[0] == []:
            print("Player 1 wins after",i,"turns.")
            Scores[0].append(0)
            Scores[1].append(sum(PlayerCards[1]))
            break
        if PlayerCards[1] == []:
            print("Player 2 wins after",i,"turns.")
            Scores[1].append(0)
            Scores[0].append(sum(PlayerCards[0]))
            break
    print("Player 1's final score is",sum(PlayerCards[0]),"and Player 2's score is",sum(PlayerCards[1]))
    Scores[0].append(sum(PlayerCards[0]))
    Scores[1].append(sum(PlayerCards[1]))


def scores():
    for n in range(10):
        game()
        global Deck
        Deck = [0,0,0,0,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11,12,12,12,12,13,13,-1,-1]
        global PlayerCards
        PlayerCards = [[],[]]
        global PlayerUnknownCards
        PlayerUnknownCards = [[],[],[],[]]
        global PlayerKnownCards
        PlayerKnownCards = [[],[],[],[]]
    MeanScores[0].append(sum(Scores[0])/len(Scores[0]))
    MeanScores[1].append(sum(Scores[1])/len(Scores[1]))

def meanscores():
    for x in range(10):
        scores()
        global Scores
        Scores = [[],[]]
    