from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_login import LoginManager
from flask_socketio import SocketIO

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
admin = Admin(app)
login = LoginManager(app)
login.login_view = 'login'
socketio = SocketIO(app)

with app.app_context():
    migrate.init_app(app, db)

from app import routes, model
