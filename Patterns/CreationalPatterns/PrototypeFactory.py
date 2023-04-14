# -*- coding: utf-8 -*-
################################################
# PROTOTYPE FACTORY
################################################
from copy import deepcopy


class Address:
  def __init__(self, street, suite, city):
    self.street = street
    self.suite = suite
    self.city = city
    
  def __str__(self):
    return f'{self.street}, Suite #{self.suite}, {self.city}'
  
  
class Employee:
  def __init__(self, name, address):
    self.address = address
    self.name = name
  
  def __str__(self):
    return f'{self.name} works at {self.address}'


class EmployeeFactory:
  main_office_employee = Employee('', Address('123 Est Dr', 0, 'London'))
  aux_office_employee = Employee('', Address('123B Est Dr', 0, 'London'))
  
  @staticmethod
  def __new_employee(emp_office_prototype, name, suite):
    new_emp = deepcopy(emp_office_prototype)
    new_emp.name = name
    new_emp.address.suite = suite
    return new_emp
  
  @staticmethod
  def new_main_office_employee(name, suite):
    return EmployeeFactory.__new_employee(EmployeeFactory.main_office_employee, name, suite)
  
  @staticmethod
  def new_aux_office_employee(name, suite):
    return EmployeeFactory.__new_employee(EmployeeFactory.aux_office_employee, name, suite)
  
  
if __name__ == '__main__':
  john = EmployeeFactory.new_main_office_employee('John Miller', 10123)
  bob = EmployeeFactory.new_aux_office_employee('Bob Cartlon', 10289)
  print(john)
  print(bob)
  