from flask import Blueprint,request
from flask_cors import CORS

Quiz = Blueprint('QuizRouter', __name__)

@Quiz.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
	return {"size": 0, "scores": []}, 200

