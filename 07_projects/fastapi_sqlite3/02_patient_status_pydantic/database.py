import sqlite3

"""1) Database Connection & Table Setup"""
conn = sqlite3.connect("patient.db")
conn.row_factory = sqlite3.Row

# Creation of Table
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
