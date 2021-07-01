"""module"""
from django.db import models
from django.utils import timezone

# Create your models here.
# class news(models.Model):
#     """news"""
#     author = models.CharField(max_length=30)
#     title = models.CharField(max_length=30)
#     description = models.TextField()
#     pub_date=models.DateTimeField(default=timezone.now())
#
#     def __str__(self):
#         return self.author

class request_info(models.Model):
    """class"""
    firstname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.IntegerField()
    qualification = models.CharField(max_length=100)
    salary = models.IntegerField()
    panid = models.CharField(max_length=100)
    req_date=models.DateField(default=timezone.now())

    def __str__(self):
        return self.firstname

class response_info(models.Model):
    """class"""
    req_id=models.IntegerField()
    response=models.CharField(max_length=200)
    reason=models.CharField(max_length=200)

    def __str__(self):
        return self.req_id