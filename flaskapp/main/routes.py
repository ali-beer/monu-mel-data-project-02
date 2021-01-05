from flaskapp import db
from flask import render_template, url_for, flash, redirect, Blueprint
from datetime import datetime

main = Blueprint('main', __name__)


@main.route("/", methods=['GET', 'POST'])
@main.route("/home", methods=['GET', 'POST'])
@main.route("/index", methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@main.route("/analysis", methods=['GET', 'POST'])
def analysis():
    return render_template('dashboard.html')

@main.route("/about", methods=['GET', 'POST'])
def about():
    return render_template('about.html')

