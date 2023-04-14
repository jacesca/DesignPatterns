# -*- coding: utf-8 -*-
################################################
# Flyweights Decorator | Text Formatting
################################################
class FormattedText:
  def __init__(self, plain_text:str) -> None:
    self.plain_text = plain_text
    self.caps = [False] * len(plain_text)
    
  def capitalize(self, start: int, end: int) -> None:
    for i in range(start, end):
      self.caps[i] = True
  
  def __str__(self) -> str:
    return ''.join([
      c.upper() if self.caps[i] else c for i, c in enumerate(self.plain_text)
    ])


# Implementing Flyweight pattern
class BetterFormattedText:
  def __init__(self, plain_text:str) -> None:
    self.plain_text = plain_text
    self.formatting = []
    
  class TextRange:
    def __init__(self, start: int, end: int, capitalize=False) -> None:
      self.start = start
      self.end = end
      self.capitalize = capitalize
      
    def covers(self, position: int) -> bool:
      return self.start <= position <= self.end

  def get_range(self, start: int, end: int) -> str: 
    range = self.TextRange(start, end)
    self.formatting.append(range)
    return range
  
  def __str__(self) -> str:
    result = []
    for i in range(len(self.plain_text)):
      c = self.plain_text[i]
      for r in self.formatting:
        if r.covers(i) and r.capitalize:
          c = c.upper()
      result.append(c)
    return ''.join(result)


if __name__ == '__main__':
  print('................................................')
  print('Text Formatting example:')
  
  text = 'This is a brave new world'
  ft = FormattedText(text)
  ft.capitalize(10, 15)
  print(ft)
  
  print('................................................')
  print('Applying Flyweight pattern:')
  
  text = 'This is a brave new world'
  bft = BetterFormattedText(text)
  bft.get_range(16, 19).capitalize = True
  print(bft)
  print('................................................')
  
  