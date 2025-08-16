from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hola ITLA - Un enorme saludo desde mi casa!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
