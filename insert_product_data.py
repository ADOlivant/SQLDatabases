import sqlite3

def insert_data(db_name,values):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = """INSERT INTO Product (Name, Price) VALUES (?,?)"""
        cursor.execute(sql,values)
        db.commit()

if __name__ == "__main__":
    products = [("Latte",1.35),("Mocha",2.4),("Green Tea",1.20),("Black Tea",1),("Americano",1.5)]
    for product in products:
        insert_data(product)
        
