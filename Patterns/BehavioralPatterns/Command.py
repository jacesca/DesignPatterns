# -*- coding: utf-8 -*-
################################################
# Command
# ----------------------------------------------
# A behavioral design pattern that turns a request into a 
# stand-alone object that contains all information about 
# the request. This transformation lets you pass requests 
# as a method arguments, delay or queue a request’s execution, 
# and support undoable operations.
# An object which represents an instruction to perform a 
# particular action. Conatins all the information necessary
# for the action to be taken.
# ----------------------------------------------
# Motivation:
# Ordinary statements are perishable:
# - Cannot undo member assignment.
# - Cannot directly serialize a sequence of actions (calls).
# Want an object that represents an operation.
# - person should change ist age to value 22.
# - car should do explode().
# Uses: GUI commands, multi-level undo/redo, macro recording
# and more!.
# ----------------------------------------------
# Summary:
# - Encapsule all details of an operation in a separate object.
# - Define instuction for applying the command (either in the
#   command iteself, or elsewhere).
# - Optionally define instructions for undoing the command.
# - Can create composite commands (a.k.a. macros). --> a.k.a. also known as
################################################
from abc import ABC
from enum import Enum
from unittest import TestCase, main

from graphene import List


# ----------------------------------------------
# Initial objects
# ----------------------------------------------
class BankAccount:
  OVERDRAFT_LIMIT = -500
  
  def __init__(self, balance: float=0) -> None:
    self.balance = balance
    self.get_balance()
    
  def get_balance(self, action: str='', value: float=None) -> None:
    if action:
      print(f'{action.capitalize()}: ${value}')
    print(self)
 
  def deposit(self, amount: float) -> None:
    self.balance += amount
    self.get_balance('Deposited', amount)

  def withdraw(self, amount: float) -> bool:
    if self.balance - amount >= BankAccount.OVERDRAFT_LIMIT:
      self.balance -= amount
      self.get_balance('Withdrawed', amount)
      return True
    return False
      
  def __str__(self) -> str:
    return f'Balance: ${self.balance}'

  def __repr__(self) -> str:
    return f'BankAccount(${self.balance})'


# ----------------------------------------------
# First Approach: command pattern
# ----------------------------------------------
class Command(ABC):
  def invoke(self):
    pass
  
  def undo(self):
    pass
  
  
class BACommand(Command):
  class Action(Enum):
    DEPOSIT = 0
    WITHDRAW = 1
  
  def __init__(self, account: BankAccount, action: Action, amount: float) -> None:
    self.account = account
    self.action = action
    self.amount = amount
      
  def invoke(self):
    if self.action == self.Action.DEPOSIT:
      self.account.deposit(self.amount)
    elif self.action == self.Action.WITHDRAW:
      self.account.withdraw(self.amount)
      
  def undo(self):
    if self.action == self.Action.DEPOSIT:
      self.account.withdraw(self.amount)
    elif self.action == self.Action.WITHDRAW:
      self.account.deposit(self.amount)
  

# ----------------------------------------------
# Improved Approach: command pattern
# ----------------------------------------------
class BACommandImproved(Command):
  class Action(Enum):
    DEPOSIT = 0
    WITHDRAW = 1
  
  def __init__(self, account: BankAccount, action: Action, amount: float) -> None:
    self.account = account
    self.action = action
    self.amount = amount
    self.success = None
      
  def invoke(self):
    if self.action == self.Action.DEPOSIT:
      self.account.deposit(self.amount)
      self.success = True
    elif self.action == self.Action.WITHDRAW:
      self.success = self.account.withdraw(self.amount)
      
  def undo(self):
    if not self.success:
      return
    
    if self.action == self.Action.DEPOSIT:
      self.account.withdraw(self.amount)
    elif self.action == self.Action.WITHDRAW:
      self.account.deposit(self.amount)


class CompositeBACommand(Command, list):
  def __init__(self, items: List(Command)=[]) -> None:
    super().__init__()
    for i in items:
      self.append(i)
      
  def invoke(self):
    for i in self:
      i.invoke()
  
  def undo(self):
    for i in reversed(self):
      i.undo()
  

