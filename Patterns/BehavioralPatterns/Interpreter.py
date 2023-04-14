# -*- coding: utf-8 -*-
################################################
# Interpreter
# ----------------------------------------------
# A behavioral design pattern that provides a way to evaluate 
# language grammar or expression. 
# This pattern involves implementing an expression interface 
# which tells to interpret a particular context. 
# It is used in SQL parsing, symbol processing engine etc.
# A component that processes structured text data. Does so by
# turning it into separate lexical tokens (lexing) and then
# interpreting sequences of said tokens (parsing).
# ----------------------------------------------
# Motivation:
# Textual input needs to be processed.
# - E.g. turned into OOP structures.
# Some Examples:
# - Programming languages compilers, interpreters and IDEs.
# - HTML, XML and similar.
# - Numeric expressions (3+4/5)
# - Regular expressions.
# Turning strings into OOP based structures in a complicated process.
# ----------------------------------------------
# Summary:
# - Barring simple cases, an interpreter acts in two stages: lexing and parsing.
# - Lexing turns text into a set of tokens, e.g.
#   >> 3 * (4 + 5) --> Lit[3] Star Lparen Lit[4] Plus Lit [5] Rparen
# - Parsing tokens into meaningful constructs, e.g.
#   >> MultiplicationExpression[
#         Integer[3], 
#         AdditionExpression[
#             Integer[4],
#             Integer[5]
#         ]
#      ]
# - Parsed data can then be traversed.
################################################


# ----------------------------------------------
# Lexing
# ----------------------------------------------
from enum import Enum, auto
from typing import List


class Token:
  class Type(Enum):
    INTEGER = auto()
    PLUS = auto()
    MINUS = auto()
    LPAREN = auto()
    RPAREN = auto()
    
  def __init__(self, type: Type, text: str) -> None:
    self.type = type
    self.text = text
  
  def __str__(self) -> str:
    return f'`{self.text}`'
  
  def __repr__(self) -> str:
    return f'`{self.text}`'
    

def lex(input: str) -> List[Token]:
  result = []
  
  i = 0
  while i < len(input):
    if input[i] == '+':
      result.append(Token(Token.Type.PLUS, '+'))
    elif input[i] == '-':
      result.append(Token(Token.Type.MINUS, '-'))
    elif input[i] == '(':
      result.append(Token(Token.Type.LPAREN, '('))
    elif input[i] == ')':
      result.append(Token(Token.Type.RPAREN, ')'))
    elif input[i].isdigit():
      digits = [input[i]]
      for j in range(i+1, len(input)):
        if input[j].isdigit():
          digits.append(input[j])
          i += 1
        else:
          result.append(Token(Token.Type.INTEGER, ''.join(digits)))
          break
    i += 1
  return result

# ----------------------------------------------
# Parsing
# ----------------------------------------------
class Integer:
  def __init__(self, value) -> None:
    self.value = value
    
  def __str__(self) -> str:
    return str(self.value)
    
  def __repr__(self) -> str:
    return str(self.value)
    

class BinaryExpression:
  class Type(Enum):
    ADDITION = auto()
    SUBSTRACTION = auto()
    
  def __init__(self) -> None:
    self.type = None
    self.left = None
    self.right = None
    
  def __repr__(self) -> str:
    return f'{self.type.name} ({self.left}, {self.right})'
  
  @property
  def value(self) -> int:
    if self.type == self.Type.ADDITION: 
      return self.left.value + self.right.value
    elif self.type == self.Type.SUBSTRACTION:
      return self.left.value - self.right.value
    
  

def parse(tokens: List[Token]) -> BinaryExpression:
  result = BinaryExpression()
  have_lhs = False # To indicate if we have set the left hand side of an expression.
  i = 0
  
  while i < len(tokens):
    token = tokens[i]
    
    if token.type == Token.Type.INTEGER:
      integer = Integer(int(token.text))
      if not have_lhs:
        result.left = integer
        have_lhs = True
      else:
        result.right = integer
        
    elif token.type == Token.Type.PLUS:
      result.type = BinaryExpression.Type.ADDITION
      
    elif token.type == Token.Type.MINUS:
      result.type = BinaryExpression.Type.SUBSTRACTION
      
    elif token.type == Token.Type.LPAREN:
      j = i
      while j < len(tokens):
        if tokens[j].type == Token.Type.RPAREN:
          break
        j += 1
      subexpression = tokens[i+1:j]
      element = parse(subexpression)
      if not have_lhs:
        result.left = element
        have_lhs = True
      else:
        result.right = element
      i = j
    
    i += 1
  return result
        
        
  
def calc(input: str) -> int:
  tokens = lex(input)
  print(tokens) # using __repr__ method
  # print(''.join(map(str, tokens))) # using __str__method

  parsed = parse(tokens)
  print(parsed)
  
  print(f'{input} = {parsed.value}')

    
  
if __name__ == '__main__':
  print('----------------------------------------------------------------------')
  print('Interpreter pattern:')
  print('----------------------------------------------------------------------')
  calc('(13+4)-(12+1)')