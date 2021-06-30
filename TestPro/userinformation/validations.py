"""validations.py"""
import json
import datetime as dt

def check_vali(dob,gender,nationality,state,salary):
    FLAG_NAME = 0
    if FLAG_NAME == 0:
        """validate age method"""
        dob = dt.datetime.strptime(dob, '%Y-%m-%d')
        dob = dob.date()
        today = dt.date.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

        if gender == "M":
            if age < 21:
                RESPONSE_NAME= "Invalid"
                REASON_NAME="Invalid age"
                FLAG_NAME=1
            else:
                RESPONSE_NAME="Valid"
        else:
            if age < 18:
                RESPONSE_NAME = "Invalid"
                REASON_NAME = "Invalid age"
                FLAG_NAME = 1
            else:
                RESPONSE_NAME='Valid'

    if FLAG_NAME == 0:
        """validate nationality method"""
        nationality = nationality.lower()
        if nationality == "indian" or nationality == "american":
            RESPONSE_NAME = "Valid"
        else:
            RESPONSE_NAME = "Invalid"
            REASON_NAME = "Invalid nationality"
            FLAG_NAME=1

    if FLAG_NAME == 0:
        """validate state method"""
        state = state.lower()
        state = state.replace(" ", "")
        states = ["andhrapradesh", "arunachalpradesh",
                  "assam", "bihar", "chhattisgarh", "karnataka",
                  "madhyapradesh","odisha","tamilnadu","telangana","westbengal"]
        if state in states:
            RESPONSE_NAME= "Valid"
        else:
            RESPONSE_NAME= "Invalid"
            REASON_NAME = "Invalid state"
            FLAG_NAME = 1

    if FLAG_NAME == 0:
        """validate salary method"""
        salary = int(salary)
        if salary>=10000 and salary<=90000:
            RESPONSE_NAME = "Valid"
        else:
            RESPONSE_NAME = "Invalid"
            REASON_NAME = "Invalid Salary"
            FLAG_NAME = 1
    if FLAG_NAME == 0:
        REASON_NAME= "Success"

    dictation = {"Response ": RESPONSE_NAME, "Reason ": REASON_NAME}
    dictation = json.dumps(dictation)
    return dictation