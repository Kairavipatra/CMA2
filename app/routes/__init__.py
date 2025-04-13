from flask import Flask

def create_app():
    app = Flask(__name__)

    from .routes import app as app_routes
    from .routes import appointments
    from .routes import auth
    from .routes import dog_walking
    from .routes import products
    from .routes import toys

    app.register_blueprint(app_routes.app_bp)
    app.register_blueprint(appointments.appointments_bp)
    app.register_blueprint(auth.auth_bp)
    app.register_blueprint(dog_walking.dog_walking_bp)
    app.register_blueprint(products.products_bp)
    app.register_blueprint(toys.toys_bp)

    return app
