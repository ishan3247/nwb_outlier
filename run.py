# flask stuff
from flask import Flask
from flask import Flask, redirect, url_for, render_template, flash, session, request, abort
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

# io stuff
import os
from dateutil.tz import tzlocal
from pathlib import Path

# data stuff
import pandas as pd
import numpy as np

# nwb stuff
from pynwb import NWBFile
from pynwb import NWBHDF5IO


# nwbfilepath = Path('test_TimeSeries.nwb')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'therearenooutliers'

class CheckboxForm(FlaskForm):
    findOutliers = BooleanField('find outliers')
    submit = SubmitField('submit')


@app.route("/", methods=['GET','POST'])
def home():
    form = CheckboxForm()

    if form.validate_on_submit():

        io = NWBHDF5IO('nwb_files/test_TimeSeries.nwb', 'r')
        nwbfile_in = io.read()


        test_timeseries_in = nwbfile_in.acquisition['test_timeseries']

        print("the time series data is", test_timeseries_in)

    return render_template("index.html", form=form)



if __name__ == "__main__":
    app.run(debug  = True)