import sqlite3

def update_product(data): 
	with sqlite3.connect("coffee_shop.db") as db: 
		cursor = db.cursor()
		sql = "update Product set Name=?, Price=? where ProductID=?"
		cursor.execute(sql,data)
		db.commit()

if __name__ == "__main__": 
	data = ("Hot Chocolate",3.0,5)
	update_product(data)
