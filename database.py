"""
     Database connection
 """
from fastapi import FastAPI , HTTPException
import mysql.connector
from mysql.connector import Error

app = FastAPI()

def get_connection():
    #setup info
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="fastapitest"
    )

@app.get("/users")
def get_users() : 
    try:
        conn= get_connection() # connect to the database
        cursor = conn.cursor(dictionary=True) # create a cursor object to execute queries
        cursor.execute("SELECT * FROM users");# execute the query
        rows = cursor.fetchall() # fetch all rows from the result set
        cursor.close() # close the cursor
        conn.close() # close the connection
        return rows
    except Error as e : 
        #return error message
        raise HTTPException(status_code=500, detail=str(e))
        
