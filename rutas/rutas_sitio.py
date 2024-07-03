from flask import render_template
from flask import url_for
from flask import request
from flask import redirect
from app import app
from modelos.entidades import Excursion


@app.route("/")
def index():
    #Se obtiene una lista de instancias de excursion, con los datos leidos de la base de datos
    excursiones = Excursion.obtener_todos_de_tabla()
    
    return render_template("index.html",info = excursiones) #Info se pasa a index.html para ser mostrado dinámicamente con Jinja


@app.route("/acerca-de-nosotros")
def about_us():
    return render_template("about-us.html") 


@app.route("/crear_excursion",methods = ["GET","POST"])
def crear_excursion():
    if request.method == "POST":
        # Se toman los datos del formulario:
        _titulo = request.form["titulo-excursion"]
        _descripcion = request.form["descripcion-excursion"]
        _destino = request.form["destino-excursion"]
        _precio = int(request.form["precio-excursion"])
        _url_imagen = request.form["url-imagen-excursion"]
        
        #Acordarse que el metodo create del CRUD recibe los datos como una tupla !!!
        datos_nueva_excursion = (_titulo,_descripcion,_destino,_precio,_url_imagen)
        
        #Se crea una instancia 
        nueva_excursion = Excursion(datos_nueva_excursion)
        #La instancia se ocupa de guardarse en la tabla
        nueva_excursion.insertar_en_tabla()
        
        print("Se ha creado un nuevo registro en la base de datos")
        
        #DEBERIA REDIRECCIONAR AL INDEX PARA VER EL LISTADO ACTUALIZADO !
        
        return redirect(url_for("index"))
    
    else:
        #En GET solo renderizo el form...
        return render_template("crear_excursion.html") 


@app.route("/modificar_excursion/<int:id>",methods = ["GET","POST"])
def modificar_excursion(id):
    
    if request.method == "POST":
        # Se toman los datos del formulario:
        _titulo = request.form["titulo-excursion"]
        _descripcion = request.form["descripcion-excursion"]
        _destino = request.form["destino-excursion"]
        _precio = int(request.form["precio-excursion"])
        _url_imagen = request.form["url-imagen-excursion"]
        
        print(f"El titulo será {_titulo}, en {_destino}, la descripcion es {_descripcion} y la url es {_url_imagen}")
        
        #Acordarse que el metodo update del CRUD recibe los datos como una tupla !!!
        datos_excursion = (id,_titulo,_descripcion,_destino,_precio,_url_imagen)
        
        
        Excursion.actualizar_registro_tabla(datos_excursion)
        
        print("Se ha actualizado el registro exitosamente !")
        
        #DEBERIA REDIRECCIONAR AL INDEX PARA VER EL LISTADO ACTUALIZADO !
        return redirect(url_for("index"))
    
    else:
        #Necesito los datos del objeto para pasarselos al formulario como "relleno"
        #Esta función devuelve un objeto
        excursion_a_modificar = Excursion.obtener_objeto_de_tabla(id)
        
        #En el get es donde debo renderizar el form con el contenido traido....
        return render_template("modificar_excursion.html", objeto_a_modificar = excursion_a_modificar) 


@app.route("/eliminar_excursion/<int:id>",methods = ["GET"])
def eliminar_excursion(id):
    if request.method == "GET":
        Excursion.eliminar_de_tabla(id)
        return redirect(url_for("index"))