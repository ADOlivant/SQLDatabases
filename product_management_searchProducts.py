import sqlite3

from create_product_table import *
from delete_existing_product import *
from insert_product_data import *
from select_existing_products import *
from update_product_data import *

from product_management_window import *

def product_search_menu():
    print()
    print('~ ~ ~ Search Products SubMenu ~ ~ ~')
    print('1.  Search by ProductID number')
    print('2.  Search by exact name')
    print('3.  Search by name containing values')
    print('4.  Search by Price')
    print('5.  Search for products below value')
    print('6.  Search for products above value')
    print('99. Return to Product Table Menu')

def get_submenu_choice():
    valid = False
    choice = None 
    while not valid:
        try:
            choice = int(input("Please select an option: "))
            if (choice >= 1 and choice <=6) or choice == 99:
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

def search_one(data,sql):
    with sqlite3.connect("coffee_shop.db") as db:
        cursor = db.cursor()
        cursor.execute(sql)
        products = cursor.fetchall()
        return products

def view_all_results(products):
    print("{0:^11} | {1:<30} | {2:>5}".format("ProductID","Name","Price"))
    for product in product:
        print("{0:^11} | {1:<30} | {2:>5}".format(product[0],product[1],product[2]))

def search_main():
    zubchoice = None
    while zubchoice!= 99:
        product_search_menu()
        zubchoice = get_submenu_choice()
        if zubchoice == 1:
            #1. Search by ProductID number
            search_by_product_id_number()
        elif zubchoice == 2:
            #2. Search by exact name.
            name = str(input("Please enter a Product Name you wish to search: "))
            sql = "select ProductID,Name,Price from Product where Name='?'"
            products = search_one((name,),sql)
            print()
            print("¬ ¬ ¬ RESULT ¬ ¬ ¬")
            print()
            print("Search Parameter: {0}".format(name))
            view_all_results(products)

def search_by_product_id_number():
    products = select_all_products()
    valid = False
    id = None
    while not valid:
        try:
            id = int(input("Please select a ProductID you wish to search: "))
            if id >= products[0][0] and id <= products[len(products)-1][0]:
                checker = select_product(id)
                checker = checker[0]
                valid = True
            else:
                print()
                if id == 0:
                    print("*** Zero Error ***")
                    print("You have entered 0 as your search term this is a")
                    print("special number within this program as the")
                    print("exit key, and has reverted your previous.")
                    print("choice to no value so not to exit the program.")
                    id = None
                else:
                    print("*** No ProductID (Boundary) ***")
                    print("There is currently no product with that ProductID.")
                print()
        except TypeError:
            print()
            print("*** No ProductID (Type) ***")
            print("There is currently no product with that ProdcutID.")
            print() 
        except ValueError:
            print()
            print("*** Value Error ***")
            print("Please ensure you supply a integer only.")
            print()
        else:
            valid = True
    product = select_product(id)
    if valid:
        print()
        print("¬ ¬ ¬ RESULT ¬ ¬ ¬")
        print("The ProductID, {0}, has reutrned the following data:".format(id))
        print("Name of Product: {0}".format(product[0]))
        print("Price of Product: £{0}".format(product[1]))
        print()
            
            
        
        
