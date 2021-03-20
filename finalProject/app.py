from flask import Flask, render_template,current_app, request
from sense_hat import SenseHat
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

if __name__== '__main__':
    app.run(debug=True, host = '0.0.0.0')
    
