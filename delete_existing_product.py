import sqlite3

def delete_product(db_name,data): 
	with sqlite3.connect(db_name) as db: 
		cursor = db.cursor()
		sql = """DELETE FROM Product WHERE Name=?"""
		cursor.execute(sql,data)
		db.commit()

def delete_product_by_id(db_name,id):
        with sqlite3.connect(db_name) as db:
                cursor = db.cursor()
                sql = """DELETE FROM Product WHERE ProductID=?"""
                cursor.execute(sql,(id,))
                db.commit()

if __name__ == "__main__": 
	data = ("Green Tea",)
	delete_product(data)
