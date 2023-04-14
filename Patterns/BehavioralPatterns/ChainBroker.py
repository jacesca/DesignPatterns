# -*- coding: utf-8 -*-
################################################
# Broker Chain
################################################
from abc import ABC
from enum import Enum
from typing import Any, Self


# Building an event broker (observer)
# CQS
class Event(list):
  def __call__(self, *args: Any, **kwds: Any) -> None:
    for item in self:
      item(*args, **kwds)
      
  def __str__(self) -> str:
    return ', '.join([item.__qualname__ for item in self])


class WhatToQuery(Enum):
  ATTACK = 1
  DEFENSE = 2
  

class Query:
  def __init__(self, creature_name: str, what_to_query: WhatToQuery, default_value: int) -> None:
    self.value = default_value
    self.what_to_query = what_to_query
    self.creature_name = creature_name


class Game:
  def __init__(self) -> None:
    self.queries = Event()

  def perform_query(self, sender: Self, query: Query) -> None:
    self.queries(sender, query)
    

class Creature:
  def __init__(self, game: Game, name: str, attack: int, defense: int) -> None:
    self.game = game
    self.name = name
    self.initial_attack = attack
    self.initial_defense = defense

  @property
  def attack(self) -> int:
    q = Query(self.name, WhatToQuery.ATTACK, self.initial_attack)
    self.game.perform_query(self, q)
    return q.value
  
  @property
  def defense(self) -> int:
    q = Query(self.name, WhatToQuery.DEFENSE, self.initial_attack)
    self.game.perform_query(self, q)
    return q.value
  
  def __str__(self) -> str:
    return f'{self.name} ({self.attack}/{self.defense})'


class CreatureModifier(ABC):
  def __init__(self, game: Game, creature: Creature) -> None:
    print(f'Adding {self.__class__.__name__}')
    self.creature = creature
    self.game = game
    self.game.queries.append(self.handle)
    
  def handle(self, sender: Creature, query: Query) -> None:
    pass
  
  def __repr__(self) -> str:
    return f'{self.__class__.__name__}'
  
  # To work with "with" command (context manager protocol)
  def __enter__(self) -> Self:
    return self
  
  def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
    self.game.queries.remove(self.handle)
  

class DoubleAttackModifier(CreatureModifier):
  def handle(self, sender: Creature, query: Query) -> None:
    if sender.name == self.creature.name and query.what_to_query == WhatToQuery.ATTACK:
      print(f'Doubling {self.creature.name}\'s attack')
      query.value *= 2


if __name__ == '__main__':
  print('................................................')
  print('Broker Chain: Ex1')
  
  game = Game()
  goblin = Creature(game, 'Strong Goblin', 2, 2)
  print(goblin)
  print(f'Attack: {goblin.attack}, Defense: {goblin.defense}')
  print(f'Events: {game.queries}\n')
  
  dam = DoubleAttackModifier(game, goblin)
  dam = DoubleAttackModifier(game, goblin)
  print(f'Events: {game.queries}\n')
  print(goblin)
  
  print('................................................')
  print('Broker Chain: Ex2')
  
  game = Game()
  goblin = Creature(game, 'Strong Goblin', 2, 2)
  DoubleAttackModifier(game, goblin)
  print(goblin)
  print(f'Events: {game.queries}\n')
  
  with DoubleAttackModifier(game, goblin):
    print(goblin)
    print(f'Events: {game.queries}\n')
  
  print(goblin)
  print(f'Events: {game.queries}')
  
  print('................................................')
  