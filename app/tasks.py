from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import current_user, login_required
from .forms import TaskForm
from .models import Tarea
from . import db

task = Blueprint('task', __name__)

@task.route('/tasks', methods = ['GET', 'POST'])
@login_required
def index():
    task_form = TaskForm()
    contexto = {
        'task_form': TaskForm(),
        'tasks': Tarea.query.filter_by(id_usuario = current_user.id),
        'usuario': current_user.usuario
    }

    if task_form.validate_on_submit():
        data_descripcion = task_form.descripcion.data
        nueva_tarea = Tarea(descripcion = data_descripcion, estado = 1, id_usuario = current_user.id)
        db.session.add(nueva_tarea)
        db.session.commit()

        flash('Tarea registrada correctamente', 'alert-success')
        return redirect(url_for('task.index'))

    return render_template('tasks.html', **contexto)

@task.route('/task/update/<task_id>', methods = ['POST'])
@login_required
def update(task_id):
    task = Tarea.query.get(task_id)
    task.estado = not task.estado
    db.session.commit()

    flash('Tarea actualizada correctamente', 'alert-success')
    return redirect(url_for('task.index'))

@task.route('/task/delete/<task_id>', methods = ['POST'])
@login_required
def delete(task_id):
    task = Tarea.query.get(task_id)
    db.session.delete(task)
    db.session.commit()

    flash('Tarea eliminada correctamente', 'alert-success')
    return redirect(url_for('task.index'))