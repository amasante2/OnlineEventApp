from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os

# Initialize extensions globally
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    # Initialize the Flask app
    app = Flask(__name__)

    # Configure the app
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.getcwd(), 'instance', 'db.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SESSION_COOKIE_HTTPONLY'] = True
    app.config['SESSION_COOKIE_SECURE'] = True  # Enable for HTTPS
    app.config['REMEMBER_COOKIE_HTTPONLY'] = True

    # Initialize extensions with the app
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    
    # Set up the login manager
    login_manager.login_view = "views.login"  # Use the Blueprint's route
    
    # Import and register the Blueprint for views
    from .views import views
    app.register_blueprint(views)

    # Return the app instance
    return app



