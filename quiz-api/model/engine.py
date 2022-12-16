import sqlite3
from sqlite3 import Error,Connection



def __init__():
    create_table(db_connect())


def db_connect():
    conn = None
    try:
        conn = sqlite3.connect('./database.db')
        conn.isolation_level = None
    except Error as e:
        print(e)
    
    return conn


def close_connect(conn:Connection):
    if conn is not None:
        conn.close()     
    
def create_table(conn:Connection):
    cursor = conn.cursor()    
    sql_query = """CREATE TABLE IF NOT EXISTS questions (
            id	INTEGER PRIMARY KEY,
            position	INTEGER NULL UNIQUE,
            title	TEXT NOT NULL,
            text	TEXT NOT NULL,
            image	TEXT NULL
        );"""        
    cursor.execute(sql_query)
    conn.commit()
    sql_query = """CREATE TABLE IF NOT EXISTS possibleAnswers (
            id	INTEGER PRIMARY KEY,
            text	TEXT,
            isCorrect	TEXT,
            idQuestion INTEGER,
            FOREIGN KEY(idQuestion) REFERENCES questions(id)
        );"""
    cursor.execute(sql_query)
    close_connect(conn)
