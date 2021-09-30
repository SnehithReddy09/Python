from flask import Flask 
from flask import render_template 
from flask import redirect 
from flask import url_for 
from flask import request
import json

#Reading data from json file
def read_json(f):
    with open(f) as f:
        return json.load(f)
data=[]
data=read_json("project_breed.json")
t_data=[]
for i in data:
    t_data.append([[i["name"],i["bred_for"],i["Country"]],i["image_url"]])
headings=["Name","Bred_for","Country","Image"]

app = Flask(__name__) 
@app.route('/')
def index():
    return render_template('display.html',headings=headings,t_data=t_data)
if __name__ == '__main__':
    app.run(debug=True, port=5001)
