from enum import unique
from . import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key = True)
    usuario = db.Column(db.String(100), unique = True, nullable = False)
    password = db.Column(db.String(100), nullable = False)

class Tarea(db.Model):
    __tablename__ = 'tareas'
    id = db.Column(db.Integer, primary_key = True)
    descripcion = db.Column(db.String(200), nullable = False)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id'))