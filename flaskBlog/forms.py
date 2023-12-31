from flask_wtf import FlaskForm
from flask_wtf.file import FileField , FileAllowed
from wtforms import StringField, PasswordField, SubmitField , BooleanField, FileField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskBlog.models import User
from flask_login import current_user


class RegistationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),Length(min=2,max=25)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    confirm_password = PasswordField('confirm password', validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign up')

    # function to check username does not match with already existing data.
    def validate_username(self,username):
      user = User.query.filter_by(username = username.data).first()

      if user:
        raise ValidationError("This username is already taken. please choose a different one")
    
    # function to check email does not match with already existing data.
    def validate_email(self,email):
      user = User.query.filter_by(email = email.data).first()

      if user:
        raise ValidationError("This email is already taken. please choose a different one")

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    remember = BooleanField('remember me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),Length(min=2,max=25)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Update')
    picture = FileField('Update Profile Picture' , validators=[FileAllowed(['jpg', 'png', 'jpeg'])])

    # function to check username does not match with already existing data.
    def validate_username(self,username):
      if username.data != current_user.username:
        user = User.query.filter_by(username = username.data).first()
        if user:
          raise ValidationError("This username is already taken. please choose a different one")
    
    # function to check email does not match with already existing data.
    def validate_email(self,email):
      user = User.query.filter_by(email = email.data).first()

      if email.data != current_user.email:
        if user:
          raise ValidationError("This email is already taken. please choose a different one")
