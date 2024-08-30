from flask_wtf.csrf import CSRFProtect
from flask import Flask
from flask_login import LoginManager
from routes import init_routes
from auth import auth_bp
from config import Config
from models import db, User
from extensions import limiter 
from config import DevelopmentConfig, TestingConfig, ProductionConfig
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

app = Flask(__name__)

# Definir a configuração com base na variável de ambiente
env = os.getenv('FLASK_ENV', 'development')

if env == 'development':
    app.config.from_object(DevelopmentConfig)
elif env == 'testing':
    app.config.from_object(TestingConfig)
else:
    app.config.from_object(ProductionConfig)

# Inicializa o Rate Limiting
limiter.init_app(app)

# Inicializa a proteção CSRF
csrf = CSRFProtect(app)

# Configuração do Flask-Login
login = LoginManager(app)
login.login_view = 'auth.login'

@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))

# Inicializa as rotas
init_routes(app)

# Inicializa as rotas de autenticação
app.register_blueprint(auth_bp, url_prefix='/auth')

# Inicializa o banco de dados
db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Cria as tabelas no banco de dados
    app.run(debug=True)
