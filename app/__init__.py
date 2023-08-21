from flask import Flask
from app.extensions import db, bcrypt, migrate, jwt
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
        
    # Initialize Flask extensions here
    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Register blueprints here
    from app.main import bp as main_bp
    from app.users import bp as user_bp
    app.register_blueprint(main_bp, url_prefix='/main')
    app.register_blueprint(user_bp, url_prefix='/users')

    @app.route('/')
    def hello():
        return 'Hello Flask Application Up running at http://localhost:'

    return app