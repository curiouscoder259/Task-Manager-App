from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from app.models import User
from app import db

# THIS is the variable your __init__.py is looking for!
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({"error": "Missing email or password", "code": "VALIDATION_ERROR"}), 400

    if User.query.filter_by(email=data['email']).first():
        return jsonify({"error": "User already exists", "code": "USER_EXISTS"}), 400

    new_user = User(
        email=data['email'],
        password_hash=generate_password_hash(data['password'])
    )
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User created successfully"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data.get('email')).first()

    if not user or not check_password_hash(user.password_hash, data.get('password')):
        return jsonify({"error": "Invalid credentials", "code": "AUTH_FAILED"}), 401

    # We wrap the ID in str() to make the security library happy
    access_token = create_access_token(identity=str(user.id))
    return jsonify(access_token=access_token, user_id=str(user.id)), 200