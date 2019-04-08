from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class VijestForm(FlaskForm):
    title = StringField('Naslov', validators=[DataRequired()])
    content = StringField('Sadržaj', validators=[DataRequired()])
    submit = SubmitField('Unesi vijest')
