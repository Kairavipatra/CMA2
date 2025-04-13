from flask import Flask, render_template

app_bp = Flask(__name__)

@app_bp.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=10000)
