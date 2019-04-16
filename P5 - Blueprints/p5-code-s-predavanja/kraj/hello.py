import os
# from flask import Flask, render_template, session, redirect, url_for, flash
# from flask_bootstrap import Bootstrap
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField
# from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app import create_app, db
app = create_app(os.getenv('FLASK_CONFIG') or 'default')

# basedir = os.path.abspath(os.path.dirname(__file__))
# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'blablastring'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# bootstrap = Bootstrap(app)
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)








