from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("hello.html")

db=[{'GOOGLE' : 5}, {"MSFT" : 8}]



@app.route('/form')
def form():
    return render_template("form.html")