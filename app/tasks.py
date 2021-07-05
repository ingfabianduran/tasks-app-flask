from flask import Blueprint, render_template
from .forms import TaskForm
from . import db

task = Blueprint('task', __name__)

@task.route('/tasks')
def index():
    contexto = {
        'task_form': TaskForm()
    }

    return render_template('tasks.html', **contexto)