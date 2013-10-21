import sqlite3

def create_table(db_name,table_name,sql):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("select name from sqlite_master where name=?",(table_name,))
        result = cursor.fetchall()
        keep_table = True
        if len(result) == 1:
            response = input("The table {0} already exists, do you wish to recreate it? (y/n): ".format(table_name))
            if response == "y":
                keep_table = False
                print("The {0} table will be recreated - all exisiting data will be lost".format(table_name))
                cursor.execute("drop table if exists {0}".format(table_name))
                db.commit()
            else:
                print("The existing table was kept")
        else:
            keep_table = False
        if not keep_table:
            cursor.execute(sql)
            db.commit()

def create_customer_table():
    sql = """CREATE TABLE Customer
             (CustomerID integer,
             FirstName text,
             LastName text,
             Street text,
             Town text,
             PostCode text,
             TelephoneNumber text,
             EMailAddress text,
             PRIMARY KEY (CustomerID))"""
    create_table(db_name,"Customer",sql)

def create_customer_order_table():
    sql = """CREATE TABLE CustomerOrder
             (OrderID integer,
             Date text,
             Time text,
             CustomerID integer,
             PRIMARY KEY(OrderID)
             FOREIGN KEY(CustomerID) references Customer(CustomerID))"""
    create_table(db_name,"CustomerOrder",sql)

def create_product_type_table():
    sql = """CREATE TABLE ProductType
             (ProductTypeID integer,
             Description text,
             PRIMARY KEY(ProductTypeID))"""
    create_table(db_name,"ProductType",sql)

def create_product_table():
    sql = """create table Product
             (ProductID integer,
             Name text,
             Price real,
             ProductTypeID integer,
             primary key(ProductID)
             foreign key(ProductTypeID) references ProductType(ProductTypeID)
             ON UPDATE restrict ON DELETE restrict)"""
    create_table(db_name,"Product",sql)

def create_order_item_table():
    sql = """CREATE TABLE OrderItem
             (OrderItemID integer,
             OrderID integer,
             ProductID integer,
             Quantity integer,
             PRIMARY KEY(OrderItemID)
             FOREIGN KEY(OrderID) references CustomerOrder(OrderID)
             FOREIGN KEY(ProductID) references Product(ProductID))"""
    create_table(db_name,"OrderItem",sql)

if __name__ == "__main__":
    db_name = "coffee_shop_v6.db"
    create_customer_table()
    create_customer_order_table()
    create_product_table()
    create_product_type_table()
    create_order_item_table()
    