# ----------------------------------------------
# Boost Approach: command pattern
# Improving the composite class
# ----------------------------------------------
class CommandBoost(ABC):
  def __init__(self):
    self.success = False
    
  def invoke(self):
    pass
  
  def undo(self):
    pass
  
  
class BACommandBoost(CommandBoost):
  class Action(Enum):
    DEPOSIT = 0
    WITHDRAW = 1
  
  def __init__(self, account: BankAccount, action: Action, amount: float) -> None:
    self.account = account
    self.action = action
    self.amount = amount
      
  def invoke(self):
    if self.action == self.Action.DEPOSIT:
      self.account.deposit(self.amount)
      self.success = True
    elif self.action == self.Action.WITHDRAW:
      self.success = self.account.withdraw(self.amount)
      
  def undo(self):
    if not self.success:
      return
    
    if self.action == self.Action.DEPOSIT:
      self.account.withdraw(self.amount)
    elif self.action == self.Action.WITHDRAW:
      self.account.deposit(self.amount)


class CompositeBACommandBoost(CommandBoost, list):
  def __init__(self, items: List(CommandBoost)=[]) -> None:
    super().__init__()
    for i in items:
      self.append(i)
      
  def invoke(self):
    for i in self:
      i.invoke()
  
  def undo(self):
    for i in reversed(self):
      i.undo()


class MoneyTransferCommandBoost(CompositeBACommandBoost):
  def __init__(self, from_acct, to_acct, amount):
    super().__init__([
      BACommandBoost(from_acct, BACommandBoost.Action.WITHDRAW, amount),
      BACommandBoost(to_acct, BACommandBoost.Action.DEPOSIT, amount)
    ])
    
  def invoke(self):
    ok = True
    for cmd in self:
      if ok:
        cmd.invoke()
        ok = cmd.success
      else:
        cmd.success = False
    self.success = ok


