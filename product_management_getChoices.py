import sqlite3

from select_existing_products import *

def get_menu_choice():
    valid = False
    choice = None 
    while not valid:
        try:
            choice = int(input("Please select an option: "))
            if choice >= 0 and choice <=5:
                valid = True
            else:
                print()
                print("*** Value Error ***")
                print("Please ensure you enter a valid integer ")
                print("from the above list.")
                print()
        except ValueError:
            print()
            print("*** Type Error ***")
            print("Please ensure you supply a integer only.")
            print()
    return choice

def get_table_choice(min,max):
    valid = False
    choice = None 
    while not valid:
        try:
            choice = int(input("Please select an option from the table above: "))
            if choice >= min and choice <=max:
                    checker = select_product(choice)
                    checker = checker[0]
                    valid = True
            else:
                print()
                if choice == 0:
                    print("*** Zero Error ***")
                    print("You have entered 0 as your choice this is a")
                    print("special number within this program as the")
                    print("exit key, and has reverted your previous.")
                    print("choice to no value so not to exit the program.")
                    choice = None
                else:
                    print("*** Boundary Error ***")
                    print("Please ensure you only select an option")
                    print("listed above.")
                print()
        except TypeError:
            print()
            print("*** Type Error ***")
            print("The option you have selected does not")
            print("exisit.")
            print() 
        except ValueError:
            print()
            print("*** Value Error ***")
            print("Please ensure you supply a integer only.")
            print()               
    return choice
