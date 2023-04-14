# -*- coding: utf-8 -*-
################################################
# Mediator
# ----------------------------------------------
# A behavioral design pattern that lets you reduce chaotic dependencies 
# between objects. The pattern restricts direct communications between 
# the objects and forces them to collaborate only via a mediator object.
# Facilitates communication between components.
# A component that facilitates communication between other components
# without them necessarily being aware of each other or having direct
# (reference) access to each other.
# ----------------------------------------------
# Motivation:
# Components may go in and out of a system ata any time:
# - Chat room participants.
# - Players in an MMORPG (Massively multiplayer online role-playing games).
# It makes no sense for them to have direct references to one another:
# - Those references may go dead.
# Solution: Have them all refer to some central component that facilitates
#           communication.
# ----------------------------------------------
# Summary:
# - Create the mediator and have each object in the sytem refer to it.
#   E.g. in a property.
# - Mediator engages in bidirectional communications with its connected 
#   components.
# - Mediator has functions the components can call.
# - Components have functions the mediator can call.
# - Event processing (e.g. Rx [reactor extensions]) libraries make 
#   communication easier to implement.
################################################
# Allow references to objects not created yet. E.g. left: Node=None
from __future__ import annotations


class Person:
  def __init__(self, name: str) ->  None:
    self.name = name
    self.chat_log = []
    self.room = None
    
  def receive(self, sender: str, message: str) -> None:
    text = f'{sender}: {message}'
    self.chat_log.append(text)
    print(f"[{self.name}'s chat session] {text}")
    
  def say(self, message: str) -> None:
    self.room.broadcast(self.name, message)
  
  def private_msg(self, who: str, message: str) -> None:
    self.room.message(self.name, who, message)
    
  def __str__(self) -> str:
    return self.name
  
  
class ChatRoom:
  def __init__(self) -> None:
    self.people = []
    
  def join(self, person: Person) -> None:
    join_msg = f'{person.name} joins the chat'
    
    self.broadcast('Room', join_msg)
    self.people.append(person)
    
    person.room = self
    
  def broadcast(self, source: str, message: str) -> None:
    for p in self.people:
      if p.name != source:
        p.receive(source, message)
        
  def message(self, source: str, destination: str, message) -> None:
    for p in self.people:
      if p.name == destination:
        p.receive(source, message)
    
    
  
if __name__ == '__main__':
  print('................................................')
  print('Mediator pattern:')
  print('................................................')
  room = ChatRoom()
  
  john = Person('John')
  jane = Person('Jane')
  
  room.join(john)
  room.join(jane)
  
  john.say('Hi room!')
  jane.say('Oh, hey John')
  
  simon = Person('Simon')
  room.join(simon)
  
  simon.say('Hi everyone!')
  
  jane.private_msg('Simon', 'Glad you could join us!')
  