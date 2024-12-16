# middleware/cors_middleware.py
from flask_cors import CORS as FlaskCORS

def CORS(app):
    FlaskCORS(app)