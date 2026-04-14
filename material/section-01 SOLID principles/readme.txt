1. Single Responsibility Principle (SRP) — class should do only one task.
2. Open Closed Principle (OCP) — class should be extended not modified.
3. Liskov Substitution Principle (LSP) — child classes must be able to replace their super classes.
4. Interface Segregation Principle (ISP) — interfaces should be small: classes should not implement unnecessary methods.
5. Dependency Inversion Principle (DIP) — dependency is reversed: high level components are free of low-level components.

------------------------------
-- Creational
------------------------------
Factory Method
Abstract Factory (factory of factories)
Builder (complex objects using smaller objects)
Prototype (cloning)
Singleton (single instance)
------------------------------
-- Structural
------------------------------
Adapter (incompatible interfaces)
Bridge (decouple an abstraction from its implementation)
Composite (a class that contains group of its own objects)
Decorator (wrapper / no modifications on existing class, new functionality added)
Facade (hides complexity)
Flyweight (reduce weight of object creation, create if needed or reuse)
Proxy (a class represents functionality of another class — create a proxy class having original object)
------------------------------
-- Behavioral
------------------------------
Chain of Responsibility
Command (stock.buy returns BuyStock, stock.sell returns SellStock — both using Stock class)
Interpreter (language grammer, sql parsing)
Iterator (.next)
Mediator (communication between different classes)
Memento (restores to a previous state)
Observer (register, notify)
State (status, context)
Null Object (for do-nothing relationship, instead of returning null value)
Strategy (a class behavior or its algorithm can change at runtime)
Template (abstract class, method flow)
Visitor (execution algorithm of element can vary as and when visitor varies)
MVC