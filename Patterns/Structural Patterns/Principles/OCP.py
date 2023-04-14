# -*- coding: utf-8 -*-
################################################
# 2.
# Open-Closed Principle (OCP)
# ----------------------------------------------
# Classes should be open for extension but closed
# for modification.
# ----------------------------------------------
# You add new functionality via extension not 
# via modification.
# Open for extension, closed for modification.
# ----------------------------------------------
# Anti-patterns:
# Modify to add more and more methods.
################################################
from enum import Enum


class Color(Enum):
  RED = 1
  GREEN = 2
  BLUE = 3
  
class Size(Enum):
  SMALL = 1
  MEDIUM = 2
  LARGE = 3
  
class Product:
  def __init__(self, name, color, size):
    self.name = name
    self.color = color
    self.size = size
    
  def __repr__(self):
    return self.name
  
  
class ProductFilter:
  """
  With this class implementation we are violating the OPC principle.
  This entire approach does not scale, causing state space explosion.
  The number of functions increase base on the number of combinations.
  For 2 features, 3 methods, for 3 features, 7 methods 
  (c s w cs sw cw csw = 7 methods for color, size and weight)
  """
  def filter_by_color(self, products, color):
    for p in products:
      if p.color == color: yield p
      
  def filter_by_size(self, products, size):
    for p in products:
      if p.size == size: yield p
      
  def filter_by_size_and_color(self, products, size, color):
    for p in products:
      if p.size == size and p.color == color:
        yield p
    
################################################
# Solution: follow the enterprise pattern: Specification
################################################
class Specification:
  """
  Specification is a class which determines whether or not a
  particular item satisfies a particular criteria.
  """
  def is_satisfied(self, item):
    """
    We are not going to do anything inside this particular method 
    because you are meant to override this method.
    """
    pass
  
  def __and__(self, other):
    """
    And operator can not be overwriten, but & yes.
    Expected use:
    spec1 & spec2
    """
    return AndSpecification(self, other)
    


class AndSpecification(Specification):
  def __init__(self, *args):
    self.args = args

  def is_satisfied(self, item):
    return all(map(
      lambda spec:spec.is_satisfied(item), self.args
    ))
    

class Filter:
   def filter(self, items, spec):
     """
     Nothing here also, the whole idea is that we extend things
     """
     pass
   
   
class ColorSpecification(Specification):
  def __init__(self, color):
    self.color = color
    
  def is_satisfied(self, item):
    return item.color == self.color
  
  
class SizeSpecification(Specification):
  def __init__(self, size):
    self.size = size
    
  def is_satisfied(self, item):
    return item.size == self.size


class BetterFilter(Filter):
  def filter(self, items, spec):
    for item in items:
      if spec.is_satisfied(item): 
        yield item


if __name__ == '__main__':
  print('................................................')
  print('Principle 2: OCP')
  print('................................................')
  
  apple = Product('Apple', Color.GREEN, Size.SMALL)
  tree = Product('Tree', Color.GREEN, Size.LARGE)
  house = Product('House', Color.BLUE, Size.LARGE)
  
  products = [apple, tree, house]
  
  pf = ProductFilter()
  result = pf.filter_by_color(products, Color.GREEN)

  print('Green products (old - breaking the principle):')
  print(result, list(result))
  for p in pf.filter_by_color(products, Color.GREEN):
    print(f'- {p.name} is green.')  
    
    
  print('................................................')
  print('Green products (new - applying the principle):')
  bf = BetterFilter()
  green = ColorSpecification(Color.GREEN)
  for p in bf.filter(products, green):
    print(f'- {p.name} is green.')
    
  print('Large products:')
  large = SizeSpecification(Size.LARGE)
  for p in bf.filter(products, large):
    print(f'- {p.name} is large.')

  print('................................................')
  print('COMBINING SPECIFICATIONS')
  print('Large blue products (Using the AndSpecification class):')
  large_blue = AndSpecification(large,
                                ColorSpecification(Color.BLUE))
  for p in bf.filter(products, large_blue):
    print(f'- {p.name} is large and blue.')
  print('Large blue products (Using & operators):')
  large_and_blue = large & ColorSpecification(Color.BLUE)
  for p in bf.filter(products, large_and_blue):
    print(f'- {p.name} is large and blue.')
  
    