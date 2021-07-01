# from django.test import TestCase
import pytest
from .models import request_info, response_info
from .forms import RegisterInfo
from .views import check_state, check_validation,user,addinfo,add_db,check_nation,check_salary,check_age


def test_state():
    """method"""
    res1 = check_state("tamilnadu")
    res2 = "Eligible"
    assert res1 == res2


def test_nation():
    """method"""
    res1 = check_nation("indian")
    res2 = "Eligible"
    assert res1 == res2


def test_salary():
    """method"""
    res1 = check_salary(30000)
    res2 = "Eligible"
    assert res1 == res2


def test_age():
    """method"""
    res1 = check_age(22,'male')
    res2 = "Eligible"
    assert res1 == res2