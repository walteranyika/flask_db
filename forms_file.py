from flask_wtf import FlaskForm
from wtforms import StringField,DateField
from  wtforms.validators import Email,DataRequired,Length

class ReForm(FlaskForm):
    names = StringField("Names",validators=[DataRequired(message="Invalid Names"), Length(min=6)])

    email = StringField("Email",validators=[DataRequired(message="Invalid email"), Email()])

    dob = StringField("Date Of Birth",validators=[DataRequired(message="Invalid DOB")])



