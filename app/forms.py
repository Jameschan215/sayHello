from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, StringField
from wtforms.validators import DataRequired


class HelloForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired()])
    secret_code = StringField('天王盖地虎', validators=[DataRequired()])
    submit = SubmitField()
