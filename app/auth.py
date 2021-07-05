from flask import Blueprint, render_template, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from .forms import LoginForm
from .models import Usuario
from . import db


auth = Blueprint('auth', __name__)

@auth.route('/', methods = ['GET', 'POST'])
def index():
    login_form = LoginForm()
    contexto = {
        'login_form': login_form
    }

    if login_form.validate_on_submit():
        data_usuario = login_form.usuario.data
        data_password = login_form.password.data
        usuario = Usuario.query.filter_by(usuario = data_usuario).first()

        if not usuario:
            return redirect(url_for('auth.index'))
        else: 
            if check_password_hash(usuario.password, data_password):
                return redirect(url_for('task.index'))
            else: 
                return redirect(url_for('auth.index'))

    return render_template('index.html', **contexto)

@auth.route('/signup')
def signup(): 
    data_usuario = {
        'usuario': 'duranfabian@unbosque.edu.co',
        'password': 'Lenovo9325*'
    }

    nuevo_usuario = Usuario(usuario = data_usuario['usuario'], password = generate_password_hash(data_usuario['password'], method = 'sha256'))
    db.session.add(nuevo_usuario)
    db.session.commit()
    return 'Usuario Registrado'