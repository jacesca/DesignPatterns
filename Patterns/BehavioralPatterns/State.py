# -*- coding: utf-8 -*-
################################################
# State
# ----------------------------------------------
# A behavioral design pattern that lets an object alter its 
# behavior when its internal state changes. It appears as if 
# the object changed its class.
# Fun with finite state machines.
# A pattern in which the object's behavior is determined by its
# state. An object transitions from one state to another (something 
# needs to trigger a transition).
# A formalized construct which manages state and transitions is
# called a state machine.
# ----------------------------------------------
# Motivation:
# Consider an ordinary telephone.
# What you do with it deoends on the state of the phone/line.
# - If it is ringing or you want to make a call, you can pick it up.
# - Phone must be off the hook to talk / make a call.
# - If you try calling someone, and it is busy, you put the handset down.
# Changes in state can be explicit or in response to event (Observer pattern).
# ----------------------------------------------
# Summary:
# - Given sufficient complexity it pays to formally define possible states to
#   formally define possible states and events/triggers.
# - Can define:
#   * State entry/exit behaviors.
#   * Action when a particular event causes a trasition.
#   * Guard conditions enabling/disabling a transition.
#   * Default action when no tranistions are found for an event.
################################################


# ----------------------------------------------
# Classic implementation
# So even thought this is a classic implementation, (which each state is a separeted
# class and each class/state handled the transition to the next state), that's not
# something recommendable, because the amount of things that need to be done.
# And also the idea that the state itself regulates the transition to some different
# state, while it is a nice idea, it is not something that people do nowadays.
# ----------------------------------------------
from abc import ABC


class Switch:
    def __init__(self):
        self.state = OffState()
        
    def on(self):
        self.state.on(self)
        
    def off(self):
        self.state.off(self)
        
class State(ABC):
    def on(self, switch):
        print('Light is already on')

    def off(self, switch):
        print('Light is already off')

class OnState(State):
    def __init__(self):
        print('Light turned on')
    
    def off(self, switch):
        print('Turning light off...')
        switch.state = OffState()
    
class OffState(State):
    def __init__(self):
        print('Light turned off')
        
    def on(self, switch):
        print('Turning light on...')
        switch.state = OnState()
    
    
if __name__ == '__main__':
    print('................................................')
    print('Classic State pattern:')
    print('................................................')
    sw = Switch()
    sw.on()
    sw.off()
    sw.off()
    