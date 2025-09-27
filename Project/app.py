from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/products")
def products():
    return render_template("products.html")

@app.route("/solutions")
def solutions():
    return render_template("solutions.html")

@app.route("/resources")
def resources():
    return render_template("resources.html")

@app.route("/pricing")
def pricing():
    return render_template("pricing.html")

@app.route("/for_developers")
def for_developers():
    return render_template("for_developers.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")