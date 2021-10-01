'''PROGRAM DESCRIPITON: 
	Create a RESTFUL API Server in Python Flask. To achieve your target go through following process:-
    
    1) You have to hit the URL "https://api.thedogapi.com/v1/breeds" into a local JSON file into ur localhost.
    2) From the JSON file scrap the data of the breed of dog, country of origin,
        bred for which purpose and the image of the dog.
    3) Display the data in a tabular format into a HTML page.
    4) Send the extracted data into a MongoDB database with basic CRUD operations associated with it.
    
    
    Display the data in a tabular format into a HTML page is done using FLASK.
'''

# PROGRAMMED BY: PULI SNEHITH REDDY
# MAIL ID : snehithreddyp@gmail.com
# DATE    : 27-09-2021
# VERSION : 3.7.9
# CAVEATS : None
# LICENSE : None

from flask import Flask 
from flask import render_template 
from flask import redirect 
from flask import url_for 
from flask import request
import json

#Reading data from json file by opening the file and writing the data using dump().
def read_json(f):
    with open(f) as f:
        return json.load(f)
data=[]
data=read_json("project_breed.json")
t_data=[]
for i in data:
    #Storing the data in json file in a format suitable for displaying in HTML.
    t_data.append([[i["name"],i["bred_for"],i["Country"]],i["image_url"]])
   
#Headings which are to be present in the Table displayed in HTML.
headings=["Name","Bred_for","Country","Image"]

app = Flask(__name__) 
@app.route('/')
def index():
    #Rendering the HTML file and also the headings of table to be displayed and data in table is also sent.
    return render_template('display.html',headings=headings,t_data=t_data)
if __name__ == '__main__':
    app.run(debug=True, port=5001)
