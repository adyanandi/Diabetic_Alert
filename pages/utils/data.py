# This file provides the implementation for creating and managing the SQLite database 
#  It includes functions for creating the database,  clearing the database, fetching user data, and storing user data.


from pages import os,sqlite3,st

def create_connection(db_path):
    db_path = os.path.join('src', 'database', db_path)
    abs_path = os.path.abspath(db_path)
    db_dir = os.path.dirname(abs_path)
    if not os.path.exists(db_dir):
        os.makedirs(db_dir)

    return sqlite3.connect(abs_path)

def create_db():
    conn = create_connection('user_data.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS diabetesData (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        contact_number TEXT NOT NULL,
        gender TEXT NOT NULL,
        pregnancies INTEGER,
        glucose INTEGER,
        blood_pressure INTEGER, 
        skin_thickness INTEGER,                     
        insulin INTEGER,
        bmi REAL,           
        age INTEGER,
        feedback TEXT
    )
    ''')
    conn.commit()
    conn.close()


def clear_database_user():
    
    conn = create_connection('user_data.db') 
    cursor = conn.cursor()

    
    cursor.execute("DELETE FROM diabetesData")  


    conn.commit()
    conn.close()



def fetch_user_data():
    try:
        conn = create_connection('user_data.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM diabetesData')
        data = cursor.fetchall()
        conn.close()
        return data
    except Exception as e:
        st.error(f"Error fetching user data: {e}")

def store_user_data(name, contact_number,gender, pregnancies, glucose, blood_pressure, skin_thickness,insulin, bmi,age, feedback):
    try:
        conn = create_connection('user_data.db')
        cursor = conn.cursor()

        
        cursor.execute('''
        INSERT INTO diabetesData (name, contact_number,gender, pregnancies, glucose, blood_pressure, skin_thickness,insulin, bmi,age, feedback)
        VALUES (?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (name, contact_number,gender, pregnancies, glucose,  blood_pressure, skin_thickness,insulin, bmi,age, feedback))

        conn.commit()
        conn.close()
    except Exception as e:
        st.error(f"Error storing user data: {e}")        