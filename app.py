from flask import Flask, render_template, request
from process import get_prediction

app = Flask(__name__)

@app.route('/', methods = ['POST','GET'])
def hello():
  message = ''
  if request.method == 'POST':
    energy = request.form.get("energy")
    energy = float(energy)
    co2 = get_prediction(energy)
    print(co2)
    message = f"Предсказание:{y_pred}"

  
  return render_template('index.html', result = message)


if __name__
app.run


