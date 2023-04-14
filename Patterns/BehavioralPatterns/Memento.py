# -*- coding: utf-8 -*-
################################################
# Memento
# ----------------------------------------------
# A behavioral design pattern that lets you save and restore the previous 
# state of an object without revealing the details of its implementation.
# Keep a memento of an object's state to return to that state.
# A token / handle representing the system state. Lets us roll back to the 
# state when the token was generated. May or may not directly expose state
# information.
# ----------------------------------------------
# Motivation:
# An object or system goes through changes.
# - e.g. a bank account gets deposits and withdrawals.
# There are different ways of navigating those changes.
# One way is to record every change (Command) and teach
# a command to undo itself.
# Another is to simply save snapshots of the system (Memento).
# ----------------------------------------------
# Summary:
# - Mementos are used to roll back states arbitrarily.
# - A memento is simply a token/handle class with (typically)
#   no functions of its own.
# - A memento is not required to expose directly the state(s)
#   to which it reverts the system.
# - Can be used to implement undo/redo.
################################################


class Memento:
    def __init__(self, balance):
        self.balance = balance


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        return Memento(self.balance)
    
    def restore(self, memento):
        self.balance = memento.balance
        
    def __str__(self):
        return f'Balance: ${self.balance}'
    
  
if __name__ == '__main__':
    print('................................................')
    print('Memento pattern:')
    print('................................................')
    account = BankAccount(100)
    print('Initial state -> ', account)
    
    m1 = account.deposit(50)
    print('Memento 1 -> ', account)
    m2 = account.deposit(25)
    print('Memento 2 -> ', account)
    
    # restore m1
    account.restore(m1)
    print('Restoring to memento 1 -> ', account)
    
    # restore m2
    account.restore(m2)
    print('Restoring to memento 2 -> ', account)
    
    