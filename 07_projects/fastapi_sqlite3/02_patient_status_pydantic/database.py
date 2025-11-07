import sqlite3
from pandantic_code import Patient

"""1) Database Connection & Table Setup"""
def get_db():
    conn = sqlite3.connect("patient.db")
    conn.row_factory = sqlite3.Row
    return conn

# Creation of Table
conn = get_db()
conn.execute(
    """
             CREATE TABLE IF NOT EXIST patients (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL
             city TEXT
             age
             gender
             ismarried INTEGER NOT NULL DEFAULT 0
             height REAL NOT NULL
             weight REAL NOT NULL
             )"""
)
conn.commit()
conn.close()

"""2) Add data into the table"""
def add_patient_data(infos: Patient):
    conn = get_db()
    conn.execute("INSERT INTO patients (infos) VALUES (?)", (infos,))
    conn.commit()
    conn.close()
    return True