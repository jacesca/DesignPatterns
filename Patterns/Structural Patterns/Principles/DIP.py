# -*- coding: utf-8 -*-
################################################
# 5.
# Dependency Inversion Principle (DIP)
# ----------------------------------------------
# High-level modules should not depend upon 
# low-level ones.
# Use abstractions instead and have everything 
# done through abstractions. We looked at how code 
# can be refactored to do exactly that.
# ----------------------------------------------
# High level classes or high level modules in 
# the code should not depend directly on lower
# level modules, instead they should depend on
# abstractions.
# Abstactions refers to abstract class/methods.
# So essentially we want to depend on interfaces
# rather that concrete implementations, because
# that way you can do is you can swap one for
# the other.
################################################
from enum import Enum
from abc import abstractmethod


class Relationship(Enum):
  PARENT = 0
  CHILD = 1
  SIBLING = 2
  
  
class Person:
  def __init__(self, name):
    self.name = name
    
  def __str__(self):
    return self.name
    

class Relationships: # low-level module
  def __init__(self):
    self.relations = []
    
  def add_parent_and_child(self, parent, child):
    self.relations.append((parent, Relationship.PARENT, child))
    self.relations.append((child, Relationship.CHILD, parent))


class Research: # high-level module
  """
  This high level class has a dependency on lower instances.
  So you'll notice that relations is basically the way that the relationships modules stores the relations.
  So at the moment it's a list.
  But imagine if you decide to change from a list to something else to maybe a dictionary or some sort
  of specialized data storage structure. 
  In this case, what's happening is your accessing the internal storage mechanism of relationships,
  which is a low level module in your high level module, which is a bad thing.  
  It's a bad thing because, for example, you cannot just go ahead and change this to something else.
  You kind of go ahead and changes to a dictionary, for example, because then what would happen is all
  of this code will effectively break.
  It would no longer work.
  So this is something that we want to really avoid.
  If you have a dependency on the storage implementation then its better to provide some sort of
  utility methods right inside the low level module to perform the search.
  """
  def __init__(self, relationships):
    relations = relationships.relations
    for r in relations:
      if r[0].name == 'John' and r[1] == Relationship.PARENT:
        print(f'John has a child called {r[2].name}.')
    


################################################
# Solution: Define an interface for the low level module.
# The idea is that research should not depend on the 
# concrete implementation, which is relationships, but it
# should depend on some sort of an abstraction that can 
# subsequently change.
# Passing the search functionality to the interface,
# inside the lower object is a better approach, 
# because if you change the implementations of 
# relations (how it is storaged), you can rewrite 
# the internal find methods and not affect the
# higher object.
################################################
class RelationshipBrowser:
  @abstractmethod
  def find_all_children_of(self, name):
    pass
  
  
class RelationshipsFix(RelationshipBrowser): # low-level module
  def __init__(self):
    self.relations = []
    
  def add_parent_and_child(self, parent, child):
    self.relations.append((parent, Relationship.PARENT, child))
    self.relations.append((child, Relationship.CHILD, parent))

  def find_all_children_of(self, name):
    for r in self.relations:
      if r[0].name == name and r[1] == Relationship.PARENT:
        yield r[2].name


class ResearchFix: # high-level module
  def __init__(self, relationships):
    for child_name in relationships.find_all_children_of('John'):
      print(f'John has a child called {child_name}.')
    
if __name__ == '__main__':
  print('................................................')
  print('Principle 5: DIP')
  print('................................................')     
  
  parent = Person('John')
  child1 = Person('Chris')
  child2 = Person('Matt')
  
  print('Breaking the principle: Risk on storage dependency')
  relationships = Relationships()
  relationships.add_parent_and_child(parent, child1)
  relationships.add_parent_and_child(parent, child2)
  Research(relationships)
  
  print('................................................')     
  print('Avoiding dependency on lower classes:')
  relationships_fix = RelationshipsFix()
  relationships_fix.add_parent_and_child(parent, child1)
  relationships_fix.add_parent_and_child(parent, child2)
  ResearchFix(relationships_fix)
    