# -*- coding: utf-8 -*-
################################################
# PROTOTYPE
# ----------------------------------------------
# When it is easier to copy an existing object to fully
# initialize a new one.
# ----------------------------------------------
# Motivation:
# Complicated objects (e.g. cars) aren't designed from
# scratch.
# - They reiterate existing designs.
# An existing (partially or fully constructed) design is
# a prototype.
# We make a copy (clone) the prototype and customize it.
# - Requires "deep copy" support.
# We make the clonning convenient (e.g. via a Factory)
# ----------------------------------------------
# A prototype is a partially or fully initialized object
# that you copy (clone) and make use of.
# ----------------------------------------------
# Summary:
# To implement a prototype, partially constuct an object
# and store it somewhere.
# Deep copy the prototype.
# Customize the resulting instance.
# A factory provides a convenient API for using prototypes.
################################################
from copy import deepcopy, copy


class Address:
  def __init__(self, street, city, country):
    self.street = street
    self.city = city
    self.country = country
    
  def __str__(self):
    return f'{self.street}, {self.city}, {self.country}'


class Person:
  def __init__(self, name, address):
    self.name = name
    self.address = address
    
  def __str__(self):
    return f'{self.name} lives at {self.address}.'
  
  
if __name__ == '__main__':
  john = Person('John Miller', Address('123 London Road', 'London', 'UK'))
  print(john)
  
  print('................................................')
  print('Expected wrong behavior')
  jane = john
  jane.name = 'Jane Miller'
  print(john)
  print(jane)
  
  print('................................................')
  print('First approach to solve it. Wrong Behavior expected')
  address = Address('123 London Road', 'London', 'UK')
  john = Person('John Miller', address)
  jane = Person('Jane Miller', address)
  address.city = 'Manchester'
  jane.address.country = 'US'
  print(john)
  print(jane)
  
  print('................................................')
  print('Shallow copy is not a solution. Wrong behavior')
  john = Person('John Miller', Address('123 London Road', 'London', 'UK'))
  jane = copy(john)
  jane.name = 'Jane Miller'
  jane.address.city = 'Manchester'
  print(john)
  print(jane)
  
  print('................................................')
  print('Approach to solve it. Deepcopy, OK!')
  john = Person('John Miller', Address('123 London Road', 'London', 'UK'))
  jane = deepcopy(john)
  jane.name = 'Jane Miller'
  jane.address.city = 'Manchester'
  print(john)
  print(jane)
  