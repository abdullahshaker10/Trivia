import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = 'postgres://shaker:a@localhost:5432/trivia_test'
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)

            # create all tables
            self.db.create_all()
            self.correct_question = {
            'question': 'this is a trivia question',
            'answer': 'this is a trivia answer',
            'category': 1,
            'difficulty': 4
            }

            self.uncorrect_question = {
            'question': 'this is a trivia question',
            'answer': 'this is a trivia answer',
            'category': "",
            'difficulty':1 
            }

            
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    
    """ 
    def test_get_available_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['categories'])


    def test_get_questions(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'])
        self.assertTrue(data['categories'])
        self.assertTrue(data['current_category'])
        self.assertTrue(data['total_questions'])

    def test_404_unvalid_page(self):
        res = self.client().get('/questions?page=10000')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_delete_question(self):
        res = self.client().delete('/questions/3')
        data = json.loads(res.data)
        q = Question.query.get(1)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(q, None)
        self.assertTrue(data['questions'])
        self.assertTrue(data['categories'])
        self.assertTrue(data['current_category'])
        self.assertTrue(data['total_questions'])
 
    def test_404_can_not_delete_question(self):
        res = self.client().delete('/questions/1')

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_create_question(self):
        res = self.client().post('/questions', json=self.correct_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)


    def test_422_if_question_creation_fails(self):
        res = self.client().post('/questions', json=self.uncorrect_question)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    def test_get_questions_by_category(self):
        res = self.client().get('/categories/1/questions')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'])
        self.assertTrue(data['current_category'])
        self.assertTrue(data['total_questions'])

    def test_get_questions_by_category(self):

        res = self.client().delete('/questions/1')

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_show_search_result(self):
        res = self.client().post('/questions', json={'searchTerm':"ab"})

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'])
        self.assertTrue(data['current_category'])
        self.assertTrue(data['total_questions'])

    def test_play_quize(self):

        res = self.client().post('/quizzes', json={'previous_questions':[], 'quiz_category':{'type': 'Science', 'id': 1}})

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['question'])


        

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()