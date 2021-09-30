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
    #Establishment of connection with MongoDB.
    connection = MongoClient("mongodb://localhost:27017")

    def mongo_connection(self):
	#If connection is made True is returned else False.
        if self.connection:
            return True 
        else:
            return False 
    
    def mongodb_list(self):
	#checking whether connection is done and if True return list of Database Names.
        if self.mongo_connection() == True:
            return self.connection.list_database_names()

    def db_exists(self, db_name):
	#Return True if particular database name exists.
        if db_name in self.mongodb_list():
            return True
        else:
            return False 
    
    def create_new_collection(self, db_name, new_collection):
	#If connection is done succesfully new_collection is created and returned.
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
    
    
    def insert_data(self,db_name,collection_name,data):
        if self.connection:
	    #Inserting the data into database where database name="db_name" and collection is "collection_name"
            self.connection[db_name][collection_name].insert_one(data)
            return "success"
        else:
            return "error"
    
    def display(self,db_name,collection_name):
        a=[]
        if self.connection:
	    #Iterating the documents in collection and appending into list.
            for i in self.connection[db_name][collection_name].find():
                a.append(i)
		
            #Iterating list and displaying contents in it.
            for i in a:
                print(i)
                print("..............")

    
obj=One()

db_name="mongo_python"
collection_name="product"
file="product.json"
#opening the json file and inserting data into MongoDB by iterating the file.
with open(file)as file:
    x=json.load(file)
    for i in x:
        print(i)
        obj.insert_data(db_name,collection_name,i)
  
#Displaying the contents which are stored in the database.
obj.display(db_name,collection_name)



