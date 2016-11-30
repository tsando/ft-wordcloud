import sqlite3 as sqlite


def connect_db(filename='app/db.sqlite'):
    conn = sqlite.connect(database=filename)
    return conn


def init_tables(conn):
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS
        ftdb
        (
        id INTEGER PRIMARY KEY,
        datetime DATETIME,
        text TEXT
        )
    """)
    conn.commit()
    pass
