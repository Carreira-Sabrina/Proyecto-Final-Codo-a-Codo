from flask import render_template
from flask import redirect
from flask import jsonify

from app import app


from modelos.entidades import Cliente

@app.route("/api/obtener_clientes")
def api_obtener_clientes():
    #Devuelve una lista de obtetos de tipo Cliente
    clientes = Cliente.obtener_todos_de_tabla()
    
    #Cuidadito ! clientes recibe una lista de objetos de tipo Cliente, para pasárselo a jsonify() se convierte cada objeto en diccionario en la linea sgte
    lista_diccionarios_clientes = [vars(cliente) for cliente in clientes]
    
    #Devuelvo un json que será consumido... en alguna parte
    return jsonify(lista_diccionarios_clientes)

