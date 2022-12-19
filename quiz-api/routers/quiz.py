from flask import Blueprint, request
from flask_expects_json import expects_json

from schemas import QuestionSchema
from services import quiz as QuizService
from services import authentification as AuthService


quiz = Blueprint('QuizRouter', __name__)


@quiz.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
    return QuizService.GetQuizInfo()

@quiz.route('/questions',methods=['POST'])
@AuthService.token_required #fonction de décoration pour vérifie si on est admin
@expects_json(QuestionSchema)
def PostQuestion(): 
    return QuizService.AddQuestion(request)

@quiz.route('/questions/<idQuestion>',methods=['DELETE'])
@AuthService.token_required
def DeleteOneQuestion(idQuestion):
    return QuizService.deleteOneQuestion(idQuestion)


