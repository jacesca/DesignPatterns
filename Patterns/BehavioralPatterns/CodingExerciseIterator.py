# -*- coding: utf-8 -*-
################################################
# Interpreter Coding Exercise
# ----------------------------------------------
# Given the following definition of a Node, please implement preorder 
# traversal right inside Node. The sequence returned should be the 
# sequence of values, not their containing nodes.
################################################
from unittest import TestCase, main


class Node:
  def __init__(self, value, left=None, right=None):
    self.right = right
    self.left = left
    self.value = value

    self.parent = None

    if left:
      self.left.parent = self
    if right:
      self.right.parent = self

  def __str__(self):
    # return str(self.value)
    return '%s (L: %s, R: %s)' % (self.value, self.left, self.right)
  
  def traverse_preorder(self):
    yield self.value
    if self.left:
      yield from self.left.traverse_preorder()
    if self.right:
      yield from self.right.traverse_preorder()
    # def next(current):
    #   if current.left:
    #     return current.left
    #   elif current.right:
    #     return current.right
    #   if current == current.parent.left:
    #     if current.parent.right:
    #       return current.parent.right
    #   parent = current.parent
    #   while parent:
    #     if parent.parent:
    #       if parent.parent.right:
    #         return parent.parent.right
    #       else:
    #         parent = parent.parent
    #     else:
    #       return None
    
    # current = self
    # while current:
    #   yield current.value
    #   current = next(current)
            

class Evaluate(TestCase):
  def test_exercise(self):
    node = Node('a',
                Node('b',
                     Node('c'),
                     Node('d')),
                Node('e'))
    self.assertEqual(
      'abcde',
      ''.join([x for x in node.traverse_preorder()])
    )
        
        
if __name__ == '__main__':
  print('----------------------------------------------------------------------')
  print('Iterator pattern:')
  print('----------------------------------------------------------------------')
  print("""
  # The problem:
  #   1
  #  / \\
  # 2   3
  #
  # in order: 213
  # preorder: 123
  # postorder: 231        
  """)  
  root_node = Node(1, Node(2), Node(3))
  print('Preorder iteration')
  print([item for item in root_node.traverse_preorder()])
  
  print("""
  # The problem:
  #      a
  #     / \\
  #    b   e
  #   / \\
  #  c   d
  # preorder: abcde        
  """)
  root_node = Node('a', Node('b', Node('c'), Node('d')), Node('e'))
  print('Preorder iteration')
  print([item for item in root_node.traverse_preorder()])

  # print('----------------------------------------------------------------------')
  main()
