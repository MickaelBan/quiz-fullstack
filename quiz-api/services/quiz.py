from flask import jsonify
from model import engine, Question
from sqlite3 import Error, Cursor
from datetime import datetime
    
def insertPosition(cursor: Cursor, qt: Question):
    sql_query = "SELECT position from questions WHERE position=" + str(qt.position)
    cursor.execute(sql_query)
    if cursor.fetchone() is not None:
        sql_query = "UPDATE questions SET position = position + 1 WHERE position >= " + \
            str(qt.position)
        cursor.execute(sql_query)
    else :
        pass
        
def changeCurrentPosition(cursor:Cursor,newPosition,currentPosition) :
    if (currentPosition > newPosition):
        sql_query = "UPDATE questions SET position = position + 1  WHERE position >= " + str(newPosition)  + \
                                                                " and position < " + str(currentPosition)
    else : 
        sql_query = "UPDATE questions SET position = position - 1  WHERE position <= " + str(newPosition)  + \
                                                                " and position > " + str(currentPosition) 
    cursor.execute(sql_query)
    
def getCurrentPosition(cursor:Cursor,idQuestion:int) -> int:
    currentPosition = cursor.execute("SELECT position FROM questions WHERE id = " + str(idQuestion) ).fetchone()[0]
    return int(currentPosition)

def updateQuestion(cursor:Cursor,qt:Question):
    sql_query = "UPDATE questions SET " + \
            "title = \"" + qt.title + "\"," + \
            "position = " + str(qt.position) + "," + \
            "text = \"" + qt.text + "\"," + \
            "image = \"" + qt.image + "\"" + \
            "WHERE id = " + str(qt.id) + ";" 
    cursor.execute(sql_query)
   
def addAnswers(cursor: Cursor, qt: Question):
    for i in range(len(qt.possibleAnswers)):
        sql_query = "INSERT INTO possibleAnswers (idQuestion,text,isCorrect) VALUES (\"" +\
            str(qt.id) + "\",\"" + \
            qt.possibleAnswers[i]['text'] + "\",\"" + \
            str(qt.possibleAnswers[i]['isCorrect']) + "\");"
        cursor.execute(sql_query)

def checkPosition(cursor:Cursor,position:int) -> bool:    
    cursor.execute("SELECT MAX(position) FROM questions")
    maxPosition = cursor.fetchone()[0]
    if maxPosition is not None and int(position) > int(maxPosition) + 1:
        return False
    return True

def checkID(cursor:Cursor,idQuestion:int) -> bool:
    maxIdD = cursor.execute("SELECT MAX(id) FROM questions").fetchone()[0]
    if (maxIdD is not None and maxIdD < idQuestion) or maxIdD is None:
        return False
    return True
    
         
def GetQuizInfo():
    cursor = engine.db_cursor()
    sql_query = "SELECT playerName,score,date FROM scores ORDER BY score DESC;"
    try:
        sql_result = cursor.execute(sql_query).fetchall()
        scores = [{"playerName": playerName, "score":score,"date":date}for playerName,score,date in sql_result]
        nbQuestion = cursor.execute("SELECT COUNT(*) FROM questions").fetchone()[0]
        engine.close_connect(cursor)
        return jsonify({"size": nbQuestion, "scores": scores}), 200
    except Error as e:
        engine.close_connect(cursor)
        return "ERROR DataBase: " + str(e), 500
    except Exception as e:
        cursor.execute('rollback')
        engine.close_connect(cursor)
        return "Error: " + str(e),500

def AddQuestion(request):
    cursor = engine.db_cursor()
    cursor.execute("begin")
    try:
        qt = Question.parseRequestToQuestion(request,idInDB=None)
        if not checkPosition(cursor,qt.position):            
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
        qt.id = cursor.lastrowid

        addAnswers(cursor, qt)

        cursor.execute("commit")
        engine.close_connect(cursor)
        return {"id": qt.id}, 200

    except Error as e:
        cursor.execute("rollback")
        engine.close_connect(cursor)
        return "ERROR in database: " + str(e), 500
    except Exception as e:
        cursor.execute('rollback')
        engine.close_connect(cursor)
        return "Error: " + str(e),500


def DeleteOneQuestion(idQuestion):
    cursor = engine.db_cursor()
    cursor.execute("begin")
    try:
        #verify if the id exist
        if not checkID(cursor,idQuestion):
            cursor.execute('rollback')
            engine.close_connect(cursor)
            return 'Not Found: check id', 404
        
        # decrements position of questions below the deletede question
        currentPosition = getCurrentPosition(cursor,idQuestion)
        cursor.execute("UPDATE questions SET position = position - 1 WHERE position > " + str(currentPosition))
        
        #delete answers of the question in first because they have a foreign key
        sql_query = "DELETE FROM possibleAnswers WHERE idQuestion = " + str(idQuestion) + ";"
        cursor.execute(sql_query)
        
        #delete the question
        sql_query = "DELETE FROM questions WHERE questions.id = " + str(idQuestion) + ";"
        cursor.execute(sql_query)
        
        cursor.execute('commit')
        engine.close_connect(cursor)
        return '', 204
    
    except Error as e:
        cursor.execute('rollback')
        engine.close_connect(cursor)
        return "ERROR Database :" + str(e), 500
    except Exception as e:
        cursor.execute('rollback')
        engine.close_connect(cursor)
        return "Error: " + str(e),500

