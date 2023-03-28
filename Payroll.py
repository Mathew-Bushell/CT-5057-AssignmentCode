import datetime as date
from tabulate import tabulate

class Employee:
    def __init__(self, uid, name, address, phonenumber, joindate, designation, grade, loan):
        self.uid = uid
        self.name = name
        self.address = address
        self.phonenumber = phonenumber
        self.joindate = joindate
        self.designation = designation
        self.grade = grade
        self.loan = loan

#used for guidance https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm
class Tree:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
    def PrintTree(self):
        #prints the data from left to right, used for testing
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()
    def insert(self,data):
        #compares the new value with the parent node and decides where it goes
        if self.data:
            if data[0] < self.data[0]:
                if self.left is None:
                    self.left = Tree(data)
                else:
                    self.left.insert(data)
            elif data[0] > self.data[0]:
                if self.right is None:
                    self.right = Tree(data)
                else:
                    self.right.insert(data)
            else:
                self.data = data
#note while maurice had an ID of 6 she was placed "last" in the tree.

def linebreaks():
    for x in range(20):
        print("")

def employeecreate():
    linebreaks()

    File = open("Employees.txt", "r")
    UIDComp = File.readlines()
    File.close()
    while True:
        match=False
        try:
            UID = int(input("What is the employees registration number:"))
        except:
            print("Registration number needs to be a number")
            continue

        for line in UIDComp:
           SplitLine = line.split(",")
           if UID == int(SplitLine[0]):
               print("Registration Number already in use")
               match = True
               break
        if match == False:
            break

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
    grade = str(input("What is the employees grade(I, II, III, IV): "))
    loan = str(input("What is the employees loan: "))
    salary = str(input("What is the employees salary(per hour): "))

    File = open("Employees.txt", "r")
    S1 = File.readlines()
    File.close()
    try:
        for line in S1:
            last=line
        last=last.split(",")
        UID = int(last[0])+1
        File = open("Employees.txt", "a")
        File.write("\n"+str(UID)+","+name+","+address+","+phonenumber+","+joinyear+","+designation+","+grade+","+loan+","+salary)



    except:
        File = open("Employees.txt", "w")
        line = (str(UID)+","+name+","+address+","+phonenumber+","+joinyear+","+designation+","+grade+","+loan)
        File.write(line)
        File.close()

def listemployee():
    # fills the splitline queue with employee data, prints it using tabulate and then empties the queue
    File = open("Employees.txt","r")
    splitFile = [["Registry", "Name", "Address", "Phone Number", "Join Date", "Role", "Grade", "Loan"]]
    for line in File:
        splitLine = line.split(',')
        splitFile.append(splitLine)

    print(tabulate(splitFile, headers="firstrow"))

    for x in splitFile:
        splitFile.pop(0)
    print(splitFile)
    input("Press enter to continue")

def treebuild():
    #builds a tree out of the data
    File = open("Employees.txt", "r")
    for line in File:
        try:
            splitLine = line.split(',')
            employees.insert(splitLine)
        except:
            splitLine = line.split(',')
            employees = Tree(splitLine)
    employees.PrintTree()


#Program Start
print("Welcome to payroll")
InputPrompt = True

while True:
    if InputPrompt == True:
        print("If you want to add a new employee input 'N'")
        print("If you want to update an employees record input 'M'")
        print("If you want to delete an employees record input 'D'")
        print("If you want to print an employee pay slip input 'P'")
        print("If you want to display an employees record input 'R'")
        print("If you want to display all employees in the system 'L'")
        print("To quit input 'Q'")
        InputPrompt = False

    MainInput = input("Please select your option by inputting 'N', 'M', 'P', 'D', 'R', 'L' or 'Q': ")

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
        treebuild()

    elif MainInput == "L" or MainInput == "l":
        InputPrompt = True
        linebreaks()
        listemployee()
        linebreaks()

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

