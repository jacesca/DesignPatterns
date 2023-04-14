# -*- coding: utf-8 -*-
################################################
# 4.
# Interface Segregation Principle (ISP)
# ----------------------------------------------
# Don't put too much into an interface, split into
# spearate interfaces.
# YAGNI - You Ain't Going to Need It. This means
# that if you are not going to need certain methods
# implemented, why force other people to implement
# the interface in the first place.
# ----------------------------------------------
# You don't really want to stick to many elements
# to many methods, for example, into an interface.
################################################
from abc import abstractmethod


class Machine:
  def print(self, document):
    raise NotImplementedError
  
  def fax(self, document):
    raise NotImplementedError
  
  def scan(self, document):
    raise NotImplementedError
  
  def __str__(self):
    return type(self).__name__
  
  def _methods(self):
    return [method for method in dir(self) if not method.startswith('_')]
  
  
class MultiFunctionPrinter(Machine):
  def print(self, document):
    pass
  
  def fax(self, document):
    pass
  
  def scan(self, document):
    pass
  
  
class OldFashionedPrinter(Machine):
  def print(self, document):
    pass
  
  # def fax(self, document):
  #   pass # do nothing
  
  # def scan(self, document):
  #   """Not supported!"""
  #   raise NotImplementedError('Printer can not scan!')
  

################################################
# Solution: Split the interface into separate parts
# that people can implement.
################################################
class GeneralMachine:
  def __str__(self):
    return type(self).__name__
  
  def _methods(self):
    return [method for method in dir(self) if not method.startswith('_')]
  
  
class Printer(GeneralMachine):
  @abstractmethod
  def print(self, document):
    pass


class Scanner(GeneralMachine):
  @abstractmethod
  def scan(self, document):
    pass
  

class FaxMachine(GeneralMachine):
  @abstractmethod
  def fax(self, document):
    pass
  
  
class MyPrinter(Printer):
  def print(self, document):
    print(document)
    
    
class Photocopier(Printer, Scanner):
  def print(self, document):
    pass
  
  def scan(self, document):
    pass
  

if __name__ == '__main__':
  print('................................................')
  print('Principle 4: ISP')
  print('................................................')
  print('Breaking the principle')
  m = MultiFunctionPrinter()
  print(f'{str(m)} have the following methods: \n{m._methods()}')
  o = OldFashionedPrinter()
  print(f'{str(o)} have the following methods: \n{o._methods()}')
  print('................................................')
  print('Separating in smaller interface')
  p = MyPrinter()
  print(f'{str(p)} have the following methods: \n{p._methods()}')
  f = Photocopier()
  print(f'{str(f)} have the following methods: \n{f._methods()}')
  