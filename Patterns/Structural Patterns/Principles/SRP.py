# -*- coding: utf-8 -*-
################################################
# 1.
# Single Responsability Principle (SRP) or 
# Separation of Concerns (SOC).
# ----------------------------------------------
# A class should only have one reason to change.
# Separation of concerns - Different classes
# handling different, independent tasks/problems.
# ----------------------------------------------
# Each class has a single main responsability.
# You do not want to overload your objects 
# with too many responsabilities.
# ----------------------------------------------
# Anti-patterns:
# God objects: when you have a developer, who
# decides to put everthing into a single class,
# (a massive class) --> Bad code.
################################################
class Journal:
  def __init__(self):
    self.entries = []
    self.count = 0
    
  def add_entry(self, text):
    self.count += 1
    self.entries.append(f'{self.count}: {text}')
    
  def remove_entry(self, position):
    del self.entries[position]
    
  def __str__(self):
    return '\n'.join(self.entries)

  # def save(self, filename):
  #   """
  #   Take a file name and save itself into it.
  #   This brake the SRP/SOC principle by giving additional responsabilities.
  #   Not only does the Journal now store entries and allow us to manipulate the entries, but
  #   its now taking responsability of persistence by providing functionality for saving and
  #   loading the journal from differente resources.
  #   This is a bad idea. If you think about a complete application where in addition to journals,
  #   you also have other different types, all of those types might have their own save and their
  #   own load and load_from_web and so on, and this functionality might have to be centrally 
  #   changed at some point.
  #   """
  #   with open(filename, 'w') as f:
  #     f.write(str(self))

  # def load(self, filename):
  #   """
  #   As the previous, this could look like a good idea.
  #   """
  #   pass

  # def load_from_web(self, url):
  #   """
  #   Third example breaking the SRP/SOC principle.
  #   """
  #   pass

################################################
# Solution: separate into different classses
################################################
class PersistenceManager:
  @staticmethod
  def save_to_file(journal, filename):
    with open(filename, 'w') as f:
      f.write(str(journal))
      
  @staticmethod
  def load(journal, filename):
    pass
  
  @staticmethod
  def load_from_web(journal, url):
    pass


def main():
  print('................................................')
  print('Principle 1: SRP/SOC')
  print('................................................')
  j = Journal()
  j.add_entry('I cried today.')
  j.add_entry('I ate a bug')
  print(f'Journal entries: \n{j}')
  
  file = 'journal.txt'
  PersistenceManager.save_to_file(j, file)
  print('Reading the file:')
  with open(file) as f:
    print(f.read())


if __name__ == '__main__':
  main()
