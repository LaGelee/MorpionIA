# -*- coding: utf-8 -*-

"""
Jeu du Morpion
Made by Alexandre

"""

from random import randint
from termcolor import colored
import os
import time
import sys

class Joueur():    
    def __init__(self):
        pass

    def play(self):
        while True:
            self.cmd = int(input(">"))
            if self.cmd <= 0 or self.cmd >= 10 or jeu.g[self.cmd-1] == bt or jeu.g[self.cmd-1] == jt:
                    print('Case  indisponible')
                    continue
            else:
                jeu.g[self.cmd-1] = jt
                return

class Bot():
    def __init__(self):
        self.gcopy = []

    def copyboard(self):
        self.gcopy = []
        for i in jeu.g:
            self.gcopy.append(i)

    def trywin(self):
        for i in range(9):
            if self.gcopy[i] == bt or self.gcopy[i] == jt:
                continue
            self.gcopy[i] = bt
            if jeu.checkwin(self.gcopy, bt) == True:
                jeu.g[i] = bt
                return 'Win'
            self.gcopy[i] = i+1

    def tryloose(self):
        for i in range(9):
            if self.gcopy[i] == bt or self.gcopy[i] == jt:
                continue
            self.gcopy[i] = jt
            if jeu.checkwin(self.gcopy, jt) == True:
                jeu.g[i] = bt
                return 'Loose'
            self.gcopy[i] = i+1

    def play(self):
        self.copyboard()
        if self.trywin() == "Win":
            return
        if self.tryloose() == 'Loose':
            return
        while True:
            self.r = randint(0,8)
            if jeu.g[self.r] == bt or jeu.g[self.r] == jt:
                continue  
            else :
                jeu.g[self.r] = bt
                break

class Jeu():
    def __init__(self):
        self.g = []

    def initialisation(self):
        self.choose()
        self.g = []
        for i in range(0,9):
            self.g.append(i+1)

    def grille(self):
        print('')
        print('|',self.g[0],'|',self.g[1],'|',self.g[2],'|')
        print('|',self.g[3],'|',self.g[4],'|',self.g[5],'|')
        print('|',self.g[6],'|',self.g[7],'|',self.g[8],'|')
        print('')
    
    def checkwin(self, gr, player):
        if gr[0] == player and gr[1] == player and gr[2] == player:
            return True
        elif gr[3] == player and gr[4] == player and gr[5] == player:
            return True
        elif gr[6] == player and gr[7] == player and gr[8] == player:
            return True
        elif gr[0] == player and gr[3] == player and gr[6] == player:
            return True
        elif gr[1] == player and gr[4] == player and gr[7] == player:
            return True
        elif gr[2] == player and gr[5] == player and gr[8] == player:
            return True
        elif gr[0] == player and gr[4] == player and gr[8] == player:
            return True
        elif gr[2] == player and gr[4] == player and gr[6] == player:
            return True

    def checktie(self):
        for i in self.g:
            if i != jt and i != bt:
                return False
        return True

    def replay(self):
        while True:
            r = str(input('Voulez vous rejouer ? (y/n) :'))
            if r == 'y' or r == 'Y' :
                self.initialisation()
                game()
            elif r == 'n' or r == 'N':
                time.sleep(2)
                sys.exit()
            else:
                continue
    
    def choose(self):
        self.turn = randint(0,1)

    def flip(self):
        if self.turn == 0:
            self.turn = 1
        else:
            self.turn = 0

joueur = Joueur()
bot = Bot()
jeu = Jeu()
jt = colored("X", color="red")
bt = colored("O", color="green")

def game():
    jeu.initialisation()
    while True:
        if jeu.turn == 0:
            os.system("cls")
            jeu.grille()
            joueur.play()
            if jeu.checkwin(jeu.g, jt):
                jeu.grille()
                print("Bravo le joueur a gagné")
                break
        else:
            bot.play()
            if jeu.checkwin(jeu.g, bt):
                jeu.grille()
                print("Bravo le Bot a gagné")
                break
        if jeu.checktie():
            jeu.grille()
            print("Il y a égalité")
            break
        jeu.flip()
    jeu.replay()

game()


"""
optimisation
Anticiper 2 coups en avance
"""