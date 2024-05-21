from flask import Blueprint, jsonify, abort, request, render_template, redirect
from controls.RegistroDaoControl import RegistroDaoControl
from datetime import datetime

router = Blueprint('router', __name__)

@router.route('/')
def home():
    return render_template("template.html")

@router.route('/registro')
def registros():
    rdc = RegistroDaoControl()
    return render_template("servp/registro.html", lista=rdc.to_dic())

@router.route('/ventanillas')
def ventanillas():
    return render_template("servp/ventanilla.html")

@router.route('/ventanillas/guardar', methods=['POST'])
def guardar_registro():
    rdc = RegistroDaoControl()
    data = request.form

    if not "nombre" in data.keys() or not "numVentanilla" in data.keys():
        abort(400)
    
    # Validar y guardar los datos
    rdc._ServidorPublico._numVentanilla = data['numVentanilla']
    rdc._ServidorPublico._nombre = data['nombre']
    rdc._ServidorPublico._fecha = data['fecha']
    rdc._ServidorPublico._calificacion = data['calificacion']
    rdc.save
    return redirect("/registro", code=302)

