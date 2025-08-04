from flask import Flask, render_template, request
from process import get_prediction


app = Flask(__name__)

@app.route('/', methods=["get", "post"])
def hello():
  message = ""
  if request.method == "POST":
    energy = request.form.get("energy")
    energy = float(energy)
    co2 = get_prediction(energy)
    
    message = f"При потребляемой энергии в размере {energy} количество выбросов будет равно {co2} "
    
  
  
  return render_template("index.html", message = message)
