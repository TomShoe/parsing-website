from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
import os, sys, subprocess, importlib

directory = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SECRET_KEY'] = 'tomisgoated'

class BattlefyForm(FlaskForm):
    matchhistory = StringField('Match History Link')

@app.route("/test")
def home():
    return render_template("base.html")

@app.route("/", methods=["GET", "POST"])
@app.route("/lol", methods=["GET", "POST"])
@app.route("/scraper", methods=["GET", "POST"])
def scraper():
    form = BattlefyForm()

    if form.validate_on_submit():
        url = form.matchhistory.data
        #result = url
        result = subprocess.check_output([sys.executable, 
            "{}/stuff.py".format(directory), url]).decode('iso-8859-1')
        return render_template("scraper.html", form=form, result=result)
    return render_template("scraper.html", form=form)

@app.route('/base', methods=["GET"])
def base():
    return render_template("base.html")

@app.template_filter('nl2br')
def nl2br(s):
    return s.replace("\n", "<br />")

if __name__ == "__main__":
    app.run(debug = True)