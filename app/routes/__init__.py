from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = 'supersecretkey'  # for session & forms

    from app.routes import auth, products, appointments, dog_walking, toys

    app.register_blueprint(auth.bp)
    app.register_blueprint(products.bp)
    app.register_blueprint(appointments.bp)
    app.register_blueprint(dog_walking.bp)
    app.register_blueprint(toys.bp)

    return app
