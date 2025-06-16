#Importing main method to run the test cases
from main import InBuilt_testcase

test_cases = [
    {"mpin": "2345",    "dob": "02-01-1998", "spouse_dob": "",            "anniversary_date": ""},
    {"mpin": "0201",    "dob": "02-01-1998", "spouse_dob": "",            "anniversary_date": ""},
    {"mpin": "1998",    "dob": "02-01-1998", "spouse_dob": "",            "anniversary_date": ""},
    {"mpin": "1508",    "dob": "02-01-1998", "spouse_dob": "15-08-1995",  "anniversary_date": ""},
    {"mpin": "0101",    "dob": "02-01-1998", "spouse_dob": "15-08-1995",  "anniversary_date": "01-01-2020"},
    {"mpin": "123456",  "dob": "",           "spouse_dob": "",            "anniversary_date": ""},
    {"mpin": "9374",    "dob": "02-01-1998", "spouse_dob": "",            "anniversary_date": ""},
    {"mpin": "1995",    "dob": "02-01-1998", "spouse_dob": "15-08-1995",  "anniversary_date": "01-01-2020"},
    {"mpin": "201401",  "dob": "02-01-1998", "spouse_dob": "15-08-1995",  "anniversary_date": "01-01-2014"},
    {"mpin": "0000",    "dob": "02-01-1998", "spouse_dob": "",            "anniversary_date": ""},
    {"mpin": "739204",  "dob": "02-01-1998", "spouse_dob": "",            "anniversary_date": ""},
    {"mpin": "1122",    "dob": "02-01-1998", "spouse_dob": "",            "anniversary_date": ""},
    {"mpin": "9802",    "dob": "02-01-1998", "spouse_dob": "",            "anniversary_date": ""},
    {"mpin": "654321",  "dob": "",           "spouse_dob": "",            "anniversary_date": ""},
    {"mpin": "7777",    "dob": "07-07-2007", "spouse_dob": "",            "anniversary_date": ""},
    {"mpin": "7392",    "dob": "02-01-1998", "spouse_dob": "",            "anniversary_date": "01-01-2020"},
    {"mpin": "02a1",    "dob": "02-01-1998", "spouse_dob": "",            "anniversary_date": ""},
    {"mpin": "123",     "dob": "02-01-1998", "spouse_dob": "",            "anniversary_date": ""},
    {"mpin": "1234567", "dob": "02-01-1998", "spouse_dob": "",            "anniversary_date": ""},
    {"mpin": "1212",    "dob": "12-12-2012", "spouse_dob": "12-12-2012",  "anniversary_date": "12-12-2012"},
]
#Iterating over the test case dataset
for i in test_cases:
    print("Mpin : ",i['mpin'])
    print(InBuilt_testcase(
        mpin=i['mpin'],
        dob=i['dob'],
        spouse_dob=i['spouse_dob'],
        anniversary_date=i['anniversary_date']
    ))