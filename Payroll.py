print("Welcome to payroll")
InputPrompt = True
while True:
    if InputPrompt == True:
        print("If you want to add a new employee input 'N'")
        print("If you want to update an employees record input 'M'")
        print("If you want to delete an employees record input 'D'")
        print("If you want to print an employee pay slip input 'P'")
        print("If you want to display an employees record input R")
        print("To quit input 'Q'")
        InputPrompt = False

    MainInput = input("Please select your option by inputting 'N', 'M', 'P', 'D' or 'Q': ")

    if MainInput == "Q" or MainInput == "q":
        print("Thank you for using Payroll :)")
        break
    elif MainInput == "N" or MainInput == "n":
        InputPrompt = True
        print("create employee")
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
    else:
        print("Invalid input please try again")
