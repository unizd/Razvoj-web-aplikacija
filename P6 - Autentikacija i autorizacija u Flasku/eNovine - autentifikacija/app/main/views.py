from flask import render_template
from . import main
from .. import db
from ..decorators import admin_required
from flask_login import login_required
from ..models import User

@main.route('/')
def index():
	return render_template('index.html')


@main.route('/korisnici')
@login_required
@admin_required
def korisnici():
	korisnici = User.query.all()
	return render_template('korisnici.html', korisnici=korisnici)