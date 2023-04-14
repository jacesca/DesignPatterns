# -*- coding: utf-8 -*-
################################################
# Memento Undo and Redo
################################################


class Memento:
    def __init__(self, balance):
        self.balance = balance


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.changes = [Memento(self.balance)]
        self.current = 0
        
    def deposit(self, amount):
        self.balance += amount
        m = Memento(self.balance)
        self.changes.append(m)
        self.current += 1
        return m
    
    def restore(self, memento):
        if memento:
            self.balance = memento.balance
            self.changes.append(memento)
            self.current = len(self.changes)-1
            
    def undo(self):
        if self.current > 0:
            self.current -= 1
            m = self.changes[self.current]
            self.balance = m.balance
            # del self.changes[self.current]
            return m
        return None
        
    def redo(self):
        if self.current + 1 < len(self.changes):
            self.current += 1
            m = self.changes[self.current]
            self.balance = m.balance
            # del self.changes[self.current]
            return m
        return None
        
    def __str__(self):
        return f'Balance: ${self.balance}'
    
  
if __name__ == '__main__':
    print('................................................')
    print('Memento pattern:')
    print('................................................')
    account = BankAccount(100)
    print('Initial state -> ', account)
    
    account.deposit(50)
    print('Memento 1 -> ', account)
    account.deposit(25)
    print('Memento 2 -> ', account)
    
    # undo 2 last transaction
    account.undo()
    account.undo()
    print('After undo() twice -> ', account)
    
    # restore m2
    account.redo()
    print('After redo() -> ', account)
    
    