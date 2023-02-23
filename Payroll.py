import datetime as date


class employee:
    def __init__(self, uid, name, address, phonenumber, joindate, designation, grade, loan):
        self.uid = uid
        self.name = name
        self.address = address
        self.phonenumber = phonenumber
        self.joindate = joindate
        self.designation = designation
        self.grade = grade
        self.loan = loan

def linebreaks():
    for x in range(20):
        print("")

def employeecreate():
    linebreaks()

    name = input("What is the employees name: ")
    address = input("What is the employees address: ")
    while True:
        try:
            phonenumber = str(input("What is the employees phone number: "))
            break
        except:
            print("Phone number was not inputted correctly, please try again")
    maxyear =  date.datetime.now().year

    while True:
        print("When did the employee join(DD/MM/YYYY)")
        daycheck = False
        monthcheck = False
        yearcheck = False
        try:

            while yearcheck == False:
                year = int(input("Year: "))
                if year >= 1900 and year <= maxyear:
                    yearcheck = True
                    year = str(year)
                else:
                    print("Unacceptable Year")

            while monthcheck == False:
                month = int(input("Month: "))
                if month >= 1 and month <= 12:
                    monthcheck = True
                    month = str(month)
                else:
                    print("Unacceptable Month")

            if month == "1" or month == "3" or month == "5" or month == "7" or month == "8" or month == "10" or month == "12":
                maxday = 31
            elif month == "4" or month == "6"  or month == "9" or month == "11":
                maxday = 30
            elif month == "2":
                maxday = 28
            else:
                print("Invalid month inputted!!!")

            while daycheck == False:
                day = int(input("Day: "))
                if day >= 1 and day <= maxday:
                    daycheck = True
                    day = str(day)
                else:
                    print("Unacceptable Day")

            break
        except:
            print("This field only accepts integers")

    joinyear = (day+"/"+month+"/"+year)
    print (joinyear)

    designation = input("What is the employees designation: ")
    grade = str(input("What is the employees grade: "))
    loan = str(input("What is the employees loan: "))

    File = open("Employees.txt", "r")
    S1 = File.readlines()
    File.close()
    try:
        for line in S1:
            last=line
        last=last.split(",")
        UID = int(last[0])+1
        File = open("Employees.txt", "a")
        File.write("\n"+str(UID)+","+name+","+address+","+phonenumber+","+joinyear+","+designation+","+grade+","+loan)



    except:
        File = open("Employees.txt", "w")
        line = ("1"+","+name+","+address+","+phonenumber+","+joinyear+","+designation+","+grade+","+loan)
        File.write(line)


print("Welcome to payroll")
InputPrompt = True

while True:
    if InputPrompt == True:
        print("If you want to add a new employee input 'N'")
        print("If you want to update an employees record input 'M'")
        print("If you want to delete an employees record input 'D'")
        print("If you want to print an employee pay slip input 'P'")
        print("If you want to display an employees record input 'R'")
        print("To quit input 'Q'")
        InputPrompt = False

    MainInput = input("Please select your option by inputting 'N', 'M', 'P', 'D', 'R' or 'Q': ")

    if MainInput == "Q" or MainInput == "q":
        print("Thank you for using Payroll :)")
        break
    elif MainInput == "N" or MainInput == "n":
        InputPrompt = True
        employeecreate()
        linebreaks()
        InputPrompt = True

    elif MainInput == "M" or MainInput == "m":
        InputPrompt = True
        print("update employee")

    elif MainInput == "D" or MainInput == "d":
        InputPrompt = True
        print("delete employee")

    elif MainInput == "P" or MainInput == "p":
        InputPrompt = True
        print("Print")

    elif MainInput == "R" or MainInput == "r":
        InputPrompt = True
        print("Search employee")
        File = open("Employees.txt", "r")
        # print(file.readlines())
        employees=[]
        for line in File:
            employees.append(line)
        File.close()
        print(employees)

    else:
        print("Invalid input please try again")

