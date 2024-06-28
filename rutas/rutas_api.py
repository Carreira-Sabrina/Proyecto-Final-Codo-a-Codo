from flask import render_template
from flask import redirect
from flask import jsonify

from app import app


from modelos.entidades import Cliente
from modelos.entidades import Excursion

@app.route("/api/obtener_clientes")
def api_obtener_clientes():
    #Devuelve una lista de obtetos de tipo Cliente
    clientes = Cliente.obtener_todos_de_tabla()
    
    #Cuidadito ! clientes recibe una lista de objetos de tipo Cliente, para pasárselo a jsonify() se convierte cada objeto en diccionario en la linea sgte
    # vars() devuelve un diccionario con los atributos de la instancia
    lista_diccionarios_clientes = [vars(cliente) for cliente in clientes]
    
    #Devuelvo un json que será consumido... en alguna parte
    return jsonify(lista_diccionarios_clientes)


@app.route("/api/obtener_cliente_por_id/<int:id>")
#Nota mental: no olvidar poner en mismo parametro en la url y entre los paréntesis de la funcion ...
def api_obtener_cliente_por_id(id):
    #Devuelve un objeto de tipo cliente
    cliente = Cliente.obtener_objeto_de_tabla(id)
    #Cuidadito ! clientes recibe una lista de objetos de tipo Cliente, para pasárselo a jsonify() se convierte cada objeto en diccionario en la linea sgte
    # vars() devuelve un diccionario con los atributos de la instancia
    diccionario_cliente = vars(cliente)
    
    #Devuelvo un json que será consumido... en alguna parte
    return jsonify(diccionario_cliente)


#Trae los datos de las excursiones de la BD para generar el contenido de "excursiones.html" dinámicamente
@app.route("/api/obtener_excursiones")
def api_obtener_excursiones():
    excursiones = Excursion.obtener_todos_de_tabla()
    lista_diccionarios_excursiones = [vars(excursion) for excursion in excursiones]
    
    return jsonify(lista_diccionarios_excursiones)