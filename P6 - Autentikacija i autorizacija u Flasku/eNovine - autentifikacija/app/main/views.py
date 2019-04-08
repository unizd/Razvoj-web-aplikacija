from flask import render_template, redirect, url_for
from ..decorators import admin_required, permission_required
from flask_login import login_required, current_user
from ..models import User, News, Permission
from .forms import VijestForm
from . import main
from .. import db


@main.route('/')
def index():
	return render_template('index.html')


@main.route('/korisnici')
@login_required
@admin_required
def korisnici():
	korisnici = User.query.all()
	return render_template('korisnici.html', korisnici=korisnici)


@main.route('/dodaj-vijest', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.ADD)
def dodaj_vijest():
    form = VijestForm()
    if current_user.can(Permission.ADD) and form.validate_on_submit():
        vijest = News(title=form.title.data, content=form.content.data,
                      author=current_user._get_current_object())
        db.session.add(vijest)
        db.session.commit()
        return redirect(url_for('.index'))
		
    return render_template('vijest.html', form=form)