import sqlite3

def select_all_products(db_name):
	with sqlite3.connect(db_name) as db: 
		cursor = db.cursor()
		cursor.execute("""SELECT * FROM Product""")
		products = cursor.fetchall()
		return products

def select_product(db_name,id):
	with sqlite3.connect(db_name) as db:
		cursor = db.cursor()
		cursor.execute("""SELECT Name,Price FROM Product WHERE ProductID=?""", (id,))
		product = cursor.fetchone()
		return product

def search_product(db_name,product):
        with sqlite3.connect(db_name) as db:
                cursor = db.cursor()
                cursor.execute("""SELECT * FROM Product WHERE Name=?""",(product,))
                results = cursor.fetchall()
                return results
                

if __name__ == "__main__": 
	products = select_all_products()
	print(products)
	product = select_product(3)
	print(product)
