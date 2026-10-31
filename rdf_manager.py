from rdflib import Graph
from rdflib import Namespace
from rdflib import Literal


def generar_rdf(nivel_anterior, nivel_actual,estado,recomendacion):
    g = Graph()

    EX = Namespace("http://www.ejemplo.org/tinas/")

    tina = EX["Tina1"]

    g.add((tina,EX.nivelAnterior, Literal(nivel_anterior)))
    g.add((tina,EX.nivelActual,Literal(nivel_actual)))
    g.add((tina,EX.estado,Literal(estado)))
    g.add((tina,EX.recomendacion,Literal(recomendacion)))
    g.serialize(destination="salida_tina.rdf",format="xml")

    return g