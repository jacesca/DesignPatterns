# -*- coding: utf-8 -*-
################################################
# Decorator
# ----------------------------------------------
# A structural design pattern that lets you attach 
# new behaviors to objects by placing these objects 
# inside special wrapper objects that contain the 
# behaviors.
# Facilitates the addition of behaviors to individual
# objects without inheriting from them.
# ----------------------------------------------
# Motivation:
# Want to augment an object with additional functionality.
# Do not want to rewrite or alter existing code (OCP).
# Want to keep new functionality separete (SRP).
# Need to be able to interact with existing structures.
# Two options:
# - Inherit from required object (if possible).
# - Build a Decorator, which simply references the decorated
#   object(s).
# ----------------------------------------------
# Summary:
# A decorator keeps the reference to the decorated object(s).
# Adds utility attributes and methods to augment the object's
# features.
# May or may not forward calls to the underlying objects.
# Proxying of underlying calls can be done dynamically.
# Python's functional decorators wrap functions; no direct relation to 
# the Gang of Four (GoF) Decorator pattern. 
################################################
import time

def some_op():
  print('Starting op')
  time.sleep(1)
  print('We are done!')
  return 123


# Defining a new decorator
def time_it(func):
  def wrapper():
    start = time.time()
    result = func()
    end = time.time()
    print(f'{func.__name__} took {int((end - start)*1000)}ms')
    return result
  return wrapper
    

# Applyint the new decorator
@time_it
def some_op_d():
  print('Starting op')
  time.sleep(1)
  print('We are done!')
  return 123


if __name__ == '__main__':
  print('................................................')
  print('Normal behavior of a funtion (without decorator):')
  some_op()

  print('................................................')
  print('Calling the new behavior function:')
  time_it(some_op)()
  
  print('................................................')
  print('Calling the function with the applied decorator:')
  some_op_d()
  
  print('................................................')
  