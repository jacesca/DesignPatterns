# -*- coding: utf-8 -*-
################################################
# 3.
# Liskov Substitution Principle (LSP)
# ----------------------------------------------
# You should be able to substitute a base type
# for a subtype.
# ----------------------------------------------
# If you have some interface that takes some sort
# of base class, you should be able to stick a 
# derivide class in there, should work.
# If this principle is broken, the derivated 
# class will have non consistence behavior.
# Code need to be built in a way that derivated
# class should work as well as the main class.
################################################

class Rectangle:
  def __init__(self, width, height):
    """
    We are going to create this features like private
    in the sense that you should not really be touching
    them. 
    """
    self._width = width
    self._height = height
  
  @property
  def area(self):
    return self._width * self._height
  
  @property
  def perimeter(self):
    return (2*self._width) + (2*self._height)
  
  @property
  def width(self):
    return self._width
  
  @width.setter
  def width(self, value):
    self._width = value
  
  @property
  def height(self):
    return self._height
  
  @height.setter
  def height(self, value):
    self._height = value
  
  def __str__(self):
    return f'{type(self).__name__} (width={self.width}, height={self.height})'


class Square(Rectangle):
  """
  This derivated class does not work with the use_it function.
  Solution:
  1. No Squeare class is needed, we can have some sort of boolean
  property on the rectangle telling us weather or not this is a square.
  2. You can have a factory method, which would make a square instead of
  a rectangle.
  """
  def __init__(self, size):
    super().__init__(size, size)
    
  @Rectangle.width.setter
  def width(self, value):
    self._width = self._height = value
    
  @Rectangle.height.setter
  def height(self, value):
    self._width = self._height = value


def use_it(rc):
  """
  This example break the substitution principle.
  Because use_it is no longer working here.
  """
  w = rc.width
  rc.height = 10
  expected_area = int(w*10)
  print(f'Expected an area of {expected_area}, got {rc.area}')
  
  
def use_it_fix(rc):
  """
  This example does not break the substitution principle.
  """
  rc.height = 10
  w = rc.width
  expected_area = int(w*10)
  print(f'Expected an area of {expected_area}, got {rc.area}')
  

if __name__ == '__main__':
  print('................................................')
  print('Principle 3: LSP')
  print('................................................')
  
  r = Rectangle(2, 3)
  print(r)
  use_it(r)
  
  print('................................................')
  s = Square(5)
  print(s)
  use_it(s)
  use_it_fix(s)
  