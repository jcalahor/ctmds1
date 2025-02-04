import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from generator import iterative_method, numpy_method

def test_iterative_method():
    number = 1000
    random_numbers = iterative_method(number)    
    assert len(random_numbers) == number
    
    for r in random_numbers:
        assert r > 0 and r <= 100

def test_numpy_method():
    number = 1000
    random_numbers = numpy_method(number)    
    assert len(random_numbers) == number
    
    for r in random_numbers:
        assert r > 0 and r <= 100