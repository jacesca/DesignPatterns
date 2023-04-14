# -*- coding: utf-8 -*-
################################################
# Composite
# ----------------------------------------------
# Treating individual and aggregate objects uniformly.
# Composite is a mechanism for treating individual (scalar)
# objects and compositions of objects in a uniform manner.
# ----------------------------------------------
# Motivation:
# Objects use other objects' properties/members through
# inheritance and composition.
# Compositions lets us make compound objects.
# - E.g. a mathematical expression composed of simple expressions, or
# - A grouping of shapes that consistes of several shapes.
# Composite design pattern is used to treat both single (scalar) and
# composite object uniformly.
# - I.e. Foo and Sequence (yielding Foo's) have a common APIs.
# ----------------------------------------------
# Summary:
# - Objects can use other objects via inheritance/composition.
# - Some composed and singular objects need similar/identical behaviors.
# - Composite design pattern lets us treat both types of objects uniformly.
# - Python supports iteration with __iter__ the IterableABC.
# - A single object can make itself iterable by yielding self from __iter__.
################################################


class GraphicObject:
  def __init__(self, color=None):
    self.color = color
    self.children = []
    self._name = 'Group'
    
  @property
  def name(self):
    return self._name 
  
  def _print(self, items, depth):
    items.append('*' * depth)
    if self.color:
      items.append(self.color)
    items.append(f'{self.name}\n')
    for child in self.children:
      child._print(items, depth + 1)
  
  def __str__(self):
    items = []
    self._print(items, 0)
    return ''.join(items)  
  

class Circle(GraphicObject):
  @property
  def name(self):
    return 'Circle'
  

class Square(GraphicObject):
  @property
  def name(self):
    return 'Square'


if __name__ == '__main__':
    drawing = GraphicObject()
    drawing._name = 'My Drawing'
    drawing.children.append(Square('Red'))
    drawing.children.append(Circle('Yellow'))
    
    group = GraphicObject()
    group.children.append(Square('Blue'))
    group.children.append(Circle('Blue'))
    
    drawing.children.append(group)
    
    print('Composite')
    print('................................................')
    print(drawing)
    print(group)