import os
from app import create_app
from app import db
db.create_all()
app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))  # Render injects PORT env variable.
    app.run(host='0.0.0.0', port=port)
