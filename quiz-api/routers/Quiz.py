from flask import Blueprint, request
from flask_cors import CORS
from services import quiz as QuizService
from services import authentification as AuthService
from sqlite3 import Connection


Quiz = Blueprint('QuizRouter', __name__)


@Quiz.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
    return QuizService.GetQuizInfo()

@Quiz.route('/question',methods=['POST'])
@AuthService.token_required #fonction de décoration pour vérifie si on est admin
def PostQuestion(): 
    return QuizService.AddQuestion()