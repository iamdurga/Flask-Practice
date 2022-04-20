from flask import Flask, make_response
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    return " Hello world! <h1> Hello </h1>"

@app.route("/<name>")
def user(name):
    return f"hello{name}!" 

@app.route("/titanic")
def titanic():
    df = pd.read_csv("data/titanic.csv")
    return "<h1 align= 'center'> Below Table is Titanic Dataset</h1>" + df.to_html()
@app.route("/cookie")
def cookie():
    res = make_response("Setting my cookie")
    res.set_cookie("visits","1", max_age=60*60*24)
    return res.get_data()

if __name__== "__main__":
    app.run(debug=True)
   
