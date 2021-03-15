from flask import Flask, render_template,current_app as app
app = Flask(__name__)
@app.route('/finalproject')
def finalP():
    return "final project thing"

if __name__== '__main__':
    app.run(debug=True, host = '0.0.0.0')
