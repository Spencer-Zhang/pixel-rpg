"""
Endpoints for user management
"""
import json

from flask import Blueprint, request, Response
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from managers.user import UserManager

bp_users = Blueprint('users', __name__)

pg_client = create_engine('postgres://127.0.0.1/pixel')
Session = sessionmaker(bind=pg_client)

users = UserManager()

@bp_users.route('/users', methods=['POST'])
def create_user():
    try:
        session = Session()
        data = json.loads(request.data)
        username = data['username']
        email = data['email']
        password = str(data['password'])
        user = users.create_user(session, username, email, password)
        res = json.dumps(user.json), 201
    except KeyError as e:
        res = 'Invalid user model', 400
    except Exception as e:
        if 'Key (username)' in e.message:
            res = 'Username {} is already used'.format(username), 409
        elif 'Key (email)' in e.message:
            res = 'Email {} is already used'.format(email), 409
        else:
            res = e.message, 500
    finally:
        session.close()
        return res

@bp_users.route('/users', methods=['GET'])
def get_users():
    session = Session()
    res = users.get_users(session)
    session.close()
    return json.dumps([user.json for user in res]), 200

@bp_users.route('/users/<username>', methods=['GET'])
def get_user(username):
    session = Session()
    user = users.get_user(session, {'username': username})
    session.close()
    return json.dumps(user.json), 200

@bp_users.route('/users/<username>', methods=['DELETE'])
def delete_user(username):
    session = Session()
    user = users.get_user(session, {'username': username})
    users.delete_user(session, user)
    session.close()
    return '', 204

