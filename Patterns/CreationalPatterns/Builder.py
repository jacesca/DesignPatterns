# -*- coding: utf-8 -*-
################################################
# BUILDER
# ----------------------------------------------
# Builder is a creational design pattern that lets 
# you construct complex objects step by step. 
# The pattern allows you to produce different 
# types and representations of an object using 
# the same construction code.
# ----------------------------------------------
# They can have: fluent interface or auditory
# interface.
# ----------------------------------------------
# - Abuilder is a separate component for building an object.
# - Can either give builder an initializer or return it via 
#   a static function.
# - To make builder fluent, return self.
# - Different facets of an object can be built with different 
#   builders working in tandem via a base class.
################################################
class HtmlElement:
  indent_size = 2
  
  def __init__(self, name='', text=''):
    self.text = text
    self.name = name
    self.elements= []
    
  def __str(self, indent):
    lines = []
    i = ' ' * (indent * self.indent_size)
    lines.append(f'{i}<{self.name}>')
    
    if self.text:
      i1 = ' ' * ((indent + 1) * self.indent_size)
      lines.append(f'{i1}{self.text}')
      
    for e in self.elements:
      lines.append(e.__str(indent + 1))
      
    lines.append(f'{i}</{self.name}>')
    return '\n'.join(lines)
  
  def __str__(self):
    return self.__str(0)
  
  @staticmethod
  def create(name):
    """
    This method allows us to start working with an element.
    Expoising the builder, breaks the OCP, but you have to realize
    that there is a bit of entanglement between an element and its 
    builder (they are connected).
    """
    return HtmlBuilder(name)

class HtmlBuilder:
  def __init__(self, root_name):
    self.root_name = root_name
    self.__root = HtmlElement(root_name)
  
  def add_child(self, child_name, child_text):
    self.__root.elements.append(
      HtmlElement(child_name, child_text)
    )
    
  def add_child_fluent(self, child_name, child_text):
    """
    With a fluent interface. This allows to change the
    invocations one after another.
    """
    self.__root.elements.append(
      HtmlElement(child_name, child_text)
    )
    return self
  
  def __str__(self):
    return str(self.__root)


if __name__ == '__main__':
  print('Without any pattern')
  print('................................................')
  # Imagine you need to print some html code
  # Simple case
  text = 'hello'
  parts = ['<p>', text, '</p>']
  print(''.join(parts))

  # A more complex case
  words = ['hello', 'world']
  parts = ['<ul>']
  for w in words:
    parts.append(f'  <li>{w}</li>')
  parts.append('</ul>')
  print('\n'.join(parts))
  print('................................................')

  print('Applying a BUILDER pattern')
  print('................................................')
  builder = HtmlBuilder('ul')
  builder.add_child('li', 'hello')
  builder.add_child('li', 'world')
  print(builder)  
  print('................................................')

  print('Applying a builder pattern with fluid interface')
  print('................................................')
  builder = HtmlBuilder('ul')
  builder.add_child_fluent('li', 'hello')\
         .add_child_fluent('li', 'world')
  print(builder)  
  print('................................................')

  print('Using the exposed constructor inside the HtmlElement')
  print('................................................')
  builder = HtmlElement.create('ul')
  builder.add_child_fluent('li', 'hello')\
         .add_child_fluent('li', 'world')
  print(builder)
