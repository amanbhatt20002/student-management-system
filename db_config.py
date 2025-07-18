import mysql.connector

def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="7856root",  # ⛔ replace with your actual MySQL password
        database="student_db"
    )
