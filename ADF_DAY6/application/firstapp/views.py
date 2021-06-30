"""module"""
from datetime import date
from datetime import datetime
import json
from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import request_info, response_info
from .forms import RegisterInfo

# Create your views here.

# def home(request):
#     """home"""
#     context = {
#         "name": "nivitha",
#         "number": 986
#
#     }
#     return render(request, 'home.html', context)
#     # return HttpResponse("<h1>Hello World</h1>")
#
# def newsp(request):
#     """news"""
#     # return HttpResponse("<h1>Hello World</h1>")
#     # obj =newsp.objects.get(id=1)
#     # context = {
#     #     "list":["python","java","c++"],
#     #     "mynum":50,
#     #     "data": obj
#     #
#     # }
#     return render(request, 'news.html')

def addinfo(request):
    """addinfo"""
    # return HttpResponse("<h1>Hello World</h1>")
    context = {
        "form": RegisterInfo
    }
    return render(request, 'signup.html',context)

def user(request):
    """user"""
    form = RegisterInfo(request.POST)
    if form.is_valid():
        myreg = request_info(firstname=form.cleaned_data['firstname'],
                            middlename=form.cleaned_data['middlename'],
                            lastname=form.cleaned_data['lastname'],
                            dob=form.cleaned_data['dob'],
                            gender=form.cleaned_data['gender'],
                            nationality=form.cleaned_data['nationality'],
                            city=form.cleaned_data['city'],
                            state=form.cleaned_data['state'],
                            pincode=form.cleaned_data['pincode'],
                            qualification=form.cleaned_data['qualification'],
                            salary=form.cleaned_data['salary'],
                            panid=form.cleaned_data['panid'],
                            )
        myreg.save()
        value=""
        value=check_validation()
    return HttpResponse(value)

def check_validation():
    """validation"""
    f_val = ""
    f_val = request_info.objects.raw('SELECT  id from firstapp_request_info where id='
                             '(select max(id) from firstapp_request_info)')[0]
    req_id = f_val.id

    f_val = request_info.objects.raw('SELECT  id,dob from firstapp_request_info where id='
                             '(select max(id) from firstapp_request_info)')[0]
    dob = f_val.dob

    f_val = request_info.objects.raw('SELECT  id,gender from firstapp_request_info where id='
                             '(select max(id) from firstapp_request_info)')[0]
    gender = f_val.gender

    f_val = request_info.objects.raw('SELECT  id, nationality from firstapp_request_info where id='
                             '(select max(id) from firstapp_request_info)')[0]
    nation = f_val.nationality

    f_val = request_info.objects.raw('SELECT  id,state from firstapp_request_info where id='
                             '(select max(id) from firstapp_request_info)')[0]
    state = f_val.state

    f_val = request_info.objects.raw('SELECT  id,salary from firstapp_request_info where id='
                             '(select max(id) from firstapp_request_info)')[0]
    salary = f_val.salary

    f_val = request_info.objects.raw('SELECT  id,panid from firstapp_request_info where id='
                             '(select max(id) from firstapp_request_info)')[0]
    pan = f_val.panid

    # f_val = request_info.objects.raw('SELECT  id,req_date from firstapp_request_info where id='
    #                          '(select max(id) from firstapp_request_info)')[0]
    # req_date = f_val.req_date

    flag = 1
    age1 = check_age1(dob)
    if flag == 1:
        nat_val = check_nation(nation)
        if nat_val != 'Eligible':
            response_val="Not Eligible"
            reason_val="Invalid Nationality"
            flag = 0
        else:
            response_val = "Eligible"
            reason_val = "SUCCESS"


    if flag == 1:
        state_val = check_state(state)
        if state_val != 'Eligible':
            response_val = "Not Eligible"
            reason_val = "Invalid State"
            flag = 0
        else:
            response_val = "Eligible"
            reason_val = "SUCCESS"

    if flag == 1:
        sal_val = check_salary(salary)
        if sal_val != 'Eligible':
            response_val = "Not Eligible"
            reason_val = "Invalid Salary"
            flag = 0
        else:
            response_val = "Eligible"
            reason_val = "SUCCESS"

    if flag == 1:
        age_val = check_age(age1,gender)
        if age_val != 'Eligible':
            response_val = "Not Eligible"
            reason_val = "Invalid age"
            flag = 0
        else:
            response_val = "Eligible"
            reason_val = "SUCCESS"

    if flag == 1:
        pan_val = validate_pan(pan)
        if pan_val != 'Eligible':
            response_val = "Not Eligible"
            reason_val = "Request received the same user "
            flag = 0
        else:
            response_val = "Eligible"
            reason_val = "SUCCESS"

    dictation = {"Request_id": req_id, "Response": response_val, "Reason": reason_val}
    dictation = json.dumps(dictation)
    add_db(req_id, response_val, dictation)
    return response_val


def check_nation(nation):
    """nationality"""
    st1 = nation.casefold()
    list1 = ['indian', 'american']
    print(st1)
    cri2 = "Eligible" if st1 in list1 else "Invalid Nationality"
    return cri2

def check_state(state1):
    """state"""
    sr_1 = state1.casefold()
    str21 = sr_1.replace(' ', '')
    list2 = ['andhrapradesh', 'arunachalpradesh', 'assam', 'bihar', 'chhattisgarh', 'karnataka',
             'madhyapradesh', 'odisha', 'tamilnadu', 'telangana', 'westbengal']
    cri3 = "Eligible" if str21 in list2 else "Invalid State"
    print(cri3,str21)
    return cri3

def check_salary(salary):
    """salary"""
    cri1="Eligible" if 10000<salary<90000 else "Not Valid Salary"
    print(cri1,salary)
    return cri1

def check_age(age1,gender1):
    """age"""
    cri4=''
    g_g=gender1.casefold()
    if (age1>21 and g_g=='male') or (age1>18 and g_g=='female'):
        cri4="Eligible"
    else:
        cri4="Not valid"
    print(cri4)
    print(gender1)
    return cri4

def check_age1(birth_date):
    """method"""
    today = date.today()
    age2 = today.year - birth_date.year -((today.month, today.day) <
         (birth_date.month, birth_date.day))
    print(age2)
    return age2

def validate_pan(pan_num):
    """validate_pam"""
    dates = []
    for i_val in request_info.objects.raw('SELECT id, panid,req_date FROM firstapp_request_info'):
        if pan_num == i_val.panid:
            str1 = ''.join(str(i_val.req_date))
            str1 = str1.split()
            dates.append(str1)
    if len(dates) > 0:
        dates.reverse()
        date_formate = '%Y-%m-%d'
        get_date = date.today()
        d1_data = get_date.strftime(date_formate)
        print(d1_data)
        a_data = datetime.strptime(d1_data, date_formate)
        b_data = datetime.strptime(dates[0][0], date_formate)
        delta = a_data - b_data
        delta = abs(delta)

        cri9 = "Activity in last five days" \
            if delta.days <= 5 else "Eligible"

        print(cri9)
    else:
        cri9="New User"
    return cri9

def add_db(req_id,response,dictation):
    """add_db"""
    mydata = response_info(req_id = req_id,response = response,reason = dictation)
    mydata.save()
