from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ['POST','GET'])
def hello():

  return render_template('index.html', result = message)


if __name__
app.run


