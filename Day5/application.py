"""DOCSTRING"""
import re
from datetime import date
import datetime as dates
import json
import logging
import mysql.connector
import config as cfg

logging.basicConfig(
    filename="sample.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s"
    )

def salary(sals):
    """method"""
    cri1="Eligible" if 10000<sals<90000 else "Not Valid Salary"
    logging.debug("checks salary")
    return cri1

def nation(nat):
    """method"""
    st1=nat.casefold()
    list1=['indian','american']
    cri2="Eligible" if st1 in list1 else "Invalid Nationality"
    logging.debug("checks nationality")
    return cri2

def check_state(state1):
    """method"""
    sr_1=state1.casefold()
    str21=sr_1.replace(' ','')
    list2=['andhrapradesh', 'arunachalpradesh', 'assam', 'bihar',  'chhattisgarh',  'karnataka',
           'madhyapradesh',  'odisha',  'tamilnadu',  'telangana', 'westbengal']
    cri3="Eligible" if str21 in list2 else "Invalid State"
    logging.debug("checks state")
    return cri3

def check_age(age1,gender1):
    """method"""
    cri4=''
    g_g=gender1.casefold()
    if (age1>=21 and g_g=='male') or (age1>=18 and g_g=='female'):
        cri4="Eligible"
    else:
        cri4="Not valid"
    logging.debug("checks age")
    return cri4

def check_age1(birth_date):
    """method"""
    today = date.today()
    age2 = today.year - birth_date.year -((today.month, today.day) <
         (birth_date.month, birth_date.day))

    logging.debug("checks age")
    return age2

def check_five(days):
    """method"""
    cri5="Eligible" if days > 5 else "Request received in last 5 days from the same user"
    logging.debug("checks request received in last 5 days")
    return cri5

# Driver code

fname=input("Enter first name ")
mname=input("Enter middle name ")
lname=input("Enter last name ")
dob=input("Enter DOB YYYY-MM-DD ")
dob=dates.datetime.strptime(dob,'%Y-%m-%d')
dob=dob.date()
gender=input("Enter gender ")
nationality=input("Enter nation ")
city=input("Enter city ")
state=input("Enter state ")
pin=int(input("Enter pincode "))
q=input("Enter qualification")
sal=int(input("Enter salary"))
pan=input("Enter panid")
req_date=dates.datetime.now()

mydb = mysql.connector.connect(host=cfg.names["host1"], user=cfg.names["user1"],
                               passwd=cfg.names["passwd1"], database=cfg.names["database1"])
mycursor = mydb.cursor()

mycursor.execute("INSERT INTO request_info (Firstname, Middlename, Lastname,Dob,Gender, "
                 "Nationality, City, State, Pincode, Qualification, Salary,PanID) "
                 "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" ,
                 (fname, mname, lname, dob, gender, nationality, city, state,
                 pin,q, sal, pan))
mydb.commit()

mycursor.execute("select request_date from request_info where Request_id = "
                 "(select max(Request_id) "
                 "from request_info group by PanID having PanID='{}')".format(pan))

value = mycursor.fetchone()
print(value[0])
DAY_S1=0
REQ=str(req_date.date())
str2=re.split('-',REQ)
val4=int(str2[0])
val5=int(str2[1])
val6=int(str2[2])
d1=date(val4,val5,val6)
print(d1)
if value[0] is not None:
    VALUE1=str(value[0].date())
    print(VALUE1 , REQ)
    str1=re.split('-',VALUE1)
    val1=int(str1[0])
    val2=int(str1[1])
    val3=int(str1[2])

    d0=date(val1,val2,val3)
    day_s1=(d1-d0).days

    print(DAY_S1)

    mycursor.execute("update request_info set request_date = %s where PanID= %s", (d1,pan))

else:
    mycursor.execute("update request_info set request_date = %s where PanID= %s", (d1, pan))

FLAG=1
age=check_age1(dob)
STATEMENT=""
if FLAG==1:
    STR4=check_age(age,gender)
    if STR4!="Eligible":
        FLAG=0
        STATEMENT=STR4

if FLAG==1:
    STR5=nation(nationality)
    if STR5!="Eligible":
        FLAG=0
        STATEMENT=STR5

if FLAG==1:
    STR2=check_state(state)
    if STR2!="Eligible":
        FLAG=0
        STATEMENT=STR2

if FLAG == 1:
    STR3=salary(sal)
    if STR3!="Eligible":
        FLAG=0
        STATEMENT=STR3

if FLAG==1:
    STR4=check_five(DAY_S1)
    if STR4!="Eligible":
        FLAG=0
        STATEMENT=STR4

mycursor.execute("select max(Request_id) from request_info")
rid=mycursor.fetchone()
request_id=int(rid[0])

if FLAG==1:
    RESPONSE="Success"
    dict1={"Request_id":request_id,"response":RESPONSE}
    dictation=json.dumps(dict1)
    print(dictation)
    mycursor.execute("INSERT INTO response_info(Request_id,response) "
                     "VALUES ('{}','{}')".format(request_id,dictation))
    mydb.commit()
else:
    RESPONSE="Failure"
    dict1 = {"Request_id": request_id, "response": RESPONSE,"reason":STATEMENT}
    dictation = json.dumps(dict1)
    print(dictation)
    mycursor.execute("INSERT INTO response_info(Request_id,response) "
                     "VALUES ('{}','{}')".format(request_id, dictation))
    mydb.commit()
