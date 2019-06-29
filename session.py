from flask import Flask, render_template, request, Session

from flask_Session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] =False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

notes = []

@app.route("/",methods=["GET","POST"])
def note():
    session["notes"]=[]
    note = request.form.get("name")
    session["notes"].append(note)
    
    return render_template('session.html',notes=session["notes"])
