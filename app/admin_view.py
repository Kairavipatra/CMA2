from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app import app, db
from app.models import User, Product

admin = Admin(app, name='PawPal Admin', template_mode='bootstrap3')

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Product, db.session))

if __name__ == '__main__':
    app.run(debug=True)
