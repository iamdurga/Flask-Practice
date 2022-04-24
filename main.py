from flask import Flask, make_response, request
import pandas as pd
import numpy as np

df = pd.read_csv("data/titanic.csv")
ages = np.arange(0,df.Age.max(),10)



def age_group(x):
    for a,aa in zip(ages[:-1],ages[1:]):
        if a  < x and x  < aa:
            return (a,aa)
    return (aa, None)

df["age_group"] = df.Age.apply(age_group) 

rdf = df.groupby("age_group").Survived.value_counts(normalize= True).rename("rate").reset_index()
rdf["lage"]= rdf.age_group.apply(lambda x: x[0])
rdf["rage"] = rdf.age_group.apply(lambda x: x[1])
rdf

app = Flask(__name__)

@app.route("/")
def home():
    return " Hello world! <h1> Hello </h1>"

@app.route("/<name>")
def user(name):
    return f"hello{name}!" 

@app.route("/titanic")
def titanic():
    
    return "<h1 align= 'center'> Below Table is Titanic Dataset</h1>" + df.to_html()

@app.route('/visit_counts', methods=['GET','POST'])  
def visit():
    counts=request.cookies.get('visits', "1")
    resp = make_response(f"<h1 align='center'>You visited {int(counts)} times.</h1>")
    vscount=int(counts)+1
    resp.set_cookie('visits',str(vscount), max_age=5*60*60)
    return resp

@app.route("/survival_rate")
def survival_rate():
    age = request.args.get("age")
    age = int(age) if age else None
    srate = 0
    if age :
        try :

            srate = rdf.query(f"lage< = {age} and rage > = {age} and Survived==1").rate.tolist()[0]
        except:
            srate = 0 if age < 0 else rdf.rate.tolist()[-1]

    return f"You Entered Age {age} and Survival rate is {srate}" 




if __name__== "__main__":
    app.run(debug=True)
   
