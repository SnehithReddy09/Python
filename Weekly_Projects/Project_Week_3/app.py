from flask import Flask 
from flask import render_template 
from flask import redirect 
from flask import url_for 
from flask import request

app = Flask(__name__) 


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/Details of the Report')
def user():
    return render_template('details.html')

@app.route('/report')
def report():
    return render_template('report.html')

@app.route('/analysis')
def analysis():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
