#Check for valid date and in case a INVALID Date is given, then it is used to give a alert message
from datetime import datetime
def get_valid_date(prompt):
    user_input = prompt
    try:
        datetime.strptime(user_input, "%d-%m-%Y")
        return True
    except ValueError:
        return False


#Check for valid DOB , This is mainly for the TEStCAse Purpose 
def check_valid_date(date):
    try:
        datetime.strptime(date, "%d-%m-%Y")
        return False
    except ValueError:
        print("Invalid date format! Please enter in DD-MM-YYYY format.")
        return(True)
    
    
    
    
