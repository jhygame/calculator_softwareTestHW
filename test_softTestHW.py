import pytest
import calculate
import UI

def fun_c(a):
    return a+a

def test_operator_compare():
    assert calculate.operator_compare('+', '*') == -1

def test_calculate_string():
    assert calculate.calculate_string("2+2") == 4