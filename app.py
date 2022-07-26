from flask import Flask, render_template

# flask -> biblioteca Flask -> Classe

app = Flask("hello")

@app.route("/")

def hello():
    return "Hello World!"

@app.route("/meucontato")

def meucontato():
    return render_template("index.html") 