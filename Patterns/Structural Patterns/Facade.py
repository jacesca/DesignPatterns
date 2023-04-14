# -*- coding: utf-8 -*-
################################################
# Facade
# ----------------------------------------------
# A structural design pattern that provides a simplified 
# interface to a library, a framework, or any other 
# complex set of classes.
# Exposing several components through a single interface.
# Provides a simple, easy to understand/user interface over
# a large and sophisticated body of code.
# ----------------------------------------------
# Motivation:
# Balancing complexity and presentation/usability.
# Ex. Typical home:
# - Many subsystems (electrical, sanitation, etc).
# - Complex internal structure (e.g. floor layers).
# - End user is not exposed to internals.
# Same with software:
# - Many subsystems working to provide flexibility, but...
# - API consumers want it to "just work".
# ----------------------------------------------
# Summary:
# Build a Facade to provide a simplified API over
# a set of classes.
# May wish to (optionally) expose internals through
# the facade.
# May allow users to 'escalate' to use more complex
# APIs if they need to. 
################################################


class Buffer:
  def __init__(self, width: int=30, height: int=20) -> None:
    self.width = width
    self.height = height
    self.buffer = ''
    
  def __getitem__(self, item: str) -> str:
    return self.buffer.__getitem__(item)
  
  def write(self, text: str) -> None:
    self.buffer += text
  
  def __str__(self) -> str:
    return ','.join(self.buffer)


class Viewport:
  def __init__(self, buffer: Buffer=Buffer()) -> None:
    self.buffer = buffer
    self.offset = 0
    
  def get_char_at(self, index:int) -> str:
    return self.buffer[index + self.offset]
  
  def append(self, text: str) -> None:
    # self.buffer += text
    self.buffer.write(text)
    

# Building a facade.
class Console:
  def __init__(self) -> None:
    b = Buffer()
    self.current_viewport = Viewport(b)
    self.buffers = [b]
    self.vieports = [self.current_viewport]

  def write(self, text: str) -> None:
    self.current_viewport.buffer.write(text)
    
  def get_char_at(self, index:int) -> str:
    # print(self.current_viewport.buffer)
    return self.current_viewport.get_char_at(index)


if __name__ == '__main__':
  print('................................................')
  print('Just an example:')
  
  c = Console()
  c.write('Hello')
  ch = c.get_char_at(0)
  print(ch)
  print('................................................')
  