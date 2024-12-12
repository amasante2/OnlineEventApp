from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os

# Initialize Flask app
app = Flask(__name__)

# Configure the app with the database URI and other settings
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.getcwd(), 'instance', 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable Flask-SQLAlchemy's modification tracking
app.config['SECRET_KEY'] = 'your_secret_key'  # Set a secret key for session management and cookies
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SECURE'] = True  # Enable for HTTPS
app.config['REMEMBER_COOKIE_HTTPONLY'] = True

# Initialize the SQLAlchemy extension with the app
db = SQLAlchemy(app)

# Initialize Flask-Migrate with the app and db
migrate = Migrate(app, db)

# Initialize Flask-Login for managing user sessions
login_manager = LoginManager(app)
login_manager.login_view = "login"  # Set login view for flask-login

# Import models (ensure they are defined in models.py)
from models import User

# Set up the login manager to load the user
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Import routes from views.py
from views import *

# The section to create the tables when the script is run directly
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # This will create all tables defined in the models
    app.run(debug=True)


