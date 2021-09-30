'''PROGRAM DESCRIPITON: 
	You have a JSON file with you. Write a python program to insert the data present in the JSON file into your 
	MongoDB collection in form of documents ?
'''

# PROGRAMMED BY: PULI SNEHITH REDDY
# MAIL ID : snehithreddyp@gmail.com
# DATE    : 21-09-2021
# VERSION : 3.7.9
# CAVEATS : None
# LICENSE : None

import json
from pymongo import MongoClient

class One:
    connection = MongoClient("mongodb://localhost:27017")

    def mongo_connection(self):
        if self.connection:
            return True 
        else:
            return False 
    
    def mongodb_list(self):
        if self.mongo_connection() == True:
            return self.connection.list_database_names()

    def db_exists(self, db_name):
        if db_name in self.mongodb_list():
            return True
        else:
            return False 
    
    def create_new_collection(self, db_name, new_collection):
        if self.connection:
            db_name = self.connection[db_name]
            new_collection = db_name[new_collection]
            return new_collection
        else:
            return("error")
    
    # timestand for mongodb 
    def timestamp():
        import datetime as dt 
        return dt.datetime.now()
    
    def insert_data(self,db_name,collection_name,id1,product_name,product_price,product_material,product_color):
        if self.connection:
            data={"id":id1,"product_name":product_name,"product_price":product_price,"product_material":product_material,
                  "product_color":product_color}
            self.connection[db_name][collection_name].insertOne(data)
            return "success"
        else:
            return "error"
    
   

    
obj=One()

db_name="mongo_python"
collection_name="product"
print(obj.db_exists(db_name))
print(obj.create_new_collection(db_name,collection_name))
file="product.json"
with open(file)as file:
    x=json.load(file)
    for i in x:
        print(i)
        obj.insert_data(db_name,collection_name,i["id"],i["product_name"],i["product_price"],i["product_material"],i["product_color"])
print(obj.db_exists("product"))


