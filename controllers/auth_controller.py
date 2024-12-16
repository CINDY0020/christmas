# controllers/auth_controller.py
from flask import Blueprint, request, jsonify
from models.user_model import User

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.find_user(username, password)
    if user:
        return jsonify(message="Login successful!"), 200
    else:
        return jsonify(message="Invalid username or password."), 401