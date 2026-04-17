import unittest
import json
from app import create_app, db

class AuthTestCase(unittest.TestCase):
    def setUp(self):
        # Set up a temporary testing app and an in-memory database
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        # Clean up the database after every test
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_registration(self):
        # Test creating a new user
        response = self.client.post('/api/auth/register', 
            data=json.dumps({'email': 'testuser@example.com', 'password': 'password123'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn('User created successfully', response.get_data(as_text=True))

    def test_login(self):
        # Register a user first
        self.client.post('/api/auth/register', 
            data=json.dumps({'email': 'loginuser@example.com', 'password': 'password123'}),
            content_type='application/json'
        )
        
        # Then try to log in
        response = self.client.post('/api/auth/login', 
            data=json.dumps({'email': 'loginuser@example.com', 'password': 'password123'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn('access_token', response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()