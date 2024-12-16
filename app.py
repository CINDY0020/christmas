# app.py
from flask import Flask, render_template
from flask_cors import CORS
from controllers.auth_controller import auth_blueprint

app = Flask(__name__)

# Apply CORS middleware
CORS(app)

# Register the authentication controller
app.register_blueprint(auth_blueprint)

# Define a route for the root URL to serve the main.html
@app.route('/')
def home():
    return render_template('main.html')

if __name__ == '__main__':
    app.run(port=5000)