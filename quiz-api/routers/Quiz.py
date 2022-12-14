from flask import Blueprint, request
from flask_cors import CORS
from services import quiz as QuizService
Quiz = Blueprint('QuizRouter', __name__)


@Quiz.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
    return QuizService.GetQuizInfo()
