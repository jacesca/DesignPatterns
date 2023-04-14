# -*- coding: utf-8 -*-
################################################
# Chain of responsibility
# ----------------------------------------------
# A behavioral design pattern that lets you pass requests 
# along a chain of handlers. Upon receiving a request, each 
# handler decides either to process the request or to pass it 
# to the next handler in the chain.
# Sequence of handlers processing an event one after another.
# A chain of components qho all get a chance to process a 
# command or a query, optionally having default processing 
# implementation and an ability to terminate the processing
# chain.
# ----------------------------------------------
# Motivation:
# Unethical behavior by an employee; who takes the blame?
# - Employee? Manager? CEO?
# You click a graphical element on a form:
# - Button handles it, stops further processing.
# - Underlying group box.
# - Underlying window-
# CCG computer game:
# - Creature has attack and defense values.
# - Those can be boosted by other cards.
# ----------------------------------------------
# Command Query Separation (CQS):
# Command = asking for an action or change 
#           (e.g. please set your attack value to 2).
# Query   = asking for information 
#           (e.g. please give me your attack value)
# CQS     = having separate means of sending commands
#           and queries to e.g. direct field access.
# ----------------------------------------------
# Summary:
# - Chain of responsability can be implemented as a chain 
#   of references or a centralized construct,
# - Enlist objects in the chain, possibly controlling their
#   order.
# - Object removal from chain (e.g. in __exit__).
################################################


class Creature:
  def __init__(self, name: str, attack: int, defense: int) -> None:
    self.name = name
    self.attack = attack
    self.defense = defense
    
  def __str__(self) -> str:
    return f'{self.name} ({self.attack}/{self.defense})'
  
  
class CreatureModifier:
  def __init__(self, creature: Creature) -> None:
    self.creature = creature
    self.next_modifier = None
  
  def add_modifier(self, modifier) -> None:
    if self.next_modifier:
      # print(f'Reviewing {self.next_modifier}')
      self.next_modifier.add_modifier(modifier)
    else:
      print(f'Adding {modifier} to {self.creature.name}')
      self.next_modifier = modifier
  
  def handle(self) -> None:
    """Location where this modifier gets applied to the creature"""
    if self.next_modifier:
      # print(f'Handleling {self.next_modifier}')
      self.next_modifier.handle()
      
  def __str__(self) -> str:
    return self.__class__.__name__


class DoubleAttackModifier(CreatureModifier):
  def handle(self) -> None:
    print(f'Doubling {self.creature.name}\'s attack')
    self.creature.attack *= 2
    super().handle()


class IncreaseDefenseModifier(CreatureModifier):
  def handle(self) -> None:
    if self.creature.attack <= 2:
      print(f'Increasing {self.creature.name}\'s defend')
      self.creature.defense += 1
    super().handle()
    
    
class NoBonusModifier(CreatureModifier):
  def handle(self) -> None:
    print(f'No bonusess for {self.creature.name}!')


if __name__ == '__main__':
  print('................................................')
  print('Example 1:')
  goblin = Creature('Goblin', 1, 1)
  print(goblin)
  
  root = CreatureModifier(goblin)
  root.add_modifier(DoubleAttackModifier(goblin))
  root.add_modifier(IncreaseDefenseModifier(goblin))
  root.add_modifier(DoubleAttackModifier(goblin))
  root.handle()
  print(goblin)
  
  print('................................................')
  print('Example 2: Condition of the increase is handleling internal')
  goblin = Creature('Goblin', 1, 1)
  print(goblin)
  
  root = CreatureModifier(goblin)
  root.add_modifier(DoubleAttackModifier(goblin))
  root.add_modifier(DoubleAttackModifier(goblin))
  root.add_modifier(IncreaseDefenseModifier(goblin))
  root.handle()
  print(goblin)
  
  print('................................................')
  print('Example 3: Avoiding all the next steps')
  goblin = Creature('Goblin', 1, 1)
  print(goblin)
  
  root = CreatureModifier(goblin)
  root.add_modifier(NoBonusModifier(goblin))
  root.add_modifier(DoubleAttackModifier(goblin))
  root.add_modifier(DoubleAttackModifier(goblin))
  root.add_modifier(IncreaseDefenseModifier(goblin))
  root.handle()
  print(goblin)
  
  print('................................................')
  