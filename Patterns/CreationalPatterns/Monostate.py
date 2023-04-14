# -*- coding: utf-8 -*-
################################################
# Monostate
# ----------------------------------------------
# A particular variation on the Singleton design pattern, where
# you put all the state of an object into a static variable. 
# But at the same time, you allow people to create new objects, 
# thereby making new instances which all access the same thing.
################################################


class CEO:
  __shared_state = {
    'name': 'Steve Poillot',
    'age': 55
  }
  
  def __init__(self):
    self.__dict__ = self.__shared_state
  
  def __str__(self):
    return f'{self.name} is {self.age} years old.'


# ----------------------------------------------
# Now, we can sort of packaage this into a class, 
# a base class that we can inherit there by making 
# this approach a bit more generic
# ----------------------------------------------
class Monostate:
  _shared_state = {}
  
  def __new__(cls, *args, **kwargs):
    obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
    obj.__dict__ = cls._shared_state
    return obj


class CFO(Monostate):
  def __init__(self):
    self.name = ''
    self.money_managed = 0
  
  def __str__(self):
    return f'{self.name} manages ${self.money_managed}.'


if __name__ == '__main__':
  print('Monostate implementation through the same class:')
  print('You are not just copying the data, you are actually '
        'copying the reference to the entire dictionary')
  print('................................................')
  
  ceo1 = CEO()
  ceo2 = CEO()
  print(ceo1)
  print(ceo2)
  
  ceo2.name = 'Bridget Martin'
  ceo2.age = 37
  print(ceo1)
  print(ceo2)
  
  print('................................................')
  print('Monostate implementation through a different class:')
  cfo1 = CFO()
  cfo2 = CFO()
  print(cfo1, cfo2, sep='\n')
  
  cfo2.name = 'Bridget Martin'
  cfo2.money_managed = '320Million'
  print(cfo1, cfo2, sep='\n')
