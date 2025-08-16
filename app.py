# Importa la clase Flask del módulo flask
from flask import Flask

# Crea una instancia de la aplicación Flask
app = Flask(__name__)

# Define una ruta para la página de inicio
@app.route('/')
def hello_world():
    # Retorna el mensaje "¡Hola, Mundo!"
    return 'Un gran saludo, espero estes pasando un excelente dia'

# Este bloque se ejecuta solo si el script se corre directamente
if __name__ == '__main__':
    # Ejecuta la aplicación en modo de depuración
    # El host '0.0.0.0' hace que la aplicación sea accesible desde fuera del contenedor Docker
    app.run(host='0.0.0.0', debug=True)
