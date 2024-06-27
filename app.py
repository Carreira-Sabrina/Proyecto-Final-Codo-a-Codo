from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__,template_folder='templates')


#Se importan las vistas, tiene que ser DESPUÉS de crear app como instancia de Flask !
from rutas.rutas_sitio import  *






if __name__ == "__main__":
    app.run(debug=True)