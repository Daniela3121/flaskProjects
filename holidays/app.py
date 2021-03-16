import json
from flask import Flask, render_template,current_app as app
import requests
import json
app = Flask(__name__, static_folder="static")

@app.route('/')
def index():
    response = requests.get('https://date.nager.at/api/v2/publicholidays/2017/AT')
    return render_template('home.html', data=data)

if __name__== '__main__':
    app.run(debug=True, host = '0.0.0.0')
