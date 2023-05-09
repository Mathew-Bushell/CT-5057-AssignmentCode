from datetime import datetime
from tabulate import tabulate
from time import sleep

class Tree:
    def __init__(self, data):
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
        #because its designed to accept an split line in the form of a list the data compares have to compare from the UID value aka pos 0
        if self.data:
            if int(data[0]) < int(self.data[0]):
                if self.left is None:
                    self.left = Tree(data)
                else:
                    self.left.insert(data)
            elif int(data[0]) > int(self.data[0]):
                if self.right is None:
                    self.right = Tree(data)
                else:
                    self.right.insert(data)
            else:
                self.data = data
    #Binary searches the tree for the targeted value
    def binarySearch(self, target):
        if target < int(self.data[0]):
            if self.left is None:
                return str("There is no employee with the ID "+str(target))
            return self.left.binarySearch(target)
        elif target > int(self.data[0]):
            if self.right is None:
                return str("There is no employee with the ID "+str(target))
            return self.right.binarySearch(target)
        else:
            return str(self.data)



# this creates a space between different outputs to reduce clutter when using the program
def linebreaks():
    for x in range(20):
        print("")

#returns a valid date as of the current date based on the users input
def getADate(textPrompt):
    maxyear = datetime.now().year

    while True:
        print(textPrompt)
        daycheck = False
        monthcheck = False
        yearcheck = False
        try:
        #requests a valid year from the user
            while yearcheck == False:
                year = int(input("Year: "))
                if year >= 1900 and year <= maxyear:
                    yearcheck = True
                    year = str(year)
                else:
                    print("Unacceptable Year")
        #requests a valid month from the user
            while monthcheck == False:
                month = int(input("Month: "))
                if month >= 1 and month <= 12:
                    monthcheck = True
                    month = str(month)
                else:
                    print("Unacceptable Month")
        #requests a valid day from the user dependent on what month the user previously entered
            if month == "1" or month == "3" or month == "5" or month == "7" or month == "8" or month == "10" or month == "12":
                maxday = 31
            elif month == "4" or month == "6" or month == "9" or month == "11":
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

    joinyear = (day + "/" + month + "/" + year)
    #returns the year to be used in other functions
    return(joinyear)

#accepts a series of inputs from the user to create en employee record
def employeecreate():
    linebreaks()
    newfile = False
    try:
        File = open("Employees.txt", "r")
        UIDComp = File.readlines()
        File.close()
    except:
        File = open("Employees.txt", "w")
        File.close()
        File = open("Employees.txt", "r")
        UIDComp = File.readlines()
        File.close()
        newfile = True
    while True:
        match=False
        try:
            UID = int(input("What is the employees registration number:"))
        except:
            print("Registration number needs to be a whole number")
            continue
    #only accepts unique registration numbers
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

    joinyear = getADate("When did the employee join(DD/MM/YYYY)")
    designation = input("What is the employees designation: ")
    #only accepts one of the valid grade options
    while True:
        grade = str(input("What is the employees grade(I, II, III, IV): "))
        if grade == "I" or grade == "II" or grade == "III" or grade == "IV":
            break
        else:
            print("Invalid Input")
    loan = str(input("What is the employees loan: "))
    salary = str(input("What is the employees salary(per hour): "))
    hours = str(input("What is the employees standard work hours: "))
    travel = str(input("What is the employees travel allowance: "))
    File = open("Employees.txt", "r")
    S1 = File.readlines()
    File.close()
    #adds employee record to Employees.txt
    #if there is no Employees.txt the program will create a new one and add the profile to it
    if newfile == False:
        File = open("Employees.txt", "a")
        File.write("\n"+str(UID)+","+name+","+address+","+phonenumber+","+joinyear+","+designation+","+grade+","+loan+","+salary+","+hours+","+travel+",5,8")



    elif newfile == True:
        File = open("Employees.txt", "w")
        line = (str(UID)+","+name+","+address+","+phonenumber+","+joinyear+","+designation+","+grade+","+loan+","+salary+","+hours+","+travel+",5,8")
        File.write(line)
        File.close()

#waits for a user input so they can read whats on screen before the program moves on
def waitForUserInput():
    input("Press enter to continue...")

def listemployee():
    # fills the splitline queue with employee data, prints it using tabulate and then empties the queue
    File = open("Employees.txt","r")
    splitFile = [["Registry", "Name", "Address", "Phone Number", "Join Date", "Role", "Grade", "Loan", "Hourly Pay", "Standard hours", "Travel Allowance", "House Allowance %", "Health Allowance %"]]
    for line in File:
        splitLine = line.split(',')
        splitFile.append(splitLine)

    print(tabulate(splitFile, headers="firstrow"))

    for x in splitFile:
        splitFile.pop(0)
    # print(splitFile)
    waitForUserInput()

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
    return(employees)

def percentage(total, percent):
    #calcultes the percetnage of a total with a provided percent
    return (int(total) / 100) * percent

