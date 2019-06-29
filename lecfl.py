import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    names =["bob",'alice','sam','rohit']
    return render_template("index.html", names=names)
@app.route("/more")
def more():
    return render_template("more.html")
@app.route("/form", methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        return "submit form"
        
    else:
        
        name = request.form.get("name")
        return render_template("form.html",name=name)
    
    
        