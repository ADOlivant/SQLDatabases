import sqlite3

def update_product(db_name,data): 
	with sqlite3.connect(db_name) as db: 
		cursor = db.cursor()
		sql = """UPDATE Product SET Name=?, Price=? WHERE ProductID=?"""
		cursor.execute(sql,data)
		db.commit()

if __name__ == "__main__": 
	data = ("Hot Chocolate",3.0,5)
	update_product(data)
