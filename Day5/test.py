import pytest
from application import check_state,nation,salary,check_age,check_five


def test_state():
    """method"""
    res1 = check_state("tamilnadu")
    res2 = "Eligible"
    assert res1 == res2

def test_nation():
    """method"""
    res1 = nation("indian")
    res2 = "Eligible"
    assert res1 == res2

def test_salary():
    """method"""
    res1 = salary(20000)
    res2 = "Eligible"
    assert res1 == res2

def test_age():
    """method"""
    res1 = check_age(21,"male")
    res2 = "Eligible"
    assert res1 == res2

def test_days():
    """method"""
    res1 = check_five(10)
    res2 = "Eligible"
    assert res1 == res2