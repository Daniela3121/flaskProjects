from flask import Flask, render_template,current_app, request
from sense_hat import SenseHat
import sqlite3
sense = SenseHat()
sense.low_light= True

app = Flask(__name__)
@app.route('/finalproject')
def finalP():
    return "reminders"

@app.route('/')
def default():
    return render_template("reminders.html")

@app.route('/form',methods = ['POST', 'GET'])
def secretMsg():
   if request.method == 'POST':
      user = request.form['msg']
      sense.show_message(user)
      return "thx"
   return "oops"
@app.route('/all')
def all():
       conn = sqlite3.connect('./static/data/senseDisplay.db')
       curs = conn.cursor()
       messages = []
       rows = curs.execute("SELECT * from messages")
       for row in rows:
           message = {'name': row[0],'message':row[1]}
           messages.append(message)
           conn.close()
           return render_template('all.html', messages=messages)


   

if __name__== '__main__':
    app.run(debug=True, host = '0.0.0.0')