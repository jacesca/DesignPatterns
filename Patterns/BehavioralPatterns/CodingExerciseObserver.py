# -*- coding: utf-8 -*-
################################################
# Observer Coding Exercise
# ----------------------------------------------
# Imagine a game where one or more rats can attack a player. 
# Each individual rat has an initial attack value of 1. However, 
# rats attack as a swarm, so each rat's attack value is actually 
# equal to the total number of rats in play.
# Given that a rat enters play through the initializer and leaves play 
# (dies) via its __exit__ method, please implement the Game and Rat 
# classes so that, at any point in the game, the Attack value of a rat 
# is always consistent.
# Here's a sample unit test your code should pass:
# 
#   def test_three_rats_one_dies(self):
#       game = Game()
#       
#       rat = Rat(game)
#       self.assertEqual(1, rat.attack)
#     
#       rat2 = Rat(game)
#       self.assertEqual(2, rat.attack)
#       self.assertEqual(2, rat2.attack)
# 
#       with Rat(game) as rat3:
#           self.assertEqual(3, rat.attack)
#           self.assertEqual(3, rat2.attack)
#           self.assertEqual(3, rat3.attack)
# 
#       self.assertEqual(2, rat.attack)
#       self.assertEqual(2, rat2.attack)
################################################
from unittest import TestCase, main


class Event(list):
    def __call__(self, *args, **kwds):
        for item in self:
            item(*args, **kwds)
            

class Game:
    def __init__(self):
        self.events = Event()
        self.rats = []

class Rat:
    def __init__(self, game):
        self.game = game
        self.attack = 1
        self.game.events.append(self.update_attack)
        self.game.rats.append(self)
        self.game.events()
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.game.events.remove(self.update_attack)
        self.game.rats.remove(self)
        self.game.events()
    
    def update_attack(self):
        self.attack = len(self.game.rats)
        

class Evaluate(TestCase):
    def test_single_rat(self):
        game = Game()
        rat = Rat(game)
        self.assertEqual(1, rat.attack)

    def test_two_rats(self):
        game = Game()
        rat = Rat(game)
        rat2 = Rat(game)
        self.assertEqual(2, rat.attack)
        self.assertEqual(2, rat2.attack)

    def test_three_rats_one_dies(self):
        game = Game()

        rat = Rat(game)
        self.assertEqual(1, rat.attack)

        rat2 = Rat(game)
        self.assertEqual(2, rat.attack)
        self.assertEqual(2, rat2.attack)

        with Rat(game) as rat3:
            self.assertEqual(3, rat.attack)
            self.assertEqual(3, rat2.attack)
            self.assertEqual(3, rat3.attack)

        self.assertEqual(2, rat.attack)
        self.assertEqual(2, rat2.attack)

     
if __name__ == '__main__':
    print('----------------------------------------------------------------------')
    print('Observer pattern:')
    print('----------------------------------------------------------------------')
    main()
