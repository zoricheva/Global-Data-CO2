from flask import Flask, render_template


app = Flask(__name__)

@app.route('/hello')
def hello():
    message = f"Стоимость квартиры площадью  равна  рублей"
  return render_template("index.html", message = message)
