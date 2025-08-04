from flask import Flask, render_template, request
from process import get_prediction


app = Flask(__name__)

@app.route('/', methods=["get", "post"])
def hello():
  message = ""
  if request.method == "POST":
    energy = requst.form.get("energy")
    energy = float(energy)
    co = get_prediction(energy)
    message = f"Стоимость квартиры площадью {energy} равна {co} рублей"
    print(co)
  
  
  return render_template("index.html")
