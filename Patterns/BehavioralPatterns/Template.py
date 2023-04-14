# -*- coding: utf-8 -*-
################################################
# Template
# ----------------------------------------------
# A behavioral design pattern that defines the skeleton of an algorithm 
# in the superclass but lets subclasses override specific steps of the 
# algorithm without changing its structure.
# A high level blueprint for an algorithm to be completed by inheritors.
# Allows us to define the "skeleton" of the algorithm, with concrete 
# implementations defined in subclasses.
# ----------------------------------------------
# Motivation:
# Algorithms can be decomposed into common parts + specifics.
# Strategy pattern does this throught composition:
# - High level algorithm expects trategies to conform to an interface.
# - Concrete implementations implement the interface.
# Template method does the same thing through inheritance:
# - Overall algorithm defined in base class, makes use of abstract members.
# - Inheritors override the abstract members.
# ----------------------------------------------
# Summary:
# - Define an algorithm at a high levele in parent class.
# - Define constituen parts as abstract methods / properties.
# - Inherit the algorith class, providing necessary overrides.
################################################
from abc import ABC


class Game(ABC):
    def __init__(self, number_of_players):
        self.number_of_players = number_of_players
        self.current_player = 0
        
    def run(self):
        self.start()
        while not self.have_winner:
            self.take_turn()
        print(f'Player {self.winning_player} wins!')
    
    @property
    def have_winner(self): pass
    
    @property
    def winning_player(self): pass
    
    def start(self): pass
    def take_turn(self): pass


class Chess(Game):
    def __init__(self):
        super().__init__(2)
        self.max_turns = 10
        self.turn = 1

    def start(self):
        print(f'Starting a game of chest with'
              f'{self.number_of_players} players')
        
    def take_turn(self):
        print(f' Turn {self.turn} taken by player {self.current_player}')
        self.turn += 1
        self.current_player = 1 - self.current_player
        
    @property
    def have_winner(self):
        return self.turn == self.max_turns
    
    @property
    def winning_player(self):
        return self.current_player
    
    
if __name__ == '__main__':
    print('................................................')
    print('Template Method pattern:')
    print('................................................')
    chess = Chess()
    chess.run()
    