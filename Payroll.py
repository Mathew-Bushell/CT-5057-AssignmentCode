print("Welcome to payroll")
while True:
    print("If you want to add a new employee input 'N'")
    print("If you want to update an employees record input 'M'")
    print("If you want to delete an employees record input 'D'")
    print("If you want to print an employee pay slip input 'P'")
    print("If you want to display an employees record input R")
    print("To quit input 'Q'")
    MainInput = input("Please select your option by inputting 'N', 'M', 'P', 'D' or 'Q': ")

    if MainInput == "Q" or MainInput == "q":
        break
    elif MainInput == "N" or MainInput == "n":
        print("create employee")
    elif MainInput == "M" or MainInput == "m":
        print("update employee")
    elif MainInput == "D" or MainInput == "d":
        print("delete employee")
    elif MainInput == "P" or MainInput == "p":
        print("Print")
    elif MainInput == "R" or MainInput == "r":
        print("Search employee")
    else:
        print("Invalid input please try again")
