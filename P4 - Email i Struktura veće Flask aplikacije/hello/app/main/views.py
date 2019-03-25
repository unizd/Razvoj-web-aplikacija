from flask import Flask, render_template, session, redirect, url_for, flash
from . import main
from .forms import NameForm
from .. import db
from ..models import User

@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        return redirect(url_for('main.index'))
    return render_template('index.html', form=form, name=session.get('name'),known=session.get('known', False))

@main.route('/users')
def users():
    users = User.query.all()
    return render_template('users.html', users=users)

@main.route('/user/<id>')
def user(id):
    user = User.query.get_or_404(id)
    return render_template('user.html', user=user)

@main.route('/userdelete/<id>')
def userdelete(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    flash('Korisnik uspješno pobrisan.')
    return redirect(url_for('main.users'))
