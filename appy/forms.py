from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField,FileField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from appy.models import User

 
class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

#checks if username is aleady occupied(taken) before current user in the registration form
def validate_username(self, username):
    user= User.query.filter_by(username=username.data).first()
    if user:
        raise ValidationError('username occupied, choose another!')

#checks if email is already occupied(taken) before the current user in registration form
def validate_email(self, email):
    user= User.query.filter_by(email=email.data).first()
    if user:
        raise ValidationError('email occupied, choose another!')



class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])                    

    submit = SubmitField('Update')

#checks if the username is has already been used(taken) before current user in login form
    def validate_username(self, username):
            if username.data != current_user.username:
                    user= User.query.filter_by(username=username.data).first()
                    if user:
                            raise ValidationError('username occupied, choose another!')

#this checks if email has already been used(taken) before the current user in login form
    def validate_email(self, email):
            if email.data != current_user.email:
                    user= User.query.filter_by(email = email.data).first()
                    if user:
                            raise ValidationError('email occupied, choose another!')

#
class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('content', validators=[DataRequired()])
    submit = SubmitField('Post')                            

