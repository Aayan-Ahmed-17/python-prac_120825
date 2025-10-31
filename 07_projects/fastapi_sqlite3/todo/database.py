import sqlite3

"Going to explore CRUD operations of SQLITE 3 with the help of todo app + using fastapi to test apis and will serve us as a frontend"

"""Initialization | setup sqlite3 db connection"""
def get_db():
    conn = sqlite3.connect("todo.db")     #will create todo.db file if not exist | else will be ignored
    conn.row_factory = sqlite3.Row          #allows us to access our data in a dict form
    print(conn)
    return conn

"""establishing db connection"""
conn = get_db()
conn.execute("CREATE TABLE IF NOT EXISTS todo ( id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT NOT NULL)")  #creates table named todo

conn.commit()
conn.close()

"""Create Todo list items in DB"""
def create_todo_items(task : str):
    conn = get_db()
    conn.execute("INSERT INTO todo (task) VALUES (?)", (task,))
    conn.commit()
    conn.close()

    return True

"""get all items from todo table in DB"""
def get_todo_item():
    conn = get_db()
    todos = conn.execute("SELECT * FROM todo").fetchall()
    conn.close()
    return {
        "message": "All Todo Items Has Been Fetched",
        "Items=>": todos
    }

