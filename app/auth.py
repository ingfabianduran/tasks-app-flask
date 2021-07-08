from flask import Blueprint, render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
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

        if usuario is None:
            flash('Usuario no encontrado', 'alert-danger')
            return redirect(url_for('auth.index'))
        else: 
            if check_password_hash(usuario.password, data_password):
                login_user(usuario)
                return redirect(url_for('task.index'))
            else: 
                flash('Contraseña incorrecta', 'alert-danger')
                return redirect(url_for('auth.index'))

    return render_template('index.html', **contexto)

@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    login_form = LoginForm()
    contexto = {
        'login_form': login_form
    }

    if login_form.validate_on_submit():
        data_usuario = login_form.usuario.data
        data_password = login_form.password.data
        usuario = Usuario.query.filter_by(usuario = data_usuario).first()

        if usuario is None:
            nuevo_usuario = Usuario(usuario = data_usuario, password = generate_password_hash(data_password, method = 'sha256'))
            db.session.add(nuevo_usuario)
            db.session.commit()
            
            flash('Usuario creado correctamente', 'alert-success')
            return redirect(url_for('auth.index'))
        else: 
            flash('El usuario ya existe', 'alert-danger')
            return redirect(url_for('auth.index'))
    
    return render_template('signup.html', **contexto)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Gracias por usar el sistema', 'alert-success')
    return redirect(url_for('auth.index'))