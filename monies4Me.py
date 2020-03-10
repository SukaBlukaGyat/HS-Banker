#Form Tutor Management System
import sys #this allows you to use the sys.exit command to quit/logout of the application
import time
def main():
    login()
    
def login():
    username="SukaBluka"
    password="Flee1"
    print("Enter username : ")
    answer1=input()
    print("Enter password : ")
    answer2=input()
    if answer1==username and     answer2==password:
        print("Welcome - Access Granted")
        menu()
    else:
        print("Wrong Username or Password")
        login()

def menu():
    print("************MAIN MENU**************")
    #time.sleep(1)
    print()

    choice = input("""
                      A: Enter New Expense
                      B: Enter New Deposit
                      C: Search by ID number
                      D: Produce Reports
                      X: Quit/Log Out

                      Please enter your choice: """)

    if choice == "A" or choice =="a":
        enterNewExpense()
    elif choice == "B" or choice =="b":
        enterNewDeposit()
    elif choice == "C" or choice =="c":
        searchExpenses()
    elif choice=="D" or choice=="d":
        produceExpenseReport()
    elif choice=="X" or choice=="x" or choice== "Exit" or choice== "exit":
        sys.exit
    else:
        print("You must only select either A, B, C, D, or Exit")
        print("Please try again")
        menu()

def enterNewExpense():
    print("************NEW EXPENSE**************")

    typeOfExpense = input("""What type of expense is it?:
                                A: Food
                                B: Gas
                                C: SchoolLunch
                                D: SchoolExpense
                                X: Exit
                                
                                Please Enter your Choice: """)
    
    if typeOfExpense == "A" or typeOfExpense =="a":
        print("You Have Chosen A")
        time.sleep(1)
        enterNewExpense()
    elif typeOfExpense == "B" or typeOfExpense =="b":
        print("You Have Chosen B")
        time.sleep(1)
        enterNewExpense()
    elif typeOfExpense == "C" or typeOfExpense =="c":
        print("You Have Chosen C")
        time.sleep(1)
        enterNewExpense()
    elif typeOfExpense=="D" or typeOfExpense=="d":
        print("You Have Chosen D")
        time.sleep(1)
        enterNewExpense()
    elif typeOfExpense=="X" or typeOfExpense=="x" or typeOfExpense== "Exit" or typeOfExpense== "exit":
        menu()
    else:
        print("You must only select either A, B, C, D, or Exit")
        print("Please try again")
        enterNewExpense()
    pass
    #Teacher will enter student details manually
    #These will be appended to the csv file

def enterNewDeposit():
    print
    pass
#Teacher can press a button to view all students at a glance

def searchExpenses():
    pass
    #Teacher can input an ID number and display the relevant student's details

def produceExpenseReport():
    pass
    #Teacher can produce clever reports such as:
    #a) list of names of males and email addresses (to email a reminder about boys football club)
    #b) list of names of females in specific postcode (to remind them of a girls coding club in the area)
    #c) list of all names, birthdays and addresses (to send out birthday cards!)
    
    
#the program is initiated, so to speak, here
main()
