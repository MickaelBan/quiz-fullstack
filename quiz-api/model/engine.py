import sqlite3
from sqlite3 import Error,Connection,Cursor


def db_connect():
    conn = None
    try:
        conn = sqlite3.connect('./database.db')
        conn.isolation_level = None
    except Error as e:
        print(e)
    
    return conn

def db_cursor():
    return db_connect().cursor()
    
def close_connect(conn:Connection):
    if conn is not None:
        conn.close() 
            
def close_connect(cursor:Cursor):
    if cursor is not None:
        cursor.close()
     
def create_table(conn:Connection):
    cursor = conn.cursor()
    sql_query = """CREATE TABLE IF NOT EXISTS questions (
            id	INTEGER PRIMARY KEY NOT NULL UNIQUE,
            position	INTEGER NULL,
            title	TEXT NOT NULL,
            text	TEXT NOT NULL,
            image	TEXT 
        );"""        
    cursor.execute(sql_query)
    sql_query = """CREATE TABLE IF NOT EXISTS possibleAnswers (
            id	INTEGER PRIMARY KEY,
            text	TEXT,
            isCorrect	TEXT,
            idQuestion INTEGER,
            FOREIGN KEY(idQuestion) REFERENCES questions(id)
        );"""
    cursor.execute(sql_query)
    sql_query = """CREATE TABLE IF NOT EXISTS scores (
            id	INTEGER PRIMARY KEY,
            playerName	TEXT,
            score INTEGER,
            date DATE
        );"""
    cursor.execute(sql_query)
    close_connect(conn)


def __init__():
    create_table(db_connect())
