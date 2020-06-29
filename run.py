from flask import Flask
from flask import Flask, redirect, url_for, render_template, flash, session, request, abort
import pandas as pd
import numpy as np



app = Flask(__name__)



@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug  = True)