from model import engine
from sqlite3 import Error,Cursor

def rebuil_DB():
    sql_query = """PRAGMA writable_schema"""
    sql_query_ = """delete from sqlite_master where type in ('table', 'index', 'trigger');"""
    cursor = engine.db_cursor()
    cursor.execute("begin")
    try:
        cursor.execute(sql_query + " = 1")
        cursor.execute(sql_query_)
        cursor.execute(sql_query + " = 0")
        cursor.execute("commit")
        cursor.close()
        engine.__init__()
    except Error as e:
        print(e)
        cursor.execute("rollback")
        return "Error in database : " + str(e), 500
    return '',204
    
   
