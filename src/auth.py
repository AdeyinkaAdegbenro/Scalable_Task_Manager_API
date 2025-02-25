import os
import jwt
from dotenv import load_dotenv
from flask import Blueprint
from flask import request, g
from functools import wraps
from data.users import create_user, get_user
from typing import Dict
from werkzeug.security import generate_password_hash, check_password_hash

auth_blueprint = Blueprint('auth', __name__, url_prefix='/auth')

load_dotenv()

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

@auth_blueprint.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data['username']
    password_hash = generate_password_hash(data['password'])
    email = data['email']
    user = create_user(username, password_hash, email)
    return (user, 201)

@auth_blueprint.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data['username']
    user = get_user(username)
    if not check_password_hash(user['password_hash'], data['password']):
        return ('Username/password incorrect', 400)
    jwt_token = generate_access_token(user)
    return (jwt_token, 201)


def generate_access_token(payload: Dict[str, str]) -> str:
    del payload['password_hash']
    token = jwt.encode(payload, JWT_SECRET_KEY, algorithm="HS256")
    return token

def jwt_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        headers = request.headers
        bearer = headers.get('Authorization')
        token = bearer.split()[1] 
        print(token)
        if not verify_token(token):
            return "Invalid signature - access not granted"
        return f(*args, **kwargs)
    return decorated_function

def verify_token(token):
    payload = jwt.decode(token, JWT_SECRET_KEY, algorithms="HS256")
    user = get_user(payload['username'])
    del user['password_hash']
    if user == payload:
        g.user = user
        return True
    return False

