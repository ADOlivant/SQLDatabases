import sqlite3

def delete_product(data): 
	with sqlite3.connect("coffee_shop.db") as db: 
		cursor = db.cursor()
		sql = "delete from Product where Name=?"
		cursor.execute(sql,data)
		db.commit()

def delete_product_by_id(id):
        with sqlite3.connect("coffee_shop.db") as db:
                cursor = db.cursor()
                sql = "delete from Product where ProductID=?"
                cursor.execute(sql,(id,))
                db.commit()

if __name__ == "__main__": 
	data = ("Green Tea",)
	delete_product(data)
