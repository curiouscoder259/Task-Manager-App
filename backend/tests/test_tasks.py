import unittest
import json
from app import create_app, db

class TasksTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()
            
            # Register and log in a user to get a valid token for testing
            self.client.post('/api/auth/register', 
                data=json.dumps({'email': 'taskuser@example.com', 'password': 'password123'}),
                content_type='application/json'
            )
            login_response = self.client.post('/api/auth/login', 
                data=json.dumps({'email': 'taskuser@example.com', 'password': 'password123'}),
                content_type='application/json'
            )
            data = json.loads(login_response.get_data(as_text=True))
            self.token = data['access_token']
            
            # Set up the authorization header
            self.headers = {
                'Authorization': f'Bearer {self.token}',
                'Content-Type': 'application/json'
            }

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_task(self):
        response = self.client.post('/api/tasks/', 
            headers=self.headers,
            data=json.dumps({'title': 'Learn PyTest', 'description': 'Write some automated tests.'})
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn('Learn PyTest', response.get_data(as_text=True))

    def test_get_tasks(self):
        # Create a task first
        self.client.post('/api/tasks/', headers=self.headers, data=json.dumps({'title': 'Test Task'}))
        
        # Then fetch all tasks
        response = self.client.get('/api/tasks/', headers=self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Test Task', response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()