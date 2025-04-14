#from flask import Flask

#def create_app():
 #   app = Flask(__name__)
  #  app.secret_key = 'supersecretkey'  # for session & forms

   # from app.routes import auth, products, appointments, dog_walking, toys

    #app.register_blueprint(auth.bp)
    #app.register_blueprint(products.bp)
    #app.register_blueprint(appointments.bp)
    #app.register_blueprint(dog_walking.bp)
    #app.register_blueprint(toys.bp)

    #return app

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize the SQLAlchemy object globally
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Secret key for session management (recommended!)
    app.config['SECRET_KEY'] = 'your_secret_key_here'

    # Database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pawpal.db'  # For file-based local DB
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize database with app
    db.init_app(app)

    # Import all blueprints
    from app.routes import app as app_routes
    from app.routes import auth, products, appointments, dog_walking, toys

    # Register blueprints
    app.register_blueprint(app_routes.app_bp)  # General pages like /, /blog etc.
    app.register_blueprint(auth.auth_bp)
    app.register_blueprint(products.products_bp)
    app.register_blueprint(appointments.appointments_bp)
    app.register_blueprint(dog_walking.dog_walking_bp)
    app.register_blueprint(toys.toys_bp)

    return app
