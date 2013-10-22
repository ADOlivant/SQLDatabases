import sqlite3

def query(db_name,sql,data):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("""PRAGMA foreign_keys = ON""")
        cursor.execute(sql,data)
        db.commit()

if __name__ == "__main__":
    sql = "UPDATE ProductType set ProductTypeID = 57 where ProductTypeID = 1"
    sql = "DELETE FROM ProductType WHERE ProductTypeID = 57"
    query(sql,())
