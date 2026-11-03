
import sqlite3

def create_database():
    conn = sqlite3.connect("quiz.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            score INTEGER
        )
    """)

    conn.commit()
    conn.close()


def save_score(name, score):
    conn = sqlite3.connect("quiz.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO scores (name, score) VALUES (?, ?)",
        (name, score)
    )

    conn.commit()
    conn.close()
