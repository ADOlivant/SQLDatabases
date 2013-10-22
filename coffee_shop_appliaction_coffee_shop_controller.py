import sqlite3

from insert_data_relationships import *

class Coffee_Shop_Controller():

    def __init__ (self):
        self.database = "coffee_shop_app.db"

    def query_manipulate(self,sql,data):
        query(self.database,sql,data)

    def query_search(self):
        pass
