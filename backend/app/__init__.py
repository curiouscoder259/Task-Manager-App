

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_cors import CORS

# 1. Create the extension instances globally
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
ma = Marshmallow()

def create_app():
    # 2. Initialize the Flask app
    app = Flask(__name__)
    
    # 3. Load the configuration from config.py
    from config import Config
    app.config.from_object(Config)

    # 4. Bind extensions to the app
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    ma.init_app(app)
    
    # Allow the React frontend to talk to this backend
    CORS(app) 

    # 5. Import models
    from app import models

    # 6. REGISTER ROUTES (This is what was missing!)
    from app.routes.auth import auth_bp
    from app.routes.tasks import tasks_bp
    
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(tasks_bp, url_prefix='/api/tasks')

    return app