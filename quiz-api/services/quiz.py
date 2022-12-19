from flask import jsonify
from model import engine,Question
from sqlite3 import Error



def GetQuizInfo():
    conn = engine.db_connect()
    cursor = conn.cursor()
    sql_query = "SELECT playerName,score,date FROM scores ORDER BY score DESC;"
    try:
        sql_result = cursor.execute(sql_query).fetchall()
        engine.close_connect(conn)
        return jsonify({"size":len(sql_result),"scores":sql_result}), 200
    except Error as e:
        engine.close_connect(conn)
        return "ERROR DataBase: " + str(e), 500


def AddQuestion(request):
    qt = ParseRequestToQuestion(request)
    conn = engine.db_connect()
    cursor = conn.cursor() 
    cursor.execute("begin")
    try:
        # check if postion is unique
        sql_query = "SELECT position from questions WHERE position=" + str(qt.position)
        cursor.execute(sql_query)
        if cursor.fetchone() is not None:
            sql_query = "UPDATE questions SET position = position + 1 WHERE position >= " + str(qt.position)
            cursor.execute(sql_query)
        
        #add question
        sql_query = "INSERT INTO questions (title,position,text,image) VALUES (\"" + \
            qt.title+"\",\"" + \
            str(qt.position) + "\",\"" + \
            qt.text + "\",\"" + \
            qt.image + \
            "\");"
        cursor.execute(sql_query)
        id = cursor.lastrowid
        
        
        #add answers 
        for i in range(len(qt.possibleAnswers)):
            sql_query = "INSERT INTO possibleAnswers (idQuestion,text,isCorrect) VALUES (\"" +\
                str(id) + "\",\"" + \
                qt.possibleAnswers[i]['text'] + "\",\"" + \
                str(qt.possibleAnswers[i]['isCorrect']) + "\");"
            cursor.execute(sql_query)
               
        cursor.execute("commit")
        engine.close_connect(conn)
        return {"id": id}, 200
    
    except Error as e : 
        print(e)
        cursor.execute("rollback")
        engine.close_connect(conn)
        return e,500 




def ParseRequestToQuestion(request) -> Question:
    js = request.get_json()
    return Question(title=js['title'],
                    position=js['position'],
                    text=js['text'],
                    image=js['image'],
                    possibleAnswers=js['possibleAnswers'])


def parseQuestionToJson(Question: Question):
    # todo
    pass
