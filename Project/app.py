from flask import Flask,render_template,request, redirect, url_for, session, Response

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

@app.route("/for-developers")
def for_developers():
    return render_template("for-developers.html")

@app.route("/login", methods = ["GET", "POST"])
def login():
    return render_template("login.html")
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "admin" and password == "12345678":
            session["user"] = username
            return redirect("/")
        else:
            return render_template("login.html", error="Invalid credentials")
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/forgotpassword")
def forgotpassword():
    return render_template("forgotpassword.html")