Instalación
Clonar el repositorio:

git clone https://github.com/tu-usuario/sistema-experto-tinas.git

cd sistema-experto-tinas
Crear entorno virtual:

conda create -n tinas python=3.11

conda activate tinas
Instalar dependencias:

pip install -r requirements.txt

Ejecución
Iniciar servidor Flask:

python app.py
Abrir en navegador:

http://localhost:5000

Flujo de Funcionamiento

El usuario mueve el control deslizante para indicar el nivel actual de agua.
Flask almacena el valor anterior utilizando sesiones.
CLIPSpy recibe ambos valores.
El motor de inferencia ejecuta las reglas expertas.
Se determina el estado de la tina.
Se genera una recomendación automática.
Los resultados son almacenados como tripletas RDF.
La interfaz muestra el resultado al usuario.

Futuras Mejoras
Integración con sensores IoT.
Persistencia en base de datos.
Consultas SPARQL sobre el conocimiento generado.
Historial de estados de la tina.
Dashboard analítico.
Exportación RDF en formato Turtle y JSON-LD.
Múltiples tinas simultáneas.
Autor: Jesus Hernandez
Proyecto académico desarrollado como práctica de Inteligencia Artificial, Sistemas Expertos y Web Semántica utilizando CLIPSpy, RDFLib y Flask.

Licencia
Este proyecto se distribuye con fines educativos y académicos.