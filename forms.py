from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class UniverseSize(FlaskForm):
    width = IntegerField('width', validators=[NumberRange(min=5, max=25)])
    height = IntegerField('height', validators=[NumberRange(min=5, max=20)])
    submit = SubmitField('submit')
