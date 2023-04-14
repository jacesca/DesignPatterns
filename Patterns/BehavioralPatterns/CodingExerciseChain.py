# -*- coding: utf-8 -*-
################################################
# Proxy Coding Exercise
# ----------------------------------------------
# You are given a game scenario with classes Goblin and GoblinKing.
# Please implement the following rules:
# - A goblin has base 1 attack/1 defense (1/1), a goblin king is 3/3.
# - When the Goblin King is in play, every other goblin gets +1 Attack.
# - Goblins get +1 to Defense for every other Goblin in play (a
#   GoblinKing is a Goblin!).
#
# Example:
# - Suppose you have 3 ordinary goblins in play. Each one is a 1/3
#   (1/1 + 0/2 defense bonus).
# - A goblin king comes into play. Now every goblin is a 2/4
#   (1/1 + 0/3 defense bonus from each other + 1/0 from goblin king)
#
# The state of all the goblins has to be consistent as goblins are added and
# removed from the game.
# Here is an example of the kind of test that will be run on the system:
#
#     class FirstTestSuite(unittest.TestCase):
#         def test(self):
#             game = Game()
#             goblin = Goblin(game)
#             game.creatures.append(goblin)
#
#             self.assertEqual(1, goblin.attack)
#             self.assertEqual(1, goblin.defense)
#
# Note: creature removal (unsubscription) does not need to be implemented.
################################################
from unittest import TestCase, main
from abc import ABC
from enum import Enum


class Event(list):
  def __call__(self, *args, **kwds):
    for item in self:
      item(*args, **kwds)

  def __str__(self):
    return ', '.join([item.__qualname__ for item in self])


class WhatToQuery(Enum):
  ATTACK = 1
  DEFENSE = 2


class Query:
  def __init__(self, creature_name, what_to_query, default_value):
    self.value = default_value
    self.what_to_query = what_to_query
    self.creature_name = creature_name


class Game:
  def __init__(self):
    self.queries = Event()
    self.creatures = []

  def perform_query(self, sender, query):
    self.queries(sender, query)


class Creature:
  def __init__(self, game, name, attack, defense):
    self.game = game
    self.name = name
    self.initial_attack = attack
    self.initial_defense = defense

  @property
  def attack(self):
    if isinstance(self, Goblin):
      additional_points = sum([
        1 if isinstance(item, GoblinKing) else 0
        for item in self.game.creatures
      ]) - int(isinstance(self, GoblinKing))
    else:
      additional_points = 0
    q = Query(self.name, WhatToQuery.ATTACK, self.initial_attack)
    self.game.perform_query(self, q)
    return q.value + additional_points
  
  @property
  def defense(self):
    if isinstance(self, Goblin):
      additional_points = sum([
        1 if isinstance(item, Goblin) else 0
        for item in self.game.creatures
      ]) - 1
    else:
      additional_points = 0
    q = Query(self.name, WhatToQuery.DEFENSE, self.initial_attack)
    self.game.perform_query(self, q)
    return q.value + additional_points
  
  def __str__(self):
    return f'{self.name} ({self.attack}/{self.defense})'
  
  
class Goblin(Creature):
  def __init__(self, game):
    self.game = game
    self.name = 'Goblin'
    self.initial_attack = 1
    self.initial_defense = 1


class GoblinKing(Goblin):
  def __init__(self, game):
    self.game = game
    self.name = 'Goblin King'
    self.initial_attack = 3
    self.initial_defense = 3


class TestFirstSuite(TestCase):
  def test(self):
    game = Game()
    goblin = Goblin(game)
    game.creatures.append(goblin)

    self.assertEqual(1, goblin.attack)
    self.assertEqual(1, goblin.defense)

    goblin2 = Goblin(game)
    game.creatures.append(goblin2)

    self.assertEqual(1, goblin.attack)
    self.assertEqual(2, goblin.defense)

    goblin3 = GoblinKing(game)
    game.creatures.append(goblin3)

    self.assertEqual(2, goblin.attack)
    self.assertEqual(3, goblin.defense)
    
        
if __name__ == '__main__':
  main()
