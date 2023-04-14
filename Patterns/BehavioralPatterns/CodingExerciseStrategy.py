# -*- coding: utf-8 -*-
# ################################################
# Strategy Coding Exercise
# ----------------------------------------------
# Consider the quadratic equation and its canonical solution:
#           ax² + bx + c = 0
#               -b √ (b² - 4ac)
#           x = ————————————————
#                     2a
#
# The part "b² - 4ac" is called the discriminant. Suppose we want 
# to provide an API with two different strategies for calculating 
# the discriminant:
# (1) In OrdinaryDiscriminantStrategy, If the discriminant is negative, 
#     we return it as-is. This is OK, since our main API returns Complex  
#     numbers anyway.
# (2) In RealDiscriminantStrategy, if the discriminant is negative, the 
#     return value is NaN (not a number). NaN propagates throughout the 
#     calculation, so the equation solver gives two NaN values. In Python, 
#     you make such a number with float('nan').
# 
# Please implement both of these strategies as well as the equation solver 
# itself. With regards to plus-minus in the formula, please return the + result 
# as the first element and - as the second. Note that the solve() method is 
# expected to return complex values.
################################################
from unittest import TestCase, main
import cmath
import math
from abc import ABC


class DiscriminantStrategy(ABC):
    def calculate_discriminant(self, a, b, c):
        return (b*b) - 4*a*c


class OrdinaryDiscriminantStrategy(DiscriminantStrategy):
    pass
        


class RealDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        result = super().calculate_discriminant(a, b, c)
        if result < 0:
            return float('nan')
        else:
            return result


class QuadraticEquationSolver:
    def __init__(self, strategy):
        self.strategy = strategy

    def solve(self, a, b, c):
        """ Returns a pair of complex (!) values """
        discriminant = complex(self.strategy.calculate_discriminant(a, b, c), 0)
        root_disc = cmath.sqrt(discriminant)
        return(
            (-b + root_disc) / (2 * a),
            (-b - root_disc) / (2 * a)
        )
        
        
class TestEvaluate(TestCase):
    def test_positive_ordinary(self):
        strategy = OrdinaryDiscriminantStrategy()
        solver = QuadraticEquationSolver(strategy)
        results = solver.solve(1, 10, 16)
        self.assertEqual(complex(-2, 0), results[0])
        self.assertEqual(complex(-8, 0), results[1])

    def test_positive_real(self):
        strategy = RealDiscriminantStrategy()
        solver = QuadraticEquationSolver(strategy)
        results = solver.solve(1, 10, 16)
        self.assertEqual(complex(-2, 0), results[0])
        self.assertEqual(complex(-8, 0), results[1])

    def test_negative_ordinary(self):
        strategy = OrdinaryDiscriminantStrategy()
        solver = QuadraticEquationSolver(strategy)
        results = solver.solve(1, 4, 5)
        self.assertEqual(complex(-2, 1), results[0])
        self.assertEqual(complex(-2, -1), results[1])

    def test_negative_real(self):
        strategy = RealDiscriminantStrategy()
        solver = QuadraticEquationSolver(strategy)
        results = solver.solve(1, 4, 5)
        self.assertTrue(math.isnan(results[0].real))
        self.assertTrue(math.isnan(results[1].real))
        self.assertTrue(math.isnan(results[0].imag))
        self.assertTrue(math.isnan(results[1].imag))


if __name__ == '__main__':
    print('----------------------------------------------------------------------')
    print('Strategy pattern:')
    print('----------------------------------------------------------------------')
    main()
