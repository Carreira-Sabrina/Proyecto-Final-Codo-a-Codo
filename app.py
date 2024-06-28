from flask import Flask
from flask_cors import CORS
from flask import render_template
from flask import url_for


app = Flask(__name__,template_folder='templates')

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


#Se importan las vistas, tiene que ser DESPUÉS de crear app como instancia de Flask !
from rutas.rutas_sitio import  *
from rutas.rutas_api import *




if __name__ == "__main__":
    app.run(debug=True)