from flask import Flask, make_response, request
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

@app.route('/visit_counts', methods=['GET','POST'])  
def visit():
    counts=request.cookies.get('visits', "1")
    resp = make_response(f"<h1 align='center'>You visited {int(counts)} times.</h1>")
    vscount=int(counts)+1
    resp.set_cookie('visits',str(vscount), max_age=5*60*60)
    return resp

if __name__== "__main__":
    app.run(debug=True)
   
