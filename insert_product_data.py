import sqlite3

def insert_data(values):
    with sqlite3.connect("coffee_shop.db") as db:
        cursor = db.cursor()
        sql = "insert into Product (Name, Price) values (?,?)"
        cursor.execute(sql,values)
        db.commit()

if __name__ == "__main__":
    products = [("Latte",1.35),("Mocha",2.4),("Green Tea",1.20),("Black Tea",1),("Americano",1.5)]
    for product in products:
        insert_data(product)
        
