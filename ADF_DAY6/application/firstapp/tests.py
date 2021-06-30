# from django.test import TestCase
import pytest
from .models import request_info, response_info
from .forms import RegisterInfo
from .views import check_state, check_validation,user,addinfo,add_db


def test_state():
    """method"""
    res1 = check_state("tamilnadu")
    res2 = "Eligible"
    assert res1 == res2

