from flask import render_template
from flask import redirect
from flask import jsonify

from app import app


from modelos.entidades import Excursion


#Trae los datos de las excursiones de la BD para generar el contenido de "excursiones.html" dinámicamente
#Nota mental: no olvidar poner en mismo parametro en la url y entre los paréntesis de la funcion ...
@app.route("/api/obtener_excursiones")
def api_obtener_excursiones():
    excursiones = Excursion.obtener_todos_de_tabla()
    lista_diccionarios_excursiones = [vars(excursion) for excursion in excursiones]
    
    return jsonify(lista_diccionarios_excursiones)