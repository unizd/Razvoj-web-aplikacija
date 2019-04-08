from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    password = PasswordField('Lozinka', validators=[DataRequired()])
    remember_me = BooleanField('Želim ostati prijavljen')
    submit = SubmitField('Prijava')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    username = StringField('Korisničko ime', validators=[
        DataRequired(), Length(1, 64),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
               'Korisničko ime smije sadržavati samo slova, brojeve, točke ili '
               'donje crte')])
    password = PasswordField('Lozinka', validators=[
        DataRequired(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Ponovi lozinku', validators=[DataRequired()])
    submit = SubmitField('Registriraj se')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email već registriran.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Korisničko ime je već zauzeto.')


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Stara lozinka', validators=[DataRequired()])
    password = PasswordField('Nova lozinka', validators=[
        DataRequired(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Potvrdi novu lozinku',
                              validators=[DataRequired()])
    submit = SubmitField('Promijeni lozinku')


class PasswordResetRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    submit = SubmitField('Resetiraj lozinku')


class PasswordResetForm(FlaskForm):
    password = PasswordField('Nova lozinka', validators=[
        DataRequired(), EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('Potvrdi novu lozinku', validators=[DataRequired()])
    submit = SubmitField('Resetiraj lozinku')


class ChangeEmailForm(FlaskForm):
    email = StringField('Novi email', validators=[DataRequired(), Length(1, 64),
                                                 Email()])
    password = PasswordField('Lozinka', validators=[DataRequired()])
    submit = SubmitField('Promijeni email')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email već postoji.')
