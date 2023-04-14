# -*- coding: utf-8 -*-
################################################
# BUILDER FACETS
# ----------------------------------------------
# Take a look at a complication of the builder pattern.
# This complication arises from the fact that sometimes
# you have an object that is so complicated to build
# that you need more than one builder to do it.
# ----------------------------------------------
# The question are: 
# How can you get several builders participating in the 
# build up of an object?
# How can you actually make a nice fluent interface so
# you can jump from one building to another?
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


class PersonBuilder:
  """
  Builder base class
  """
  def __init__(self, person=Person()):
    self.person = person
  
  @property
  def identifies(self):
    "Break the OCP principle"
    return PersonIdentifyBuilder(self.person)
  
  @property
  def works(self):
    "Break the OCP principle"
    return PersonJobBuilder(self.person)
  
  @property
  def lives(self):
    "Break the OCP principle"
    return PersonAddressBuilder(self.person)
  
  def build(self):
    return self.person


class PersonIdentifyBuilder(PersonBuilder):
  def __init__(self, person):
    super().__init__(person)
  
  def with_name(self, firstname):
    self.person.firstname = firstname
    return self
  
  def with_lastname(self, lastname):
    self.person.lastname = lastname
    return self
  
  def born_on(self, date_of_birth):
    self.person.date_of_birth = date_of_birth
    return self

class PersonJobBuilder(PersonBuilder):
  def __init__(self, person):
    super().__init__(person)
  
  def at(self, company_name):
    self.person.company_name = company_name
    return self
    
  def as_a(self, position):
    self.person.position = position
    return self
  
  def earning(self, annual_income):
    self.person.annual_income = annual_income
    return self
  
  
class PersonAddressBuilder(PersonBuilder):
  def __init__(self, person):
    super().__init__(person)
    
  def at(self, street_address):
    self.person.street_address = street_address
    return self
  
  def with_postcode(self, postcode):
    self.person.postcode = postcode
    return self
  
  def in_city(self, city):
    self.person.city = city
    return self  
  
  
if __name__ == '__main__':
  print('Chain multiple builders')
  print('................................................')
  
  pb = PersonBuilder()
  person = pb.identifies.with_name('Oliver').with_lastname('Flynn').born_on('Jan 19, 2008')\
             .lives.at('123 London Road').in_city('London').with_postcode('SW12BC')\
             .works.at('Fabrik').as_a('Engineering').earning(123000)\
             .build()
  print(person)
  