def DeleteAllQuestions():
    cursor = engine.db_cursor()
    cursor.execute('begin')
    try:
        #delete all answers because they have a foreign key
        cursor.execute("DELETE FROM possibleAnswers")
        #delete all questions
        cursor.execute("DELETE FROM questions")
        cursor.execute('commit')
        engine.close_connect(cursor)
        return '', 204
    except Error as e:
        cursor.execute('roolback')
        engine.close_connect(cursor)
        return "ERROR database: " + str(e), 500
    except Exception as e:
        cursor.execute('rollback')
        engine.close_connect(cursor)
        return "Error: " + str(e),500

def UpdateQuestion(request,idQuestion:int):
    cursor = engine.db_cursor()
    cursor.execute('begin')
    try :
        #verify if the id exits
        if not checkID(cursor,idQuestion):
            cursor.execute('rollback')
            engine.close_connect(cursor)
            return 'Not Found: check id', 404
        
        qt = Question.parseRequestToQuestion(request,idQuestion)
        #verify if the position is correct        
        if not checkPosition(cursor,qt.position):
            cursor.execute('rollback')
            engine.close_connect(cursor)
            return "Bad request: the position is too high",400  
        
        #verify if the position change because we need to increment or decrement some positions in db
        currentPosition = getCurrentPosition(cursor,idQuestion)        
        if qt.position != int(currentPosition) :
            changeCurrentPosition(cursor,newPosition=qt.position,currentPosition=currentPosition)
        
        #update the question in the database 
        updateQuestion(cursor,qt)
        
        #update answers
        cursor.execute("DELETE FROM possibleAnswers WHERE idQuestion = " + str(idQuestion) + ";")
        addAnswers(cursor,qt)
                
        cursor.execute('commit')
        engine.close_connect(cursor)
        return '',204
    
    except Error as e:
        cursor.execute('rollback')
        engine.close_connect(cursor)
        return "Error database: " + str(e),500
    except Exception as e:
        cursor.execute('rollback')
        engine.close_connect(cursor)
        return "Error: " + str(e),500
    
def DeleteAllParticipations():
    cursor = engine.db_cursor()
    cursor.execute('begin')
    try:
        #delete all scores
        cursor.execute("DELETE FROM scores")
        cursor.execute('commit')
        engine.close_connect(cursor)
        return '',204
    except Error as e:
        cursor.execute('rollback')
        engine.close_connect(cursor)
        return "Error database: " + str(e),500    
    except Exception as e:
        cursor.execute('rollback')
        engine.close_connect(cursor)
        return "Error: " + str(e),500
    
    
def GetQuestionById(questionId:int):
    cursor = engine.db_cursor()
    try:
        if not checkID(cursor,questionId):
            engine.close_connect(cursor)
            return "Not Found", 404
        #translate a question une the base in an object Question
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
        
        #find id of the question
        sql_query = "SELECT id FROM questions " +\
            "WHERE position = " + str(position)
        cursor.execute(sql_query)
        questionId = cursor.fetchone()[0] 
        
        #translate a question of the base in an object Question
        qt = Question.parseDbToQuestion(cursor,questionId)
        engine.close_connect(cursor)
        return qt.parseQuestionToJson(),200
    except Error as e:
        engine.close_connect(cursor)
        return "Error database: " + str(e),500    
    except Exception as e:
        engine.close_connect(cursor)
        return "Error: " + str(e),500    


def getGoodAnswers(cursor:Cursor,answers:list):
    sql_query = "SELECT id,position FROM questions ORDER BY position"
    listQuestionOrderer = cursor.execute(sql_query).fetchall()
    if len(listQuestionOrderer) != len(answers):
        raise Exception('The number of answers entered by the player is different from the total number of questions')
    goodAnswers = []
    score = 0
    for id,position in listQuestionOrderer:
        index = position - 1
        sql_query = "SELECT id,isCorrect FROM possibleAnswers WHERE idQuestion = " + str(id) + " ORDER by id"
        answersFetch = cursor.execute(sql_query).fetchall()
        for i in range(len(answersFetch)):
            if answersFetch[i][1] == 'True' :
                if i == answers[index] - 1:
                    score += 1
                    goodAnswers.append({"correctAnswerPosition":i+1, "isCorrect": True})
                else :
                    goodAnswers.append({"correctAnswerPosition":i+1, "isCorrect": False})
                
                break
    return goodAnswers,score   
        

def PostParticipation(request):
    cursor = engine.db_cursor()
    cursor.execute('begin')
    try:
        answers = request.get_json()['answers']
        playerName = request.get_json()['playerName']
        
        #construc a summary of good answers and calculate the score
        try:
            summary,score = getGoodAnswers(cursor,answers)
        except Error as e : 
            raise e
        except Exception as e:
            cursor.execute('rollback')
            engine.close_connect(cursor)
            return "Bad request: " + str(e),400 
        
        # post the scrore in the base
        date_time = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        sql_query = "INSERT INTO scores (playerName,score,date) VALUES ('" + playerName + "'," + str(score) + "," + "'" + date_time + "')"
        cursor.execute(sql_query)
        
        cursor.execute('commit')
        engine.close_connect(cursor)
        
        json = {"playerName": playerName,"score":score, "answersSummaries": summary}
        return json,200
    except Error as e:
        cursor.execute('rollback')
        engine.close_connect(cursor)
        return "Error database: " + str(e),500    
    except Exception as e:
        cursor.execute('rollback')
        engine.close_connect(cursor)
        return "Error: " + str(e),500   