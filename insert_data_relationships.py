import sqlite3

def query(db_name,sql,data):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute(sql,data)
        db.commit()

def insert_product_type_data(records):
    sql = "INSERT into ProductType(Description) values (?)"
    for record in records:
        query(sql,record)

def insert_product_data(records):
    sql = "INSERT into Product (Name,Price,ProductTypeID) values (?,?,?)"
    for record in records:
        query(sql,record)

if __name__ == "__main__":
    product_types = [("Coffe",),("Tea",),("Cold Drink",)]
    insert_product_type_data(product_types)
    products = [("Latte",1.35,1),("Mocha",2.4,1),("Green Tea",1.20,2),("Black Tea",1.2,2),("Americano", 1.50,1),("Raspberry",3.5,3),("Lemonade",2.85,3)]
    #products = [("Raspberry",3.25,4),("Cookie",1.15,5)]
    insert_product_data(products)
