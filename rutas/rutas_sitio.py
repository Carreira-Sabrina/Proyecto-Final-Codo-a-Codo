from flask import render_template
from app import app


lista = ["Pedro","Pedro","Pedro","Pe"]


@app.route("/inicio_gestion_reservas")
def inicio_gestion_reservas():
    return render_template("inicio_gestion_reservas.html",datos=lista)


@app.route("/listar_clientes")
def listar_clientes():
    return render_template("listar_clientes.html")


@app.route("/listar_reservas")
def listar_clientes():
    return render_template("listar_reservas.html")


@app.route("/nueva_reserva")
def listar_clientes():
    return render_template("nueva_reserva.html")
