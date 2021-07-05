from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    usuario = StringField('Usuario', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    ingresar = SubmitField('Ingresar')

class TaskForm(FlaskForm):
    descripcion = StringField('Descripcion', validators = [DataRequired()])
    registrar = SubmitField('Registrar')