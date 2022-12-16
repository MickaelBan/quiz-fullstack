from model import Question
from flask import json,request,jsonify
from schemas import question
from flask_expects_json import expects_json
from model import engine



def GetQuizInfo():
    return {"size": 0, "scores": []}, 200

# @expects_json(question)
def AddQuestion():
    
    sql_query = """INSERT INTO questions (title,position,text,image) VALUES ('QSDs',2,'dqqdq','qddzd')""" 
    sql_query += ""
    
    engine.execute(sql_query=sql_query)
    
    # id = cursor.execute("SELECT id FROM question WHERE text=" + Question.text )
    
    return {'id question': 'null'},200

@expects_json(question)
def ParseRequestToQuestion() -> Question:
    js = request.get_json()   
    return Question(title=js['title'], position=js['position'], text=js['text'], image=js['image'],possibleAnswers=js['possibleAnswers'])

def parseQuestionToJson(Question: Question):
    pass
    