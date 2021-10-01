'''PROGRAM DESCRIPITON: 
	Create a RESTFUL API Server in Python Flask. To achieve your target go through following process:-
    
    1) You have to hit the URL "https://api.thedogapi.com/v1/breeds" into a local JSON file into ur localhost.
    2) From the JSON file scrap the data of the breed of dog, country of origin,
        bred for which purpose and the image of the dog.
    3) Display the data in a tabular format into a HTML page.
    4) Send the extracted data into a MongoDB database with basic CRUD operations associated with it.
'''

# PROGRAMMED BY: PULI SNEHITH REDDY
# MAIL ID : snehithreddyp@gmail.com
# DATE    : 27-09-2021
# VERSION : 3.7.9
# CAVEATS : None
# LICENSE : None

import requests
import json 
import json
from pymongo import MongoClient

#Class which consists of methods related to JSON creation, reading and URL checking and retriveing data from URL.
class func:
    #Creation of JSON file by opening/ creating it and writing data into file by dump().
    def create_json(self,data,file_name):
        with open(file_name,"w") as f:
            return json.dump(data,f)
        
    #Reading data from JSON file using load().
    def read_json(self,f):
        with open(f) as f:
            return json.load(f)
        
    #Checking whetehr URL exists or not.
    def check_url(self, url):
        try:
            url = requests.get(url)
            #Return True if URL exists.
            return True
        except:
            #Return False if URL doesnot exists.
            return False

    def read_url(self, url):
        #Retrieving data from URL using requests.get() and then returning it by converting into json object.
        url = requests.get(url)
        return url.json()
        
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
    
    
    def insert_data(self,db_name,collection_name,data):
        if self.connection:
            self.connection[db_name][collection_name].insert_one(data)
            return "success"
        else:
            return "error"
    
    def display(self,db_name,collection_name):
        a=[]
        if self.connection:
            for i in self.connection[db_name][collection_name].find():
                a.append(i)
               
            for i in a:
                print(i)
                print("..............")    
   
#url used for retrieving data from the web
url = "https://api.thedogapi.com/v1/breeds"
s=func()
if s.check_url(url)==True:
    x=s.read_url(url)
    #entire data from url is stored in product_1 json file
    s.create_json(x,"project_1.json")
else:
    print("wrong")
data=[]
#From "product_1.json" file we are extracting required data and storing it in "project_breed.json"
x=s.read_json("project_1.json")
for i in x:
    y={}
    if "name" in i:
        y["name"]=i["name"]
    else:
        y["name"]="None"
    if "bred_for" in i:
        y["bred_for"]=i["bred_for"]
    else:
        y["bred_for"]="-"
    if "origin" in i:
        y["Country"]=i["origin"]
    else:
        y["Country"]="-"
    if "image" in i:
        y["image_url"]=i["image"]["url"]
    else:
        y["image_url"]="-"
    data.append(y)
# "product_breed.json" is created.
s.create_json(data,"project_breed.json")


obj=One()
#Data is to be stored in MongoDB in project_week1 database and in dog_breed collection
db_name="project_week1"
collection_name="dog_breed"
#Documents is taken from "project_breed.json" file
file="project_breed.json"
with open(file)as file:
    x=json.load(file)
    for i in x:
        obj.insert_data(db_name,collection_name,i)

#displaying documents from MongoDB
obj.display(db_name,collection_name)
