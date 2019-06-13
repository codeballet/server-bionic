from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class RegisterForm(FlaskForm):
    user_name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Register')