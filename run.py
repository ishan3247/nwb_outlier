# flask stuff
from flask import Flask
from flask import Flask, redirect, url_for, render_template, flash, session, request, abort
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from werkzeug.utils import secure_filename

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

# general initialization
app = Flask(__name__)
app.config['SECRET_KEY'] = 'therearenooutliers'
UPLOAD_FOLDER = 'upload_folder'
ALLOWED_EXTENSIONS = {'nwb'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
filename=None

# check if file is of a valid extension
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


class CheckboxForm(FlaskForm):
    findOutliers = BooleanField('find outliers')
    submit = SubmitField('submit')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    file = None

    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))


    if 'filename' in locals():
        if filename!= '':
            
            io = NWBHDF5IO('nwb_files/'+filename, 'r')
            nwbfile_in = io.read()
            file=nwbfile_in
            print(nwbfile_in)

    return render_template('upload_file.html', file=file)


if __name__ == "__main__":
    app.run(debug  = True)