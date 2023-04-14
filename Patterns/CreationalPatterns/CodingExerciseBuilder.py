# -*- coding: utf-8 -*-
################################################
# Builder Coding Exercise
# ----------------------------------------------
# You are asked to implement the Builder design pattern for rendering simple chunks of code.
# ----------------------------------------------
# Sample use of the builder you are asked to create:
# cb = CodeBuilder('Person').add_field('name', '""') \
#                           .add_field('age', '0')
# print(cb)
# ----------------------------------------------
# The expected output of the above code is:
# class Person:
#   def __init__(self):
#     self.name = ""
#     self.age = 0
# ----------------------------------------------
# Please observe the same placement of spaces and indentation.
################################################
from unittest import TestCase, main


class CodeBuilder:
    ident_size = '  '
    
    def __init__(self, root_name):
        self.class_name = f'class {root_name.lower().capitalize()}:'
        self.class_body = []

    def add_field(self, name, value):
        self.class_body.append(f'{self.ident_size*2}self.{name} = {value}')
        return self

    def __str__(self):
        if self.class_body:
          body =  f'{self.ident_size}def __init__(self):\n' +\
                  '\n'.join(self.class_body)
        else:
          body = f'{self.ident_size}pass'
        return f'{self.class_name}\n{body}'

# if __name__ == '__main__':
#   print('#................................................')
#   print('# Empty class')
#   cb = CodeBuilder('Foo')
#   print(cb) 
  
#   print('#................................................')
#   print('# Person class')
#   cb = CodeBuilder('Person').add_field('name', '""') \
#                             .add_field('age', '0')
#   print(cb)


class TestEvaluate(TestCase):
    @staticmethod
    def preprocess(s=''):
        return s.strip().replace('\r\n', '\n')

    def test_empty(self):
        cb = CodeBuilder('Foo')
        self.assertEqual(
            self.preprocess(str(cb)),
            'class Foo:\n  pass'
        )

    def test_person(self):
        cb = CodeBuilder('Person').add_field('name', '""') \
            .add_field('age', 0)
        self.assertEqual(self.preprocess(str(cb)),
                         'class Person:\n' +\
                         '  def __init__(self):\n' +\
                         '    self.name = \"\"\n' +\
                         '    self.age = 0')


if __name__ == '__main__':
    main() 