import sqlite3 as sqlite

def connect_db(filename='app/db.sqlite'):
    conn = sqlite.connect(database=filename)
    return conn