# ----------------------------------------------
# Testing what we did
# ----------------------------------------------
class TestSuite(TestCase):
  def test_1_composite_deposit(self):
    print('\nFIRST TEST CASE:\n---------------')
    ba = BankAccount()
    amount1 = 100
    deposit1 = BACommandImproved(
      ba, BACommandImproved.Action.DEPOSIT, amount1
    )
    amount2 = 50
    deposit2 = BACommandImproved(
      ba, BACommandImproved.Action.DEPOSIT, amount2
    )
    composite = CompositeBACommand([
      deposit1, deposit2
    ])
    composite.invoke()
    print(f'Undo the deposits (${amount1}, ${amount2})...')
    composite.undo()
    self.assertEqual(ba.balance, 0)
    print('...pass...')
    
  def test_2_transfer(self):
    print('\nSECOND TEST CASE:\n----------------')
    ba1 = BankAccount(100)
    ba2 = BankAccount(0)
    print(f'Initial State  -> ba1: {ba1}, ba2: {ba2}')
    
    amount = 100
    #Withdrawing from ba1
    wd = BACommandImproved(
      ba1, BACommandImproved.Action.WITHDRAW, amount
    )
    #to deposit in be2
    dc = BACommandImproved(
      ba2, BACommandImproved.Action.DEPOSIT, amount
    )
    
    transfer = CompositeBACommand([
      wd, dc
    ])
    transfer.invoke()
    print(f'After transfer (${amount}) -> ba1: {ba1}, ba2: {ba2}')
    transfer.undo()
    print(f'After undo     (${amount}) -> ba1: {ba1}, ba2: {ba2}')
    self.assertEqual((ba1.balance, ba2.balance), (100, 0))
    print('...pass...')
      
  def test_3_transfer_fail(self):
    print('\nTHIRD TEST CASE: (FAILURE)\n---------------')
    ba1 = BankAccount(100)
    ba2 = BankAccount(0)
    print(f'Initial State  -> ba1: {ba1}, ba2: {ba2}')
    
    amount = 1000
    #Withdrawing from ba1
    wd = BACommandImproved(
      ba1, BACommandImproved.Action.WITHDRAW, amount
    )
    #to deposit in be2
    dc = BACommandImproved(
      ba2, BACommandImproved.Action.DEPOSIT, amount
    )
    
    transfer = CompositeBACommand([
      wd, dc
    ])
    transfer.invoke()
    print(f'After transfer (${amount}) -> ba1: {ba1}, ba2: {ba2}')
    # self.assertEqual((ba1.balance, ba2.balance), (100, 0))
    
    transfer.undo()
    print(f'After undo     (${amount}) -> ba1: {ba1}, ba2: {ba2}')
    # self.assertEqual((ba1.balance, ba2.balance), (100, 0))
    # print('...pass...')
    print('...FAIL...')
    
  def test_4_better_transfer(self):
    print('\nFOURTH TEST CASE: (BOOST TO AVOID THE FAILURE)\n---------------')
    ba1 = BankAccount(100)
    ba2 = BankAccount(0)
    print(f'Initial State  -> ba1: {ba1}, ba2: {ba2}')
    
    amount = 1000
    #Withdrawing from ba1 to deposit in be2
    transfer = MoneyTransferCommandBoost(ba1, ba2, amount)
    transfer.invoke()
    print(transfer.success)
    print(f'After transfer (${amount}) -> ba1: {ba1}, ba2: {ba2}')
    self.assertEqual((ba1.balance, ba2.balance), (100, 0))
    
    transfer.undo()
    print(transfer.success)
    print(f'After undo     (${amount}) -> ba1: {ba1}, ba2: {ba2}')
    self.assertEqual((ba1.balance, ba2.balance), (100, 0))
    print('...pass...')
    
    
  def test_5_better_allowed_transfer(self):
    print('\nFIFTH TEST CASE: \n---------------')
    ba1 = BankAccount(100)
    ba2 = BankAccount(0)
    print(f'Initial State  -> ba1: {ba1}, ba2: {ba2}')
    
    amount = 100
    #Withdrawing from ba1 to deposit in be2
    transfer = MoneyTransferCommandBoost(ba1, ba2, amount)
    transfer.invoke()
    print(transfer.success)
    print(f'After transfer (${amount}) -> ba1: {ba1}, ba2: {ba2}')
    self.assertEqual((ba1.balance, ba2.balance), (0, amount))
    
    transfer.undo()
    print(transfer.success)
    print(f'After undo     (${amount}) -> ba1: {ba1}, ba2: {ba2}')
    self.assertEqual((ba1.balance, ba2.balance), (amount, 0))
    print('...pass...')
    
  
if __name__ == '__main__':
  print('----------------------------------------------------------------------')
  
  print('The object:')
  
  my_account = BankAccount(600)
  my_account.deposit(200)
  my_account.withdraw(900)
  
  print('----------------------------------------------------------------------')
  
  print('Applying the command pattern:')
  
  ba = BankAccount()
  amount = 100
  cmd = BACommand(ba, BACommand.Action.DEPOSIT, amount)
  cmd.invoke()
  print(f'After ${amount} deposit: {ba}')
  
  cmd.undo()
  print(f'${amount} deposit undone: {ba}')
  
  print('----------------------------------------------------------------------')
  print('Showing the current issues:')
  
  illegal_ba = BankAccount()
  amount = 1000
  illegal_cmd = BACommand(illegal_ba, BACommand.Action.WITHDRAW, amount)
  illegal_cmd.invoke()
  print(f'After impossible ${amount} withdrawal: {illegal_ba}')

  illegal_cmd.undo()
  print(f'After undo: {illegal_ba}')
  
  print('----------------------------------------------------------------------')
  print('After improving the Command class:')
  
  ba = BankAccount()
  amount = 1000
  cmd = BACommandImproved(ba, BACommandImproved.Action.WITHDRAW, amount)
  cmd.invoke()
  print(f'After impossible ${amount} withdrawal: {ba}')

  cmd.undo()
  print(f'After undo: {ba}')
  
  print('----------------------------------------------------------------------')
  print('Showing one more case where it fails:')
  try:
    main()
  except AssertionError as e:
    print(str(e))
    pass
  