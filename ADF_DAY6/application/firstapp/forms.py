"""module"""
from django import forms

class RegisterInfo(forms.Form):
    """form"""
    firstname = forms.CharField(max_length=100)
    middlename = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    dob = forms.DateField()
    gender = forms.CharField(max_length=100)
    nationality = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    state = forms.CharField(max_length=100)
    pincode = forms.IntegerField()
    qualification = forms.CharField(max_length=100)
    salary = forms.IntegerField()
    panid = forms.CharField(max_length=100)
    # req_date = form.DateTimeField(default=timezone.now())
