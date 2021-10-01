'''PROGRAM DESCRIPITON:
	Create API REST server using python flask which:-
	1) displays the entire content of the data which has been deleted
	2) In update function, display which data has been updated to what(data before updation and after updation).
'''

# PROGRAMMED BY: PULI SNEHITH REDDY
# MAIL ID : snehithreddyp@gmail.com

# DATE    : 24-09-2021

# VERSION : 3.7.9

# CAVEATS : None

# LICENSE : None



from flask import Flask
from flask import render_template
from flask import jsonify,request
from flask import redirect
from flask import url_for
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']="mysql+pymysql://root:tinku@localhost:3307/snehith"
app.config['SECRET_KEY'] = 'Tinku@abc'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)

# create a table inside our database 
class APIUserModel(db.Model):
    __tablename__ = 'guvi_data_sciences'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20))
    email = db.Column(db.String(20))

class Suman(db.Model):
    __tablename__ = 'machine_learning'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20))
    email = db.Column(db.String(20))

# Presenting the data in json format in POSTMAN with 'POST' method and then sending it through API
# From the API requesting data and then storing it in DB and saving the changes.
@app.route('/write', methods = ['POST'])
def write():
    #Requesting id, name and email from POSTMAN
    id=request.get_json()["id"]
    name = request.get_json()["name"]
    email = request.get_json()["email"]
    api_user_model = APIUserModel(id=id,name = name, email = email)
    save_to_database = db.session()
    try:
	#Added to database
        save_to_database.add(api_user_model)
	#After data is added sucessfully comit is done to save the database.
        save_to_database.commit()
    except:
	#If insertion does not happens we have to go to the previous stage py performing rollback operation.
        save_to_database.rollback()
	#Used for free the memory
        save_to_database.flush()   
    #Returning the jsonify object as response to the insertion data.
    return jsonify({"message":"success"})

# fetch data from server
@app.route('/', methods=['GET'])
def fetch_all():
    data = APIUserModel.query.all()
    data_all = []
    for data in data:
        data_all.append({"id":data.id, "name":data.name, "email":data.email})
    return jsonify(data_all)


# fetch data based on ID
@app.route('/display/<int:id>', methods=['GET'])
def fetch_by_id(id):
    try:
	# Getting data based on id using filter_by()
        data = APIUserModel.query.filter_by(id=id).first()
        return jsonify({"id":data.id, "name":data.name, "email":data.email})
    except:
        return jsonify({"message":"error"})

#update data
@app.route('/update/<int:id>', methods=['PATCH'])
def update(id):
    # update = insert + fetch by id 
    a = APIUserModel.query.filter_by(id=id).first()
    # Storing the initial values of id, name and email in x,y,z before updation.
    x=a.id
    y=a.name
    z=a.email
    name = request.get_json()["name"]
    email = request.get_json()["email"]
    save_to_database = db.session
    try:
        api_user_model = APIUserModel.query.filter_by(id=id).first()
        api_user_model.name = name
        api_user_model.email = email
        save_to_database.commit()
    except:
        return jsonify({"message":"error in updating data"})
        save_to_database.rollback()
        save_to_database.flush()
    id=api_user_model.id
    #data after updation is stored in this data variable.
    data=APIUserModel.query.filter_by(id=id).first()
    #returns the list which consists of data before updation and after updation.
    return jsonify([{"id":x, "name":y, "email":z},{"update":"to"},{"id":data.id, "name":data.name, "email":data.email}])

#delete data 
@app.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    a = APIUserModel.query.filter_by(id=id).first()
    try:
        save_to_database = db.session 
	# First find the data based on id using filter_by() and the delete the data using delete().
        APIUserModel.query.filter_by(id=id).delete()
        save_to_database.commit()
	#returning the data which is been deleted for displaying.
        return jsonify([{"id":a.id, "name":a.name, "email":a.email}])
    except:
        return jsonify({"message":"error in deleting data"})


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=5000)

