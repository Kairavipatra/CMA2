from flask import Flask

def create_app():
    app = Flask(__name__)
    from app.routes import app_bp 
    from app.routes import auth, products, appointments, dog_walking, toys, app as app_routes
    app.register_blueprint(app_bp)
    app.register_blueprint(auth.auth_bp)
    app.register_blueprint(products.products_bp)
    app.register_blueprint(appointments.appointments_bp)
    app.register_blueprint(dog_walking.dog_walking_bp)
    app.register_blueprint(toys.toys_bp)
    app.register_blueprint(app_routes.app_bp)

    return app