def mergesort(array):
    if len(array) > 1:
        # finds the middle of the array
        mid = len(array) // 2

        #divides array elements into left and right
        L = array[:mid]
        R = array[mid:]

        #seperate halves are sorted
        mergesort(L)
        mergesort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        #once the array is split it is sorted
        while i < len(L) and j < len(R):
            if int(L[i][0]) <= int(R[j][0]):
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1

        # Checks if any elements are left
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1

def interpolation_search(fullArray, target):
    #sets up array positions
    array = []
    for x in fullArray:
        array.append(int(x[0]))
    # print(array)
    n = len(array)
    low = 0
    high = n - 1

    while low <= high and target >= array[low] and target <= array[high]:
        # Estimate the position of the target value using linear interpolation
        pos = low + int(((target - array[low]) / (array[high] - array[low])) * (high - low))

        if target == array[pos]:
            return pos

        #if the target is higher than the pointer positon it will move the lower position up
        if array[pos] < target:
            low = pos + 1
        # if the target is lower than the pointer positon it will move the higher position down
        else:
            high = pos - 1

    return -1  # Target value not found in the array

def mainMenu():
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
            sleep(3)
            break

        elif MainInput == "N" or MainInput == "n":
            InputPrompt = True
            employeecreate()
            linebreaks()
            InputPrompt = True

        elif MainInput == "M" or MainInput == "m":
            linebreaks()
            InputPrompt = True
            employeeArray = []
            file = open("Employees.txt", "r")
            employees = file.readlines()
            file.close()
            for line in employees:
                editedLine = line.replace("\n", "")
                editedLine = editedLine.split(",")
                employeeArray.append(editedLine)
            # print(employeeArray)
            mergesort(employeeArray)
            # print(employeeArray)
            while True:
                try:
                    target = int(input("Enter the Employee ID of the employee you would like to modify: "))
                    targetPos = interpolation_search(employeeArray, target)
                    if targetPos != -1:
                        break
                    else:
                        print("No user has been found with this Employee ID")
                except:
                    print("Invalid Input, Employee IDs can only be numbers!")
            changeOptions = {"Employee Registration Number": 0, "Name": 1, "Address": 2, "Phone Number": 3,
                             "Join Date": 4, "Designation": 5, "Grade": 6, "Loan": 7, "Salary Per Hour": 8, "Hours": 9,
                             "Travel Allowance": 10, "House Allowance": 11, "Health Allowance": 12}
            while True:
                match = False
                changeTarget = input(
                    "What value would you like to modify:\nEmployee Registration Number\nName\nAddress\nPhone Nubmer\nJoin Date\nDesignation\nGrade\nLoan\nSalary Per Hour\nTravel Allowance\nHouse Allowance\nHealth Allowance\n")
                for x in changeOptions:
                    if changeTarget == x:
                        match = True
                if match == True:
                    break
                else:
                    print("Invalid Input!")
            if changeOptions[changeTarget] == 0 or changeOptions[changeTarget] == 3 or changeOptions[
                changeTarget] == 7 or changeOptions[changeTarget] == 8 or changeOptions[changeTarget] == 9 or \
                    changeOptions[changeTarget] == 10 or changeOptions[changeTarget] == 11 or changeOptions[
                changeTarget] == 12:
                while True:
                    try:
                        change = int(input("What would you like to change " + changeTarget + " to?(Ints only):"))
                        change = str(change)
                        break
                    except:
                        print("Invalid Input!")
            elif changeOptions[changeTarget] == 6:
                while True:
                    try:
                        change = str(input("What would you like to change " + changeTarget + " to?(I, II, III, IV):"))
                        if change == "I" or change == "II" or change == "III" or change == "IV":
                            break
                        else:
                            print("Invalid Input")
                    except:
                        print("Invalid Input!")
            elif changeOptions[changeTarget] == 4:
                change = getADate("What would you like to change the Join Date to?")
            else:
                while True:
                    try:
                        change = str(input("What would you like to change " + changeTarget + " to?(Strings Only):"))
                        break
                    except:
                        print("Invalid Input!")

            modifiedList = employeeArray[targetPos]
            modifiedList[changeOptions[changeTarget]] = change
            employeeArray[targetPos] = modifiedList
            # print(employeeArray)
            File = open("Employees.txt", "w")
            newFile = str()
            for line in employeeArray:
                if len(newFile) == 0:
                    newFile = newFile + line[0] + "," + line[1] + "," + line[2] + "," + line[3] + "," + line[4] + "," + \
                              line[5] + "," + line[6] + "," + line[7] + "," + line[8] + "," + line[9] + "," + line[
                                  10] + "," + line[11] + "," + line[12]
                else:
                    newFile = newFile + "\n" + line[0] + "," + line[1] + "," + line[2] + "," + line[3] + "," + line[
                        4] + "," + line[5] + "," + line[6] + "," + line[7] + "," + line[8] + "," + line[9] + "," + line[
                                  10] + "," + line[11] + "," + line[12]
            # print(newFile)
            File.write(newFile)
            File.close()
            print("File Modified")
            waitForUserInput()
            linebreaks()

        elif MainInput == "D" or MainInput == "d":
            linebreaks()
            InputPrompt = True
            employeeArray = []
            file = open("Employees.txt", "r")
            employees = file.readlines()
            file.close()
            for line in employees:
                editedLine = line.replace("\n", "")
                editedLine = editedLine.split(",")
                employeeArray.append(editedLine)
            # print(employeeArray)
            mergesort(employeeArray)
            # print(employeeArray)

            while True:
                try:
                    target = int(input("Enter the Employee ID: "))
                    targetPos = interpolation_search(employeeArray, target)
                    if targetPos != -1:
                        break
                    else:
                        print("No user has been found with this Employee ID")
                except:
                    print("Invalid Input, Employee IDs can only be numbers!")

            confirmation = input("Are you sure you want to delete this employee(Y/N)? ")
            if confirmation == "Y" or confirmation == "y":
                File = open("Employees.txt", "w")
                employeeArray.pop(targetPos)
                newFile = str()
                for line in employeeArray:
                    if len(newFile) == 0:
                        newFile = newFile + line[0] + "," + line[1] + "," + line[2] + "," + line[3] + "," + line[
                            4] + "," + line[5] + "," + line[6] + "," + line[7] + "," + line[8] + "," + line[9] + "," + \
                                  line[10] + "," + line[11] + "," + line[12]
                    else:
                        newFile = newFile + "\n" + line[0] + "," + line[1] + "," + line[2] + "," + line[3] + "," + line[
                            4] + "," + line[5] + "," + line[6] + "," + line[7] + "," + line[8] + "," + line[9] + "," + \
                                  line[10] + "," + line[11] + "," + line[12]
                # print(newFile)
                File.write(newFile)
                File.close()
                print("File Deleted")
            elif confirmation == "N" or confirmation == "n":
                print("Deletion Aborted")
            else:
                print("Invalid Input!")
            waitForUserInput()
            linebreaks()

        elif MainInput == "P" or MainInput == "p":
            InputPrompt = True
            linebreaks()
            employees = treebuild()
            target = int(input("Enter the ID of the employee you wish to print the pay slip of: "))
            slipDate = getADate("What is the date for the payslip(DD/MM/YYYY)")
            while True:
                try:
                    hours= int(input("How many hours has the employee worked this month: "))
                    break
                except:
                    print("Invalid Input")
            while True:
                try:
                    overtime = int(input("How many hours of overtime has the employee worked: "))
                    break
                except:
                    print("Invalid Input")
            employeeDetails = employees.binarySearch(target)
            
            try:
                head = [["Registry", "Name", "Travel Allowance", "House allowance", "Health allowance", "Deductions",
                         "Net Salary"]]
                tail = []
                print("Pay slip for " + slipDate)
                employeeDetails = employeeDetails.replace("[", "")
                employeeDetails = employeeDetails.replace("]", "")
                employeeDetails = employeeDetails.replace("'", "")
                employeeDetails = employeeDetails.split(",")
                # employeeDetails[10] = employeeDetails[10].replace("\n", "")
                # print(employeeDetails)
                tail.append(employeeDetails[0])
                tail.append(employeeDetails[1])
                if overtime > 0:
                    salary = (hours * (int(employeeDetails[9]) + overtime))
                else:
                    salary = (hours * int(employeeDetails[9]))
                # tail.append(salary)
                tail.append((employeeDetails[10])[:-2])
                tail.append(percentage(salary, int(employeeDetails[11])))
                tail.append(percentage(salary, int(employeeDetails[12].replace("\\n", ""))))
                deductions = percentage(salary, 20)
                tail.append(deductions)
                netSalary = salary - deductions
                tail.append(netSalary)
                head.append(tail)
                print(tabulate(head, headers="firstrow"))
                waitForUserInput()
                linebreaks()
            except:
                print(employeeDetails)

        elif MainInput == "L" or MainInput == "l":
            InputPrompt = True
            linebreaks()
            listemployee()
            linebreaks()

        elif MainInput == "R" or MainInput == "r":
            InputPrompt = True
            print("Search employee")
            linebreaks()
            employees = treebuild()
            while True:
                try:
                    target = int(input("Enter the ID of the employee view: "))
                    break
                except:
                    print("Invalid Input")
            employeeDetails = employees.binarySearch(target)

            try:
                head = [
                    ["Registry", "Name", "Address", "Phone Number", "Join Date", "Role", "Grade", "Loan", "Hourly Pay",
                     "Standard hours", "Travel Allowance", "House Allowance %", "Health Allowance %"]]
                tail = []
                employeeDetails = employeeDetails.replace("[", "")
                employeeDetails = employeeDetails.replace("]", "")
                employeeDetails = employeeDetails.replace("'", "")
                employeeDetails = employeeDetails.split(",")
                employeeDetails[12] = (employeeDetails[12])[:-2]

                head.append(employeeDetails)
                print(tabulate(head, headers="firstrow"))
                waitForUserInput()
                linebreaks()
            except:
                print(employeeDetails)

        else:
            print("Invalid input please try again")


# program start
#ensures the user has to login to be able to access the rest of the program
print("Welcome to payroll.exe, please log in.")
while True:
    username = input("What is your username:")
    password = input("What is your password:")
    if username == "Admin" and password == "Admin123":
        mainMenu()
        break
    else:
        print("Invalid username or password, Please try again!")