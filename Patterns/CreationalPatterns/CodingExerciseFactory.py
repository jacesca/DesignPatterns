# -*- coding: utf-8 -*-
################################################
# Factory Coding Exercise
# ----------------------------------------------
# You are given a class called Person. 
# The person has two attributes: id , and name .
# Please implement a PersonFactory that has a non-static create_person() method 
# that takes a person's name and return a person initialized with this name and an id.
# The id of the person should be set as a 0-based index of the object created. 
# So, the first person the factory makes should have Id=0, second Id=1 and so on.
################################################
from unittest import TestCase, main


class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        
    def __str__(self):
      return f'({self.id}) {self.name}'

class PersonFactory:
    def __init__(self):
      self.num_persons_created = 0
      
    def create_person(self, name):
        p = Person(self.num_persons_created, name)
        self.num_persons_created += 1
        return p
        
        
# if __name__ == '__main__':
#   pf = PersonFactory()
  
#   print('First person: ')
#   p = pf.create_person('Oliver')
#   print(p)
  
#   print('................................................')
#   print('Second person: ')
#   p = pf.create_person('Julieta')
#   print(p)

class TestEvaluate(TestCase):
    def test_exercise(self):
        pf = PersonFactory()

        p1 = pf.create_person('Chris')
        self.assertEqual(p1.name, 'Chris')
        self.assertEqual(p1.id, 0)

        p2 = pf.create_person('Sarah')
        self.assertEqual(p2.id, 1)


if __name__ == '__main__':
    main()     
    
# pytest CodingExerciseFactory.py