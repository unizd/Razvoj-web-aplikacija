import os
# from flask import Flask, render_template, session, redirect, url_for, flash
# from flask_bootstrap import Bootstrap
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField
# from wtforms.validators import DataRequired
# from flask_sqlalchemy import SQLAlchemy
from app import create_app, db
# from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))
# app = Flask(__name__)
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
# app.config['SECRET_KEY'] = 'blablastring'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# bootstrap = Bootstrap(app)
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

# class Role(db.Model):
#     __tablename__ = 'roles'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), unique=True)
#     users = db.relationship('User', backref='role', lazy='dynamic')

#     def __repr__(self):
#         return '<Role %r>' % self.name

# class User(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(64), unique=True, index=True)
#     # email = db.Column(db.String(64))
#     role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

#     def __repr__(self):
#         return '<User %r>' % self.username

# class NameForm(FlaskForm):
#     name = StringField('Kako se zoveš?', validators=[DataRequired()])
#     submit = SubmitField('Pošalji')

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     form = NameForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(username=form.name.data).first()
#         if user is None:
#             user = User(username=form.name.data)
#             db.session.add(user)
#             db.session.commit()
#             session['known'] = False
#         else:
#             session['known'] = True
#         session['name'] = form.name.data
#         return redirect(url_for('index'))
#     return render_template('index.html', form=form, name=session.get('name'),known=session.get('known', False))

# @app.route('/users')
# def users():
#     users = User.query.all()
#     return render_template('users.html', users=users)

# @app.route('/user/<id>')
# def user(id):
#     user = User.query.get_or_404(id)
#     return render_template('user.html', user=user)

# @app.route('/userdelete/<id>')
# def userdelete(id):
#     user = User.query.get_or_404(id)
#     db.session.delete(user)
#     db.session.commit()
#     flash('Korisnik uspješno pobrisan.')
#     return redirect(url_for('users'))


# @app.errorhandler(404)
# def page_not_found(e):
# 	return render_template('404.html'), 404
