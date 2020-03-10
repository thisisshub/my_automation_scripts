import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
# do not forget to share client email id from json to sheets
creds = ServiceAccountCredentials.from_json_keyfile_name('My First Project-e4de45f2cf3a.json', scope)
client = gspread.authorize(creds)

sheet = client.open('attendance').sheet1
data = sheet.get_all_values()

day = datetime.today().strftime('%A')

Monday = ['DELAB','CSA','DS','DM','DE']
Tuesday = ['DE','DM','DS','OOP','DM','TE']
Wednesday = ['OOPLAB','DS','DE','CSA','TE']
Thursday = ['CSA','OOP','DM','OOP','CSALAB']
Friday = ['DSLAB','OOP','CSA','DS','DE'] 

# below functions update column C in spreadsheet

def DM1():
    val = int(sheet.acell('B2').value)
    val = val + 1
    sheet.update_acell('B2', val)    
def DS1():
    val = int(sheet.acell('B3').value)
    val = val + 1
    sheet.update_acell('B3', val)
def CSA1():
    val = int(sheet.acell('B4').value)
    val = val + 1
    sheet.update_acell('B4', val)
def OOP1():
    val = int(sheet.acell('B5').value)
    val = val + 1
    sheet.update_acell('B5', val)
def DE1():
    val = int(sheet.acell('B6').value)
    val = val + 1
    sheet.update_acell('B6', val)
def TE1():
    val = int(sheet.acell('B7').value)
    val = val + 1
    sheet.update_acell('B7', val)

def DELAB1():
    val = int(sheet.acell('B9').value)
    val = val + 1
    sheet.update_acell('B9', val)

def OOPLAB1():
    val = int(sheet.acell('B10').value)
    val = val + 1
    sheet.update_acell('B10', val)

def CSALAB1():
    val = int(sheet.acell('B11').value)
    val = val + 1
    sheet.update_acell('B11', val)

def DSLAB1():
    val = int(sheet.acell('B12').value)
    val = val + 1
    sheet.update_acell('B12', val)

# below functions update column B in spreadsheet
    
def DM():
    val = int(sheet.acell('C2').value)
    val = val + 1
    sheet.update_acell('C2', val)    
def DS():
    val = int(sheet.acell('C3').value)
    val = val + 1
    sheet.update_acell('C3', val)
def CSA():
    val = int(sheet.acell('C4').value)
    val = val + 1
    sheet.update_acell('C4', val)
def OOP():
    val = int(sheet.acell('C5').value)
    val = val + 1
    sheet.update_acell('C5', val)
def DE():
    val = int(sheet.acell('C6').value)
    val = val + 1
    sheet.update_acell('C6', val)
def TE():
    val = int(sheet.acell('C7').value)
    val = val + 1
    sheet.update_acell('C7', val)

def DELAB():
    val = int(sheet.acell('C9').value)
    val = val + 2
    sheet.update_acell('C9', val)

def OOPLAB():
    val = int(sheet.acell('C10').value)
    val = val + 2
    sheet.update_acell('C10', val)

def CSALAB():
    val = int(sheet.acell('C11').value)
    val = val + 2
    sheet.update_acell('C11', val)

def DSLAB():
    val = int(sheet.acell('C12').value)
    val = val + 2
    sheet.update_acell('C12', val)

def function_to_decide_day():
    if day == 'Sunday':
        pass    

    elif day == 'Saturday':
        print (day) # change this to actual attendance        
        
    if day == 'Monday':
        print (Monday)
        x = list(map(int, input('Which classes did you attend?')))
        switch = {0:DELAB1, 1:CSA1, 2:DS1, 3:DM1, 4:DE1}
        if x == 'all':
            switch[range(0,4)]()

    if day == 'Tuesday':
        DE1()
        DM1()
        DS1()
        OOP1()
        DM1()
        TE1()
        DE()
        DM()
        DS()
        OOP()
        DM()
        TE()

    if day == 'Wednesday':
        OOPLAB1()
        DS1()
        DE1()
        CSA1()
        TE1()
        OOPLAB()
        DS()
        DE()
        CSA()
        TE()
    
    if day == 'Thursday':
        CSA1()
        OOP1()
        DM1()
        OOP1()
        CSALAB1()
        CSA()
        OOP()
        DM()
        OOP()
        CSALAB()

    if day == 'Friday':
        DSLAB1()
        OOP1()
        CSA1()
        DS1()
        DE1()
        DSLAB()
        OOP()
        CSA()
        DS()
        DE()

percent = sheet.col_values(4)
print (percent)
function_to_decide_day()
