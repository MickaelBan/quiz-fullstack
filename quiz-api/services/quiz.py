from flask import jsonify
from model import engine, Question
from sqlite3 import Error, Cursor


def GetQuizInfo():
    conn = engine.db_connect()
    cursor = conn.cursor()
    sql_query = "SELECT playerName,score,date FROM scores ORDER BY score DESC;"
    try:
        sql_result = cursor.execute(sql_query).fetchall()
        engine.close_connect(conn)
        return jsonify({"size": len(sql_result), "scores": sql_result}), 200
    except Error as e:
        engine.close_connect(conn)
        return "ERROR DataBase: " + str(e), 500


def insertPosition(cursor: Cursor, qt: Question):
    sql_query = "SELECT position from questions WHERE position=" + str(qt.position)
    cursor.execute(sql_query)
    if cursor.fetchone() is not None:
        sql_query = "UPDATE questions SET position = position + 1 WHERE position >= " + \
            str(qt.position)
        cursor.execute(sql_query)


def addAnswers(cursor: Cursor, qt: Question,id):
    for i in range(len(qt.possibleAnswers)):
        sql_query = "INSERT INTO possibleAnswers (idQuestion,text,isCorrect) VALUES (\"" +\
            str(id) + "\",\"" + \
            qt.possibleAnswers[i]['text'] + "\",\"" + \
            str(qt.possibleAnswers[i]['isCorrect']) + "\");"
        cursor.execute(sql_query)

def checkPosition(cursor:Cursor,qt:Question):
    cursor.execute("SELECT MAX(position) FROM questions")
    maxPosition = cursor.fetchone()[0]
    if maxPosition is not None and qt.position > int(maxPosition) + 1:
        return False
    return True
        

def AddQuestion(request):
    qt = Question.parseRequestToQuestion(request)
    cursor = engine.db_cursor()
    cursor.execute("begin")
    try:
        
        if not checkPosition(cursor,qt):            
            cursor.execute('rollback')
            engine.close_connect(cursor)
            return "Bad request: the position is too high",400
        
        # increment other position if position is occuped
        insertPosition(cursor, qt)

        # add question
        sql_query = "INSERT INTO questions (title,position,text,image) VALUES (\"" + \
            qt.title+"\",\"" + \
            str(qt.position) + "\",\"" + \
            qt.text + "\",\"" + \
            qt.image + \
            "\");"
        cursor.execute(sql_query)
        id = cursor.lastrowid

        addAnswers(cursor, qt,id)

        cursor.execute("commit")
        engine.close_connect(cursor)
        return {"id": id}, 200

    except Error as e:
        cursor.execute("rollback")
        engine.close_connect(cursor)
        return "ERROR in database: " + str(e), 500


def deleteOneQuestion(idQuestion):
    cursor = engine.db_cursor()
    cursor.execute("begin")
    try:
        sql_query = "DELETE FROM possibleAnswers WHERE idQuestion = " + str(idQuestion) + ";"
        cursor.execute(sql_query)
        sql_query = "DELETE FROM questions WHERE questions.id = " + str(idQuestion) + ";"
        cursor.execute(sql_query)
        # if cursor.execute("SELECT * FROM questions WHERE id = " + str(idQuestion)).fetchone() is not None:
        #     cursor.execute('rollback')
        #     engine.close_connect(conn)
        #     return "ERROR delete",500
        cursor.execute('commit')
        engine.close_connect(cursor)
        return '', 204
    except Error as e:
        cursor.execute('rollback')
        engine.close_connect(cursor)
        return "ERROR Database :" + str(e), 500


def deleteAllQuestions():
    cursor = engine.db_cursor()
    cursor.execute('begin')
    try:
        cursor.execute("DELETE FROM possibleAnswers")
        cursor.execute("DELETE FROM questions")
        cursor.execute('commit')
        engine.close_connect(cursor)
        return '', 204
    except Error as e:
        # print(e)
        cursor.execute('roolback')
        engine.close_connect(cursor)
        return "ERROR database: " + str(e), 500

def updateQuestion(request,idQuestion):
    cursor = engine.db_cursor()
    cursor.execute('begin')
    try :
        qt = Question.parseRequestToQuestion(request)
        if not checkPosition(cursor,qt):
            cursor.execute('rollback')
            engine.close_connect(cursor)
            return "Bad request: the position is too high",400
        
        actuelPosition = cursor.execute("SELECT position FROM questions WHERE id = " + str(idQuestion) ).fetchone()
        maxIdD = cursor.execute("SELECT MAX(id) FROM questions").fetchone()[0]
        if (maxIdD is not None and maxIdD < idQuestion) or maxIdD is None:
            return "Not Found", 404
        if  qt.position != int(actuelPosition[0]) :
            insertPosition(cursor,qt)
        
        sql_query = "UPDATE questions SET " + \
            "title = \"" + qt.title + "\"," + \
            "position = " + str(qt.position) + "," + \
            "text = \"" + qt.text + "\"," + \
            "image = \"" +qt.image + "\"" + \
            "WHERE id = " + str(idQuestion) + ";" 
        cursor.execute(sql_query)
        
        cursor.execute("DELETE FROM possibleAnswers WHERE idQuestion = " + str(idQuestion) + ";")
        addAnswers(cursor,qt,idQuestion)
        
        cursor.execute('commit')
        engine.close_connect(cursor)
        return '',204
    
    except (Error,Exception) as e:
        cursor.execute('rollback')
        engine.close_connect(cursor)
        return "Error database: " + str(e),500

def deleteAllParticipations():
    cursor = engine.db_cursor()
    cursor.execute('begin')
    try:
       cursor.execute("DELETE FROM scores")
       cursor.execute('commit')
       engine.close_connect(cursor)
       return '',204
    except (Error) as e:
        cursor.execute('rollback')
        engine.close_connect(cursor)
        return "Error database: " + str(e),500    
    
def GetQuestionById(questionId:int):
    cursor = engine.db_cursor()
    try:
        maxIdD = cursor.execute("SELECT MAX(id) FROM questions").fetchone()[0]
        if (maxIdD is not None and int(maxIdD) < int(questionId)) or maxIdD is None:
            return "Not Found", 404
        qt = Question.parseDbToQuestion(cursor,questionId)
        engine.close_connect(cursor)
        return qt.parseQuestionToJson(),200
    except (Error) as e:
        engine.close_connect(cursor)
        return "Error database: " + str(e),500    
        
def GetQuestionByPosition(position:int):
    cursor = engine.db_cursor()
    try:
        maxPos = cursor.execute("SELECT MAX(position) FROM questions").fetchone()[0]
        if (maxPos is not None and int(maxPos) < int(position)) or maxPos is None:
            return "Not Found", 404
        
        questionId = cursor.execute("SELECT id FROM questions " +\
            "WHERE position = " + str(position)).fetchone()[0] 
        qt = Question.parseDbToQuestion(cursor,questionId)
        engine.close_connect(cursor)
        return qt.parseQuestionToJson(),200
    except (Error) as e:
        engine.close_connect(cursor)
        return "Error database: " + str(e),500    
        