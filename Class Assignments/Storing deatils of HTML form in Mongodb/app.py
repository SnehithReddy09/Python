'''PROGRAM DESCRIPITON: 
HMTL form for registration is created and after filling the data, the student details like name,email, course are stored in the MongoDB "Registration" database.
'''

# PROGRAMMED BY: PULI SNEHITH REDDY
# MAIL ID : snehithreddyp@gmail.com

# DATE    : 23-09-2021

# VERSION : 3.7.9

# CAVEATS : None

# LICENSE : None




from flask import Flask 
from flask import render_template 
from flask import redirect 
from flask import url_for 
from flask import request
import json
from pymongo import MongoClient

connection = MongoClient("mongodb://localhost:27017")

def mongo_connection():
    if connection:
        return True
    else:
        return False

def mongodb_list():
   if mongo_connection() == True:
        return connection.list_database_names()

def db_exists( db_name):
    if db_name in mongodb_list():
        return True
    else:
        return False

def create_new_collection(db_name, new_collection):
    if connection:
        db_name = connection[db_name]
        new_collection = db_name[new_collection]
        return new_collection
    else:
        return("error")

# timestand for mongodb
def timestamp():
    import datetime as dt
    return dt.datetime.now()

def insert_data(db_name,collection_name,data):
    if connection:
        connection[db_name][collection_name].insert_one(data)
        return "success"
    else:
        return "error"

def display(db_name,collection_name):
    a=[]
    if connection:
        for i in connection[db_name][collection_name].find():
            a.append(i)

        for i in a:
            print(i)
            print("-----------------------------------------------")



app = Flask(__name__) 

def func(name,email,course):
    data={}
    data["name"]=name
    data["email"]=email
    data["course"]=course
    insert_data("Registration","Data",data)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submi',methods=['POST'])
def result():
    name=request.form['name']
    email=request.form['email']
    course=request.form['course']
    func(name,email,course)
    return render_template("submit.html")

@app.route('/user')
def user():
    return render_template('user.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)


