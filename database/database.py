import sqlite3

conn = sqlite3.connect("crop_disease.db", check_same_thread=False)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS prediction_history(

id INTEGER PRIMARY KEY AUTOINCREMENT,

disease TEXT,

confidence REAL,

prediction_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP

)
""")

conn.commit()


def save_prediction(disease, confidence):

    cursor.execute("""
    INSERT INTO prediction_history(disease, confidence)
    VALUES(?,?)
    """, (disease, confidence))

    conn.commit()


def get_predictions():

    cursor.execute("""
    SELECT * FROM prediction_history
    ORDER BY id DESC
    """)

    return cursor.fetchall()
def clear_predictions():
    conn = sqlite3.connect("crop_disease.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM prediction_history")

    conn.commit()
    conn.close()