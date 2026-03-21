from flask import Flask, render_template
from flask import request, render_template, redirect, url_for

app = Flask(__name__)
app.secret_key = "fendergluid" # Here u go :3

@app.route('/')
def base():
  return render_template("base.html")
