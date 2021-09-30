import requests
import json 
import json
from pymongo import MongoClient

class func:
    def create_json(self,data,file_name):
        with open(file_name,"w") as f:
            return json.dump(data,f)
    
    def read_json(self,f):
        with open(f) as f:
            return json.load(f)

    def check_url(self, url):
        try:
            url = requests.get(url)
            return True
        except:
            return False

    def read_url(self, url):
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
