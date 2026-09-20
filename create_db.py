import sqlite3

def init_db():
    # Database connection (agar file nahi hai toh automatic ban jayegi)
    conn = sqlite3.connect("prediction.db")
    cursor = conn.cursor()

    # Table creation
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            study_hours REAL,
            attendance REAL,
            previous_marks REAL,
            assignment_marks REAL,
            internal_marks REAL,
            practice_test REAL,
            sleep_hours REAL,
            predicted_marks REAL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()
    print("prediction.db successfully created!")

if __name__ == "__main__":
    init_db()