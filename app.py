from flask import Flask, render_template, request



app = Flask(__name__)

@app.route('/', methods=["get", "post"])
def hello():

  if request.method == "POST":
    energy = requst.form.get("energy")
    print(energy)
    
  return render_template("index.html")
