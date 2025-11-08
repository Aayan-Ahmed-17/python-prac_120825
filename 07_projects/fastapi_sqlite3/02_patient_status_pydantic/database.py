import sqlite3

"""1) Database Connection & Table Setup"""


def get_db():
    conn = sqlite3.connect("patient.db")
    conn.row_factory = sqlite3.Row
    return conn


# Creation of Table
conn = get_db()
conn.execute(
    """
             CREATE TABLE IF NOT EXISTS patients (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL,
             city TEXT,
             age INTEGER,
             gender TEXT,
             ismarried INTEGER NOT NULL DEFAULT 0,
             height REAL NOT NULL,
             weight REAL NOT NUL)"""
)
conn.commit()
conn.close()

"""2) Add data into the table"""


def add_patient_data(patient):
    conn = get_db()
    conn.execute(
        "INSERT INTO patients (name, city, age, gender, ismarried, height, weight) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (
            patient.name,
            patient.city,
            patient.age,
            patient.gender,
            1 if patient.ismarried else 0,
            patient.height,
            patient.weight,
        ),
    )
    conn.commit()
    conn.close()

    return{"success": True, "patient_id": patient.id}
