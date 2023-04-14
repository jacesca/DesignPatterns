# -*- coding: utf-8 -*-
################################################
# Singleton Allocator
# ----------------------------------------------
# Singleton is a component which is instantiated only once.
# ----------------------------------------------
# Motivation:
# For some components it only makes sense to have one in the system.
# - Datanase repository.
# - Object factory.
# E.g. the initializer call is expensive.
# - We only do it once.
# - We provide everyone with the same instance.
# Want to prevent anyone creating additional copies.
# Need to take care of lazy instantiation. This idea that nobody really gets
# to instantiate the Singleton until the singleton is actually needed it.
# ----------------------------------------------
# Summary:
# Different realizations of Singleton: custom allocator, decorator, metaclass. 
# The metaclass is the nicer implementation.
# Laziness is easy, just init on first request.
# Monostate variation.
# Testability issues.
################################################
import os, sys
from random import randint

class DatabaseNoInitMethod:
  """
  Class without __init__ method, no issues, no data initialized.
  """
  _instance = None
  
  def __new__(cls, *args, **kwargs):
    if not cls._instance:
      cls._instance = super(DatabaseNoInitMethod, cls).__new__(cls, *args, **kwargs)
    return cls._instance


class DatabaseWithInitMethod:
  """
  Class with __init__ method, data upload each time it is called.
  """
  _instance = None
  
  def __init__(self):
    print('Loading database')
    
  def __new__(cls, *args, **kwargs):
    if not cls._instance:
      cls._instance = super(DatabaseWithInitMethod, cls).__new__(cls, *args, **kwargs)
    return cls._instance
  
  
class DatabaseWithInitTestDifferent:
  """
  Demostrating that object created are not equal. Data is upload each time it is called.
  """
  _instance = None
  
  def __init__(self):
    self.id = randint(1, 101)
    print('Loading database')
    
  def __new__(cls, *args, **kwargs):
    if not cls._instance:
      cls._instance = super(DatabaseWithInitTestDifferent, cls).__new__(cls, *args, **kwargs)
    return cls._instance
  
  
if __name__ == '__main__':
  print('The problem: Database is loaded each time is called.')
  print('................................................')
  
  print('Database without Init method: (No issues, no init method)')
  d1 = DatabaseNoInitMethod()
  d2 = DatabaseNoInitMethod()
  
  print(d1 == d2)
  print(d1 is d2)
  
  print('................................................')
  print('Database with Init method: (2 loads of the same data)')
  d1 = DatabaseWithInitMethod()
  d2 = DatabaseWithInitMethod()
  
  print(d1 == d2)
  print(d1 is d2)
  
  print('................................................')
  print('Database with Init method, testing they are different: (2 loads of the same data)')
  d1 = DatabaseWithInitTestDifferent()
  d2 = DatabaseWithInitTestDifferent()
  
  print(d1 == d2)
  print(d1 is d2)
  