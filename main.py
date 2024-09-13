from flask import Flask
from router.tickets import tickets_bp

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<p>Hello, World!</p>'

app.register_blueprint(tickets_bp)

if __name__ == '__main__':
    app.run(debug=True)

# OUTRAS FORMAS DE RODAR:

# flask --app main run -
    # flask --app main run --port 3000
# flask --app main run --debug