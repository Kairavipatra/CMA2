#from flask_admin import Admin
#from flask_admin.contrib.sqla import ModelView
#from app import app, db
#from app.models import User, Product

#admin = Admin(app, name='PawPal Admin', template_mode='bootstrap3')

#admin.add_view(ModelView(User, db.session))
#admin.add_view(ModelView(Product, db.session))

#if __name__ == '__main__':
 #   app.run(debug=True)

from flask import Flask, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager, current_user

# Initialize globally
db = SQLAlchemy()
admin = Admin(name='PawPal Admin', template_mode='bootstrap3')

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

# Protect Admin Panel
class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login', next=request.url))

class SecureModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login', next=request.url))


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'your_secret_key_here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pawpal.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)

    # Setup User Loader
    from app.models import User  # Assuming User model exists

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Initialize Admin with secure view
    secure_admin = Admin(app, name='PawPal Admin', template_mode='bootstrap3', index_view=MyAdminIndexView())
    secure_admin.add_view(SecureModelView(User, db.session))

    from app.models import Product
    secure_admin.add_view(SecureModelView(Product, db.session))

    from app.routes import app as app_routes
    from app.routes import auth, products, appointments, dog_walking, toys

    app.register_blueprint(app_routes.app_bp)
    app.register_blueprint(auth.auth_bp)
    app.register_blueprint(products.products_bp)
    app.register_blueprint(appointments.appointments_bp)
    app.register_blueprint(dog_walking.dog_walking_bp)
    app.register_blueprint(toys.toys_bp)

    return app
