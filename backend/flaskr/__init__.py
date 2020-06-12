import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
from flask_migrate import Migrate
import random
from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10


def paginate_questions(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE
    questions = [question.format() for question in selection]
    current_questions = questions[start:end] 
    return current_questions
 
 
def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    def after_request(response):
        response.headers.add(
          'Access-Control-Allow-Headers',
          'Content-Type,Authorization,true'
          )
        response.headers.add(
          'Access-Control-Allow-Methods',
          'GET,PATCH,POST,DELETE,OPTIONS'
          )
        return response

    @app.route('/categories')
    def reterive_categories():
        categories = Category.query.all()
        formated_categories = {}
        for category in categories:
            formated_categories[category.id] = category.type
        return jsonify({
          'success': True,
          'categories': formated_categories
        })
        
    @app.route('/questions')
    def reterive_questions():
        questions = Question.query.all()
        selected = paginate_questions(request, questions)
        if len(selected) == 0:
            abort(404)
        categories = Category.query.all()
        formated_categories = {}
        for category in categories:
            formated_categories[category.id] = category.type.lower()
        current_category = [question['category']for question in selected]
        return jsonify({
          'success': True,
          'questions': selected,
          'total_questions': len(questions),
          'categories': formated_categories,
          'current_category': current_category
        })

    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delete_question(question_id):
        question = Question.query.filter(
            Question.id == question_id
            ).one_or_none()
        if question is None:
            abort(404)
            
        question.delete()
        questions = Question.query.all()
        selected = paginate_questions(request, questions)
        categories = Category.query.all()
        formated_categories = {}
        for category in categories:
            formated_categories[category.id] = category.type.lower()
        current_category = [question['category']for question in selected]
        return jsonify({
            'success': True,
            'questions': selected,
            'total_questions': len(questions),
            'categories': formated_categories,
            'current_category': current_category
        })
        
    @app.route('/questions', methods=['POST'])
    def create_question():
        body = request.get_json()
        question = body.get('question', None)
        answer = body.get('answer', None)
        category = body.get('category', None)
        difficulty = body.get('difficulty', None)
        search = body.get('searchTerm', None)
        try:
            if search:
                selection = Question.query.filter(
                    Question.question.ilike('%{}%'.format(search))
                    )
                selected = paginate_questions(request, selection)
                categories = Category.query.all()
                formated_categories = {}
                for category in categories:
                    formated_categories[category.id] = category.type.lower()
                category = [question['category']for question in selected]
                return jsonify({
                    'success': True,
                    'questions': selected,
                    'total_questions': len(selection.all()),
                    'current_category': category
                })
            else:
                q = Question(
                    question=question, 
                    answer=answer,
                    category=category, 
                    difficulty=difficulty
                )
                q.insert()
                return jsonify({
                    'success': True
                  })
        except:
            abort(422)

    @app.route('/categories/<int:id>/questions')
    def get_question_by_category(id):
        questions = Question.query.filter_by(category=id).all()
        selected = paginate_questions(request, questions)
        if len(selected) == 0:
            abort(404)
        categories = Category.query.all()
        formated_categories = {}
        for category in categories:
            formated_categories[category.id] = category.type.lower()
        current_category = [question['category']for question in selected]
        return jsonify({
          'success': True,
          'questions': selected,
          'total_questions': len(questions),
          'current_category': current_category
        })
        
    @app.route('/quizzes', methods=['POST'])
    def quiz():
        body = request.get_json()
        previous_questions = body.get('previous_questions', None)
        quiz_category = body.get('quiz_category', None) 
        if quiz_category['type'] == 'click':
            questions = Question.query.filter(
                Question.id.notin_(previous_questions)
                ).all() 
            selected = [question.format() for question in questions]
            selected = random.choice(selected)
        else:
            questions = Question.query.filter(
                Question.id.notin_(previous_questions), 
                Question.category == quiz_category['id']).all() 
                
            selected = [question.format() for question in questions]
            selected = random.choice(selected)
        return jsonify({
            'success': True,
            'question': selected,
            })
        
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
          "success": False, 
          "error": 404,
          "message": "resource not found"
          }), 404
        
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
          "success": False, 
          "error": 422,
          "message": "unprocessable"
          }), 422
          
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
          "success": False, 
          "error": 400,
          "message": "bad request"
          }), 400     
          
    @app.errorhandler(500)
    def bad_request(error):
        return jsonify({
            "success": False, 
            "error": 500,
            "message": "internal server error"
        }), 500
    return app
