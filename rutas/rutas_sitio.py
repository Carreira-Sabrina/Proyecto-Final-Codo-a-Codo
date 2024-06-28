from flask import render_template
from flask import url_for
from app import app
from modelos.entidades import Excursion

#MACHETE PARA EL INDEX
#  <a class="post-bnt-acciones editar" href="{{url_for('editar_post', id=post[0])}}">Editar post</a>



@app.route("/")
def index():
    #Se obtienen las excursiones
    excursiones = Excursion.obtener_todos_de_tabla()
    
    return render_template("index.html",info = excursiones) # Acá habría que pasar los datos para ya mostar las excursiones !

@app.route("/acerca-de-nosotros")
def about_us():
    return render_template("about-us.html") 



