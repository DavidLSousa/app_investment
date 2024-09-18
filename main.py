from flask import Flask

from router.tickets import tickets_bp
from router.news import news_bp
from router.dashboard import dashboard_bp

app = Flask(__name__)


# db.connect()
# db.create_tables([Ticket])

# Routers
app.register_blueprint(tickets_bp)
app.register_blueprint(news_bp)
app.register_blueprint(dashboard_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

# OUTRAS FORMAS DE RODAR:

# flask --app main run -
    # flask --app main run --port 3000
# flask --app main run --debug

# Atualizar requirements
# pip freeze > requirements.txt
# pip install -r requirements.txt

# DOCKER
# docker run <NAME IMAGE>
# docker ps
# docker ps -a
# docker stop <container_id>
# docker rm <container_id>

# docker build -t app_investment . -> Cria a imagem
# docker run -d -p 5000:5000 app_investment -> sobe o container, pode ser substiruido pelo docker-compose

# docker-compose up
# docker-compose down
# docker-compose up --build -> Reconstroi as imagens quando necessario (atualiza quando modificado)

# docker volume rm
