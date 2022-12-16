from model import Question
from flask import json, request, jsonify
from flask_expects_json import expects_json
from model import engine
from sqlite3 import Error


def GetQuizInfo():
    return {"size": 0, "scores": []}, 200


def AddQuestion():
    qt = ParseRequestToQuestion()
        
    conn = engine.db_connect()
    cursor = conn.cursor() 
    cursor.execute("begin")
    try:
        sql_query = "INSERT INTO questions (title,position,text,image) VALUES (\"" + \
            qt.title+"\",\"" + \
            str(qt.position) + "\",\"" + \
            qt.text + "\",\"" + \
            qt.image + \
        "\");"
        cursor.execute(sql_query)         
        id = cursor.lastrowid
        
        for i in range ( len(qt.possibleAnswers)):
            sql_query = "INSERT INTO possibleAnswers (idQuestion,text,isCorrect) VALUES (\""+\
                str(id) + "\",\"" + qt.possibleAnswers[i]['text'] + "\",\"" + str(qt.possibleAnswers[i]['isCorrect']) +"\"" \
                + ");"
            cursor.execute(sql_query)
            engine.close_connect(conn)
            
            return {"id":id},200
        
        cursor.execute("commit") 
    except Error as e:
        cursor.execute("rollback")
        engine.close_connect(conn)
        return "Bad request: " +str(e),400


def ParseRequestToQuestion() -> Question:
    js = request.get_json()
    return Question(title=js['title'], 
                    position=js['position'], 
                    text=js['text'], 
                    image=js['image'], 
                    possibleAnswers=js['possibleAnswers'])


def parseQuestionToJson(Question: Question):
    pass
