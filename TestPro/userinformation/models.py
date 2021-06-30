"""model.py"""
from django.db import models

# Create your models here.
class user_request(models.Model):
    """Create user request table"""
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    dob = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    nationality = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pin_code = models.CharField(max_length=20)
    qualification = models.CharField(max_length=20)
    salary = models.CharField(max_length=20)
    pan_number = models.CharField(max_length=20)
    request_received = models.CharField(max_length=20)

class user_response(models.Model):
    """create user response table"""
    response = models.CharField(max_length=500)
