from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, EmailField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo


class RegisterUserForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired(), Length(min=3, max=50)])
    last_name = StringField("Last Name", validators=[DataRequired(), Length(min=3, max=50)])
    email_id = EmailField("Email ID", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=5, max=16)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), Length(min=5, max=16), EqualTo("password")])
    submit = SubmitField("Register")

class LoginUserForm(FlaskForm):
    email_id = EmailField("Email ID", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")