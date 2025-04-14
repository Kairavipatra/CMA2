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
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager

# Initialize globally
db = SQLAlchemy()
admin = Admin(name='PawPal Admin', template_mode='bootstrap3')
login_manager = LoginManager()  # <-- add this!

def create_app():
    app = Flask(__name__)

    # Secret key for session management
    app.config['SECRET_KEY'] = 'your_secret_key_here'

    # Database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pawpal.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize database and admin with app
    db.init_app(app)
    admin.init_app(app)
    login_manager.init_app(app)  # <-- initialize login manager!

    # User loader function for Flask-Login
    from app.models import User, Product

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Import and register blueprints
    from app.routes import app as app_routes
    from app.routes import auth, products, appointments, dog_walking, toys

    app.register_blueprint(app_routes.app_bp)
    app.register_blueprint(auth.auth_bp)
    app.register_blueprint(products.products_bp)
    app.register_blueprint(appointments.appointments_bp)
    app.register_blueprint(dog_walking.dog_walking_bp)
    app.register_blueprint(toys.toys_bp)

    # Register models in Flask-Admin
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Product, db.session))

    return app
