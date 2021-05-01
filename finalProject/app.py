from flask import Flask, render_template,current_app, request
from sense_hat import SenseHat
import sqlite3
sense = SenseHat()
sense.low_light= True

app = Flask(__name__)
@app.route('/finalproject')
def finalP():
    return "final project thing"

@app.route('/')
def default():
    return render_template("final_project.html")

@app.route('/form',methods = ['POST', 'GET'])
def secretMsg():
   if request.method == 'POST':
      user = request.form['msg']
      sense.show_message(user)
      return "thx"
   return "oops"

   message = request.form['message']
   name = request.form['name']

   conn = sqlite3.connnect('./static/senseDisplay.db')
   curs= conn.cursor()
   curs.execute("INSERT INTO MESSAGES (name, message) VALUES ((?),(?))",(name,message))
   conn.commit()
   conn.close
   return render_template('sent.html', message=message, name=name)

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
    
