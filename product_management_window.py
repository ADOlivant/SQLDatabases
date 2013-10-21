import sqlite3

from create_product_table import *
from delete_existing_product import *
from insert_product_data import *
from select_existing_products import *
from update_product_data import *

from product_management_getChoices import *
from product_management_searchProducts import *

def product_table_menu():
    print()
    print('~ ~ ~ Product Table Menu ~ ~ ~')
    print('1. (Re)Create Product Table')
    print('2. Add new product')
    print('3. Edit exisiting product')
    print('4. Delete existing product')
    print('5. Search for products')
    print('0. Exit')
    print()

def view_table(items):
    print('{0:^11} | {1:^30} | {2:^5}'.format('ProductID','Name','Price'))
    for item in items:
        print('{0:^11} | {1:<30} | £{2:>5.2f}'.format(item[0],item[1],item[2]))

def get_values():
    name = str(input("Please enter the (new) name for the product: "))
    price = float(input("Please enter the (new) price for the product: "))
    return (name,price)

def main():
    db_name = "coffee_shop.db"
    choice = None
    while choice != 0:
        product_table_menu()
        choice = get_menu_choice()
        if choice == 1:
            #1. (Re)Create Product Table
            table_sql = """create table Product
                     (ProductID integer,
                     Name text,
                     Price real,
                     primary key(ProductID)"""
            create_table(db_name,"Product",table_sql)
        elif choice == 2:
            #2. Add new product
            values = get_values()
            insert_data(values)
        elif choice == 3:
            #3. Edit exisiting product
            products = select_all_products()
            view_table(products)
            print()
            choice = get_table_choice(1,products[len(products)-1][0])
            product = select_product(choice)
            check = input('Are you sure you wish to edit details about {0}? (y/n): '.format(product[0]))
            if check == "y":
                name = str(input("Please enter a new name for {0}: ".format(product[0])))
                price = float(input("Please enter a price for {0}: ".format(name)))
                update_product((name,price,choice))
                print("Selected data has been changed in the database.")
            else:
                print("Selected data has not be editied.")            
        elif choice == 4:
            #4. Delete existing product
            products = select_all_products()
            view_table(products)
            print()
            choice = get_table_choice(1,products[len(products)-1][0])
            product = select_product(choice)
            check = input('Are you sure you wish to delete {0}? (y/n): '.format(product[0]))
            if check == "y":
                delete_product_by_id(choice)
                print("Selected data has been removed from database.")
            else:
                print("Selected data has not be deleted.")
        elif choice == 5:
            #5. Search for products
            product = input("Please enter the name of the product to search for: ")
            results = search_product(product)
            view_table(results)
            
if __name__ == "__main__":
    main()
