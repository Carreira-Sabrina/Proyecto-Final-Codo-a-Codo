from flask import Flask
from flask import render_template

app = Flask(__name__,template_folder='templates')



#Pruebas locas con Jinja
@app.route("/base_template")
def devolver_plantilla_base():
    return render_template("base_template.html")


@app.route("/")
def devolver_index():
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)