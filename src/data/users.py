from models import User
from init_db import get_db
from sqlalchemy import select
from typing import Dict

def create_user(username: str, password_hash: str, email: str) -> Dict[str, str]:
    with get_db() as session:
        with session.begin():
            user = User(
                username=username,
                password_hash=password_hash,
                email=email
            )
            session.add(user)
        return user_to_json(user)
    

def get_user(username: str) -> Dict[str, str]:
    with get_db() as session:
        user = session.query(User).filter(User.username == username).one()
        return user_to_json(user)

def user_to_json(user: User) -> Dict[str, str]:
    return dict(
        id=user.id,
        username=user.username,
        password_hash=user.password_hash,
        email=user.email
    )