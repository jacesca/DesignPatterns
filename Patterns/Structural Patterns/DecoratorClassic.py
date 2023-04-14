# -*- coding: utf-8 -*-
################################################
# Classic Decorator
################################################
from abc import ABC


class Shape(ABC):
  def __str__(self) -> str:
    return ''
  
  
class Circle(Shape):
  def __init__(self, radius:float) -> None:
    self.radius = radius
    
  def resize(self, factor: float) -> None:
    self.radius *= factor
    
  def __str__(self) -> str:
    return f'A circle of radius {self.radius}'


class Square(Shape):
  def __init__(self, side: float) -> None:
    self.side = side
    
  def resize(self, factor: float) -> None:
    self.side *= factor
    
  def __str__(self) -> str:
    return f'A square of side {self.side}'
  

class ColoredShape(Shape):
  def __init__(self, shape: Shape, color: str) -> None:
    self.color = color
    self.shape = shape
    
  def __str__(self) -> str:
    return f'{self.shape} has the color {self.color}'


class ColoredShapeWarning(Shape):
  def __init__(self, shape: Shape, color: str) -> None:
    if isinstance(shape, ColoredShapeWarning):
      raise Exception('Cannot apply same decorator twice')
    self.color = color
    self.shape = shape
    
  def __str__(self) -> str:
    return f'{self.shape} has the color {self.color}'
  
  
class TransparentShape(Shape):
  def __init__(self, shape: Shape, transparency: float) -> None:
    self.shape = shape
    self.transparency = transparency
    
  def __str__(self) -> str:
    return f'{self.shape} has {self.transparency*100.0}% transparency'  
  
  
if __name__ == '__main__':
  print('................................................')
  print('Normal objects:')
  circle = Circle(2)
  square = Square(3)
  print(circle, square, sep='\n')
  
  print('\nAdding behaviors:')
  red_circle = ColoredShape(circle, 'red')
  blue_square = ColoredShape(square, 'blue')
  print(red_circle, blue_square, sep='\n')
  
  red_half_transparent_circle = TransparentShape(red_circle, 0.5)
  print(red_half_transparent_circle)
  
  print('\nNothing prevent of applying the same twice:')
  mixed = ColoredShape(ColoredShape(Square(3), 'red'), 'green')
  print(mixed)
  
  print('\nHandleling twice application of the same behavior:')
  try:
    mixed = ColoredShapeWarning(ColoredShapeWarning(Square(3), 'red'), 'green')
    print(mixed)
  except Exception as e:
    print(str(e))
  
  print('\nThis not avoid the next situation C(T(C)):')
  try:
    mixed = ColoredShapeWarning(TransparentShape(ColoredShapeWarning(Square(3), 'red'), 0.75), 'green')
    print(mixed)
  except Exception as e:
    print(str(e))

  print('\nNew objects resulting from ColoredShape and TransparentShape does not have the resize method:')
  try:
    red_circle.resize(5)
    print(red_circle)
  except AttributeError as e:
    print(str(e))

  print('................................................')
  