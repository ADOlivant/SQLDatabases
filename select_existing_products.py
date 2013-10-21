import sqlite3

def select_all_products():
	with sqlite3.connect("coffee_shop.db") as db: 
		cursor = db.cursor()
		cursor.execute("select * from Product")
		products = cursor.fetchall()
		return products

def select_product(id):
	with sqlite3.connect("coffee_shop.db") as db:
		cursor = db.cursor()
		cursor.execute("select Name,Price from Product where ProductID=?", (id,))
		product = cursor.fetchone()
		return product

def search_product(product):
        with sqlite3.connect("coffee_shop.db") as db:
                cursor = db.cursor()
                cursor.execute("""SELECT * FROM Product WHERE Name=?""",(product,))
                results = cursor.fetchall()
                return results
                

if __name__ == "__main__": 
	products = select_all_products()
	print(products)
	product = select_product(3)
	print(product)
