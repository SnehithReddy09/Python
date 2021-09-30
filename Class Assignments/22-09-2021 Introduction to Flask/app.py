'''
PROGRAM DESCRIPITON:
	Create a FLASK Framework integrating it with HTML, CSS and JAVA SCRIPT.
'''

# PROGRAMMED BY: PULI SNEHITH REDDY
# MAIL ID : snehithreddyp@gmail.com
# DATE    : 22-09-2021
# VERSION : 3.7.9
# CAVEATS : None
# LICENSE : None


from flask import Flask 
from flask import render_template 
from flask import redirect 
from flask import url_for 
from flask import request
import json

app = Flask(__name__) 

@app.route('/')
def index():
    #Return the html file in the browser
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=5001)


