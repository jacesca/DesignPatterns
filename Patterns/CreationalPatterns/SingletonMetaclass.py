# -*- coding: utf-8 -*-
################################################
# Singleton Metaclass
################################################


class Singleton(type):
  _instances = {}
  
  def __call__(cls, *args, **kwds):
    if cls not in cls._instances:
      cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwds)
      
    return cls._instances[cls]
  

class Database(metaclass=Singleton):
  def __init__(self):
    print('Loading database')
    
    
if __name__ == '__main__':
  print('Testing the Singleton metaclass')
  print('................................................')
  d1 = Database()
  d2 = Database()
  
  print(d1 == d2)