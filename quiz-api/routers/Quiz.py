from flask import Blueprint, request
from flask_cors import CORS
from services import quiz as QuizService
from services import authentification as AuthService
from schemas import QuestionSchema
from flask_expects_json import expects_json


quiz = Blueprint('QuizRouter', __name__)


@quiz.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
    return QuizService.GetQuizInfo()

@quiz.route('/question',methods=['POST'])
@AuthService.token_required #fonction de décoration pour vérifie si on est admin
@expects_json(QuestionSchema)
def PostQuestion(): 
    return QuizService.AddQuestion()