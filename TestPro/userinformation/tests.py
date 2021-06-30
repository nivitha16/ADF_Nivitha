"""tests.py"""
from .validations import check_vali
# Create your tests here.

def test1():
    """first test case"""
    result = check_vali("2000-04-03", "M", "indian", "tamilnadu", "30000")
    assert result == '{"Response ": "Valid", "Reason ": "Success"}'

def test2():
    """second test case"""
    result = check_vali("2018-04-03", "M", "indian", "tamilnadu", "30000")
    assert result == '{"Response ": "Invalid", "Reason ": "Invalid age"}'

def test3():
    """third test case"""
    result = check_vali("1982-04-03", "M", "russia", "tamilnadu", "30000")
    assert result == '{"Response ": "Invalid", "Reason ": "Invalid nationality"}'

def test4():
    """fourth test case"""
    result = check_vali("1982-04-03", "M", "indian", "andra", "30000")
    assert result == '{"Response ": "Invalid", "Reason ": "Invalid state"}'

def test5():
    """fifth test case"""
    result = check_vali("1982-04-03", "M", "indian", "tamilnadu", "200")
    assert result == '{"Response ": "Invalid", "Reason ": "Invalid Salary"}'

