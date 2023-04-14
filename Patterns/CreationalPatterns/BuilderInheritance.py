# -*- coding: utf-8 -*-
################################################
# BUILDER INHERITANCE
# ----------------------------------------------
# With the builder facets we are violating the OCP,
# becouse when you have a new sub builder you need
# to add it to the builder.
# ----------------------------------------------
# The alternative approach is to use inheritance.
# Whenever you need to build up additional information
# you inherit from a builder that you have already.
################################################

class Person:
  def __init__(self):
    # identification
    self.firstname = None
    self.lastname = None
    self.date_of_birth = None
    # address
    self.street_address = None
    self.postcode = None
    self.city = None
    # employment
    self.company_name = None
    self.position = None
    self.annual_income = None
   
  def __str__(self):
    return f'{self.firstname} {self.lastname} born on {self.date_of_birth}' +\
           f'\nAddress: {self.street_address}, {self.postcode}, {self.city}' +\
           f'\nEmployed at {self.company_name} as a {self.position} earning {self.annual_income}' 

  @staticmethod
  def new():
    return PersonBuilder()
  
  
class PersonBuilder:
  def __init__(self):
    self.person = Person()
    
  def build(self):
    return self.person
  
  
class PersonInfoBuilder(PersonBuilder):
  def with_fname(self, firstname):
    self.person.firstname = firstname
    return self
  
  def with_lname(self, lastname):
    self.person.lastname = lastname
    return self
  
  def born_on(self, date_of_birth):
    self.person.date_of_birth = date_of_birth
    return self


class PersonJobBuilder(PersonInfoBuilder):
  def works_at(self, company_name):
    self.person.company_name = company_name
    return self
    
  def as_a(self, position):
    self.person.position = position
    return self
  
  def earning(self, annual_income):
    self.person.annual_income = annual_income
    return self
  
  
class PersonAddressBuilder(PersonJobBuilder):
  def lives_at(self, street_address):
    self.person.street_address = street_address
    return self
  
  def with_postcode(self, postcode):
    self.person.postcode = postcode
    return self
  
  def in_city(self, city):
    self.person.city = city
    return self  
  
  
if __name__ == '__main__':
  print('Fixing the breaking principles on the BuilderFacets with BuilderIbheritance')
  print('................................................')
  
  pb = PersonAddressBuilder()
  person = pb.with_fname('Oliver').with_lname('Flynn').born_on('Jan 19, 2008')\
             .lives_at('123 London Road').in_city('London').with_postcode('SW12BC')\
             .works_at('Fabrik').as_a('Engineering').earning(123000)\
             .build()
  print(person)