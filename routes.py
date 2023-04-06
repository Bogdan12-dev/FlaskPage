from flask import Flask, render_template, request, flash, redirect, url_for
from test import app
from test.user import *
from test.db_model import session
from werkzeug.security import generate_password_hash, check_password_hash
from .create_order import order_session
from .forms import LoginForm
from flask_login import login_user
from . import login_manager
from test.orders import *

@app.route("/")
@app.route("/main")
def test():
    return render_template("index.html")
@app.route("/order")
def ord():
    return render_template("order.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/contact")
def contact():
    return render_template("contact.html")
@app.route("/food")
def fooood():
    return render_template("food.html")
@login_manager.user_loader
def load_user(user_id):
    user = session.query(User).filter(User.id == user_id).first()
    return user


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        age = request.form.get("age")
        password = request.form.get("password")
        password = generate_password_hash(password)
        new_user = User(username=username, email=email, age=age, password=password)
        session.add(new_user)
        session.commit()
        print('succesfully singed up')
    return render_template("login_test.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = session.query(User).where(User.username == username).first()
        login_user(user)
        print(user)
        print(check_password_hash(user.password, password))
        if not user or not check_password_hash(user.password, password):
            flash("u might entered password wrong or u might be not signed up")
            return redirect(url_for("signup"))
        else:
            flash("logged in succesfully")
            return redirect("main")
            print("logged in")
    return render_template("login.html")

@app.route("/order", methods=["GET", "POST"])
def order():
    if request.method == "POST":
        new_order = Orders(**request.form)
        order_session.add(new_order)
        order_session.commit()
    return redirect(url_for("order"))

