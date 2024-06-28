from flask import render_template
from app import app




@app.route("/inicio_gestion_reservas")
def inicio_gestion_reservas():
    return render_template("inicio_gestion_reservas.html")


@app.route("/listar_clientes")
def listar_clientes():
    return render_template("listar_clientes.html")


@app.route("/listar_reservas")
def listar_reservas():
    return render_template("listar_reservas.html")


@app.route("/crear_reserva")
def crear_reserva():
    return render_template("crear_reserva.html")
