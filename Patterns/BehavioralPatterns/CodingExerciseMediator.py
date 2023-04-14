# -*- coding: utf-8 -*-
################################################
# Mediator Coding Exercise
# ----------------------------------------------
# Our system has any number of instances of Participant classes. 
# Each Participant has a value integer attribute, initially zero.
# A participant can say() a particular value, which is broadcast to 
# all other participants. At this point in time, every other 
# participant is obliged to increase their value by the value 
# being broadcast.
# Example:
# - Two participants start with values 0 and 0 respectively
# - Participant 1 broadcasts the value 3. 
#   We now have Participant 1 value = 0, Participant 2 value = 3
# - Participant 2 broadcasts the value 2. 
#   We now have Participant 1 value = 2, Participant 2 value = 3
################################################
from unittest import TestCase, main

# ----------------------------------------------
# First approach
# ----------------------------------------------
# class Participant:
#   def __init__(self, mediator):
#     self.value = 0
#     self.mediator = mediator
#     self.mediator.people.append(self)
#   def say(self, value):
#     self.mediator.broadcast(self, value)


# class Mediator:
#   def __init__(self):
#     self.people = []
#   def broadcast(self, player, value):
#     for p in self.people:
#       if p != player:
#         p.value += value


# ----------------------------------------------
# Second approach: using events
# ----------------------------------------------
class Event(list):
  def __call__(self, *args, **kwds):
    for item in self:
      item(*args, **kwds)
      
      
class Participant:
  def __init__(self, mediator):
    self.value = 0
    self.mediator = mediator
    self.mediator.events.append(self.alert)

  def alert(self, player, value):
    if self != player:
      self.value += value
    
  def say(self, value):
    self.mediator.broadcast(self, value)


class Mediator:
  def __init__(self):
    self.events = Event()
  
  def broadcast(self, player, value):
    self.events(player, value)
        


class TestFirstSuite(TestCase):
  def test(self):
    m = Mediator()
    p1 = Participant(m)
    p2 = Participant(m)

    self.assertEqual(0, p1.value)
    self.assertEqual(0, p2.value)

    p1.say(2)

    self.assertEqual(0, p1.value)
    self.assertEqual(2, p2.value)

    p2.say(4)

    self.assertEqual(4, p1.value)
    self.assertEqual(2, p2.value)
        
                
if __name__ == '__main__':
  print('----------------------------------------------------------------------')
  print('Iterator pattern:')
  
  m = Mediator()
  p1 = Participant(m)
  p2 = Participant(m)
  print(f'p1: {p1.value}, p2: {p2.value}')
  
  p1.say(3)
  p2.say(2)
  print(f'p1: {p1.value}, p2: {p2.value}')
  
  print('----------------------------------------------------------------------')
  
  main()
