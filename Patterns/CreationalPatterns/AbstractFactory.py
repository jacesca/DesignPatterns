# -*- coding: utf-8 -*-
################################################
# ABSTRACT FACTORY
# ----------------------------------------------
# Abstract Factory is a creational design pattern 
# that lets you produce families of related objects 
# without specifying their concrete classes.
# It is essentially abstract based classes, however
# you can make them.
# ----------------------------------------------
# If you have a hierarchy of types, then you can have a 
# corresponding hierarchy of factories. At some point 
# you would have an abstract factory as a base class
# of other factories.
################################################
from abc import ABC
from enum import Enum, auto


class HotDrink(ABC):
  def consume(self):
    pass
  

class Tea(HotDrink):
  def consume(self):
    print('This tea is delicious.')
    
    
class Coffee(HotDrink):
  def consume(self):
    print('This coffee is delicious.')
    
    
class HotDrinkFactory(ABC):
  def prepare(self, amount):
    pass
  
  
class TeaFactory(HotDrinkFactory):
  def prepare(self, amount):
    print(f'Put in tea bag, boil water, '
          f'pour {amount}ml, enjoy!')
    return Tea()


class CoffeeFactory(HotDrinkFactory):
  def prepare(self, amount):
    print(f'Grind some coffee beans, boil water, '
          f'pour {amount}ml, enjoy!')
    return Coffee()


def make_drink(type):
  if type.lower() == 'tea':
    return TeaFactory().prepare(200)
  elif type.lower() == 'coffee':
    return CoffeeFactory().prepare(50)
  else:
    return None 
  
  
class HotDrinkMachine:
  """
  This approach breaks the OCP because when you make a new 
  kind of drink, you need to modify this class.
  """
  class AvailableDrink(Enum):
    COFFEE = auto()
    TEA = auto()
  
  factories = []
  initialized = False
  
  def __init__(self):
    if not self.initialized:
      self.initialized = True  
      for d in self.AvailableDrink:
        name = d.name.lower().capitalize()
        factory_name = name + 'Factory'
        factory_instance = eval(factory_name)()
        self.factories.append((name, factory_instance))
        
  def make_drinks(self):
    print('Available drinks:')
    for index, factory in enumerate(self.factories):
      print(f'{index}. {factory[0]}')
    
    total_factories = len(self.factories)
    s = input(f'Please pick drink (0-{total_factories-1}): ')
    idx = int(s)
    
    if idx < total_factories:
      s = input('Specify ammount: ')
      amount = int(s)

      return self.factories[idx][1].prepare(amount)
    else:
      print('No drink selected or available.')
      return None
      
    
if __name__ == '__main__':
  print('Using "make_drink" method: ')
  entry = input('What kind of drink would you like? ')
  drink = make_drink(entry)
  if drink:
    drink.consume()
  else:
    print('No drink selected or available.')


  print('................................................')  
  print('Using "HotDrinkMachine" class:')
  hdm = HotDrinkMachine()
  hdm.make_drinks()
  