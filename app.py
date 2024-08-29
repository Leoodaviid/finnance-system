from flask import Flask
from routes import init_routes
from config import Config
from models import db

app = Flask(__name__)
app.config.from_object(Config)

# Inicializa as rotas
init_routes(app)

# Inicializa o banco de dados
db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Cria as tabelas no banco de dados
    app.run(debug=True)
