import unittest
import requests
import json
import bcrypt

headers = {
    'content-type': 'application/json'
}

data = {
    'username': 'Kevin',
    'email': 'kmit@test.com',
    'password': 'testpassword'
}

bad_data = {
    'username': 'Kevin',
    'password': 'testpassword'
}

class TestUsers(unittest.TestCase):

    def test_01_create_user(self):
        """Should create a user"""
        res = requests.post('http://localhost:5000/users',
            headers=headers, data=json.dumps(data))
        self.assertEqual(res.status_code, 201)
        user = res.json()
        self.assertEqual(user['username'], 'Kevin')
        self.assertEqual(user['email'], 'kmit@test.com')
        self.assertEqual(bcrypt.hashpw('testpassword',
            str(user['pwhash'])), user['pwhash'])

    def test_02_create_user_duplicate(self):
        """Should not create a duplicate user"""
        res = requests.post('http://localhost:5000/users',
            headers=headers, data=json.dumps(data))
        self.assertEqual(res.status_code, 409)

    def test_021_create_bad_user(self):
        """Should not create a user without an email"""
        res = requests.post('http://localhost:5000/users',
            headers=headers, data=json.dumps(bad_data))
        self.assertEqual(res.status_code, 400)

    def test_03_get_all_users(self):
        """Should get all users"""
        res = requests.get('http://localhost:5000/users', headers=headers)
        users = res.json()

    def test_04_get_user(self):
        """Should get a specific user"""
        res = requests.get(
            'http://localhost:5000/users/Kevin', headers=headers)
        user = res.json()
        self.assertEqual(user['username'], 'Kevin')
        self.assertEqual(user['email'], 'kmit@test.com')

    def test_041_get_missing(self):
        """Should return 404 for a non-existent user"""
        res = requests.get(
            'http://localhost:5000/users/Dave', headers=headers)
        self.assertEqual(res.status_code, 404)

    def test_99_delete_user(self):
        """Should delete a user"""
        res = requests.delete(
            'http://localhost:5000/users/Kevin', headers=headers)
        self.assertEqual(res.status_code, 204)
