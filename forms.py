from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField , BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),Length(min=2,max=25)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    confirm_password = PasswordField('confirm password', validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    remember = BooleanField('remember me')
    submit = SubmitField('Login')
