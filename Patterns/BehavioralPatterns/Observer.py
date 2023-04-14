# -*- coding: utf-8 -*-
################################################
# Observer
# ----------------------------------------------
# A behavioral design pattern that lets you define a subscription 
# mechanism to notify multiple objects about any events that happen 
# to the object they’re observing.
# Am observer is an object that whishes to be informed about
# events happening in the system. The entity generating the event is
# an observable.
# ----------------------------------------------
# Motivation:
# We need to be informed when certain things happen.
# - Object's property changes.
# - Object does something.
# - Some external event occurs.
# We want to listen to events and be notified when they occur.
# - Notifications should include useful data.
# Want to unsubscribe from events if we are no longer interested.
# ----------------------------------------------
# Summary:
# - Observer is an intrusive approach: an observable must
#   provide an event to subscribe to.
# - Subscription and unsubscription handled with addition/removal
#   of items in a list.
# - Property notifications are easy: dependent property 
#   notifications are tricky.
################################################


class Event(list):
    def __call__(self, *args, **kwds):
        for item in self:
            item(*args, **kwds)
      

class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.falls_ill = Event()


    def catch_a_cold(self):
       self.falls_ill(self.name, self.address)
       

def call_doctor(name, address):
    print(f'{name} needs a doctor at {address}')
  
if __name__ == '__main__':
    print('................................................')
    print('Observer pattern:')
    print('................................................')
    
    person = Person('Ana', '221B Baker St')
    person.falls_ill.append(lambda name, address: print(f'{name} catched a cold'))
    person.falls_ill.append(lambda name, address: print(f'{name} is sick at {address}'))
    person.falls_ill.append(call_doctor)
    
    person.catch_a_cold()
    
    person.falls_ill.remove(call_doctor)
    
    person.catch_a_cold()
    