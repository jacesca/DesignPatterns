# -*- coding: utf-8 -*-
################################################
# Facade Coding Exercise
# ----------------------------------------------
# https://en.wikipedia.org/wiki/Magic_square
# A magic square is a square matrix of numbers where the sum in each row, 
# each column, and each of the diagonals is the same.
# You are given a system of 3 classes that can be used to make a magic 
# square. The classes are:
# - Generator: this class generates a 1-dimensional list of random digits in range 1 to 9.
# - Splitter: this class takes a 2D list and splits it into all possible arrangements 
#   of 1D lists. It gives you the columns, the rows and the two diagonals.
# - Verifier: this class takes a 2D list and verifies that the sum of elements in every 
#   sublist is the same.
# Please implement a Façade class called MagicSquareGenerator  which simply generates 
# the magic square of a given size.
################################################
from unittest import TestCase, main
from random import randint

class Generator:
  def generate(self, count):
    return [randint(1,9) for x in range(count)]

class Splitter:
  def split(self, array):
    result = []

    row_count = len(array)
    col_count = len(array[0])

    for r in range(row_count):
      the_row = []
      for c in range(col_count):
        the_row.append(array[r][c])
      result.append(the_row)

    for c in range(col_count):
      the_col = []
      for r in range(row_count):
        the_col.append(array[r][c])
      result.append(the_col)

    diag1 = []
    diag2 = []

    for c in range(col_count):
      for r in range(row_count):
        if c == r:
          diag1.append(array[r][c])
        r2 = row_count - r - 1
        if c == r2:
          diag2.append(array[r][c])

    result.append(diag1)
    result.append(diag2)

    return result

class Verifier:
  def verify(self, arrays):
    first = sum(arrays[0])

    for i in range(1, len(arrays)):
      if sum(arrays[i]) != first:
        return False

    return True

class MagicSquareGenerator:
  def generate(self, size):
    # todo - return a magic square of the given size

    g = Generator()
    s = Splitter()
    v = Verifier()
    
    while True:
      square = [g.generate(size) for _ in range(size)]
      sides = s.split(square)
      is_magic = v.verify(sides)
      if is_magic: 
        return square


class TestEvaluate(TestCase):
  def test_exercise(self):
    gen = MagicSquareGenerator()
    square = gen.generate(3)

    print(square)

    v = Verifier()
    self.assertTrue(v.verify(square),
                    'Verification failed. '
                    'This is not a valid magic square.')
    
      
if __name__ == '__main__':
  print('----------------------------------------------------------------------')
  print('Running each class in the Magic square process:')
  
  size = 3
  g = [Generator().generate(size) for _ in range(size)]
  print(g)
  
  s = Splitter().split(g)
  print(s)
  
  v = Verifier().verify(s)
  print(f'Is magic square? {v}')

  print('----------------------------------------------------------------------')
  print('Adding a Facade:')
  
  magic_square = MagicSquareGenerator().generate(3)
  print(magic_square)
  
  # print('----------------------------------------------------------------------')
  
  main() 