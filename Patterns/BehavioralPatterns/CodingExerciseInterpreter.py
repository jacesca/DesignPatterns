# -*- coding: utf-8 -*-
################################################
# Interpreter Coding Exercise
# ----------------------------------------------
# You are asked to write an expression processor for simple numeric expressions 
# with the following constraints:
# - Expressions use integral values (e.g., '13' ), single-letter variables defined in Variables, 
#   as well as + and - operators only
# - There is no need to support braces or any other operations
# - If a variable is not found in variables  (or if we encounter a variable with >1 letter, e.g. ab), 
#   the evaluator returns 0 (zero)
# - In case of any parsing failure, evaluator returns 0
# 
# Example:
# - calculate("1+2+3")  should return 6
# - calculate("1+2+xy")  should return 0
# - calculate("10-2-x")  when x=3 is in variables  should return 5
################################################
from enum import Enum, auto
from unittest import TestCase, main


class ExpressionProcessor:
  class Token:
    class Type(Enum):
      INTEGER = auto()
      VARIABLE = auto()
      PLUS = auto()
      MINUS = auto()
      
    def __init__(self, type, text):
      self.type = type
      self.text = text
    
    def __str__(self):
      return f'`{self.text}`'
    
    def __repr__(self):
      return f'`{self.text}`'

  
  def __init__(self):
    self.variables = {}
    self.err = None
  
  def set_variables(self, var, value):
    self.variables[var] = value
    self.err = None
    
  def _lex(self, input):
    self.err = None
    result = []
    if input:
      if input[-1] in ['+', '-']:
        self.err = 'Last term can not be an operator!'
    else:
      self.err = 'No expresion defined!'
    if not self.err:
      i = 0
      while i < len(input):
        if input[i] == '+':
          if i-1 >= 0:
            if input[i-1] in ['+', '-']:
              self.err = 'Missing term!'
              break
          result.append(self.Token(self.Token.Type.PLUS, '+'))
        elif input[i] == '-':
          result.append(self.Token(self.Token.Type.MINUS, '-'))
        elif input[i].isalpha():
          result.append(self.Token(self.Token.Type.VARIABLE, input[i]))
          if i+1 < len(input):
            if input[i+1] not in ['+', '-']:
              self.err = 'Variable not valid!'
              break
        elif input[i].isdigit():
          digits = [input[i]]
          for j in range(i+1, len(input)):
            if input[j] not in ['+', '-']:
              digits.append(input[j])
              i += 1
            else:
              break
          digits = ''.join(digits)
          if digits.isdigit():
            result.append(self.Token(self.Token.Type.INTEGER, ''.join(digits)))
          else:
            self.err = 'Expression not valid!'
            break
        else:
          self.err = 'Incorrect expression!'
          return []
        i += 1
    if self.err:
      return []
    return result
  
  def _get_value(self, token):
    if token.type == self.Token.Type.INTEGER:
      return int(token.text)
    elif token.type == self.Token.Type.VARIABLE:
      if token.text in self.variables.keys():
        return self.variables[token.text]
      else:
        self.err = 'Variable not defined!'
        return 0
        
  def _parse(self, tokens):
    if self.err:
      return 0
    else:
      result = 0
      i = 0

      while i < len(tokens):
        token = tokens[i]
      
        if token.type in [self.Token.Type.INTEGER, self.Token.Type.VARIABLE]:
          result = self._get_value(token)
        elif token.type == self.Token.Type.PLUS:
          i += 1
          result += self._get_value(tokens[i])
        elif token.type == self.Token.Type.MINUS:
          i += 1
          result -= self._get_value(tokens[i])
          
        if self.err:
            return 0
        i += 1
    return result
  
  def calculate(self, expression):
    tokens = self._lex(expression)
    print(tokens) 

    parsed = self._parse(tokens)
    # print(parsed)

    return parsed
    # print(f'{input} = {parsed.value}')
            


class TestFirstSuite(TestCase):
    @classmethod
    def setUpClass(cls):
        ep = ExpressionProcessor()
        ep.variables['x'] = 5
        cls.ep = ep

    def test_simple(self):
        self.assertEqual(1, self.ep.calculate('1'))

    def test_addition(self):
        self.assertEqual(3, self.ep.calculate('1+2'))

    def test_addition_with_variable(self):
        self.assertEqual(6, self.ep.calculate('1+x'))

    def test_failure(self):
        self.assertEqual(0, self.ep.calculate('1+xy'))
        
        
if __name__ == '__main__':
  c = ExpressionProcessor()
  vars = [('x', 3), ('z', 4)]
  for v in vars:
    c.set_variables(*v) 
  for i, exp in enumerate(['1+2+3', 
                           '10-2-x',
                           '10-2-y',
                           '10-2-yr',
                           '10r-2-y',
                           '10-2-',
                           '-2-8',
                           '4++10',
                           '++10',
                           '4+ +10',
                           '5',
                           '1']):
    print('\n----------------------------------------------------------------------')
    print(f'Executing Example {i+1}: ({exp})')
    print('Variables -> ', c.variables)
    print(f'result: {c.calculate(exp)}')
    print(f'Err: {c.err}')
  
  print('\n----------------------------------------------------------------------')
  main()
