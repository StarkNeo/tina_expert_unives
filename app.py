from dotenv import load_dotenv
import os
from flask import Flask, render_template, request, session
from clips import Environment
from rdf_manager import generar_rdf

load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY")

def obtener_estado(nivel_anterior, nivel_actual):
    env = Environment()
    env.load("reglas.clp")
    env.reset()
    env.assert_string(
        f"""
            (tina
                (nivel-anterior {nivel_anterior})
                (nivel-actual {nivel_actual})
            )))"""
    )
    env.run()
    
    estado = ""
    recomendacion = ""

    for fact in env.facts():
        if fact.template.name == "estado":
            estado = fact["valor"]

        if fact.template.name == "recomendacion":
            recomendacion = fact["accion"]


    return estado, recomendacion


@app.route("/", methods=["GET", "POST"])
def index():

    estado = None
    recomendacion = ""

    nivel_actual = 0
        
    if request.method == "POST":
        nivel_actual = int(request.form["nivel"])
        nivel_anterior = session.get("ultimo_nivel",nivel_actual)       

        estado, recomendacion = obtener_estado(nivel_anterior, nivel_actual)

        session["ultimo_nivel"] = nivel_actual


        generar_rdf(
            nivel_anterior,
            nivel_actual,
            estado,
            recomendacion
        )

        return render_template(
            "index.html",
            nivel=nivel_actual,
            anterior=nivel_anterior,
            estado=estado,
            recomendacion=recomendacion
        )

    return render_template(
        "index.html",
        nivel=0,
        anterior=0
    )


if __name__ == "__main__":
    app.run(debug=True)