from flask import Flask
from router.tickets import tickets_bp
from router.news import news_bp
from router.dashboard import dashboard_bp

app = Flask(__name__)

app.register_blueprint(tickets_bp)
app.register_blueprint(news_bp)
app.register_blueprint(dashboard_bp)

if __name__ == '__main__':
    app.run(debug=True)

# OUTRAS FORMAS DE RODAR:

# flask --app main run -
    # flask --app main run --port 3000
# flask --app main run --debug