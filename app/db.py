import sqlite3 as sqlite


def connect_db(filename='app/db.sqlite'):
    conn = sqlite.connect(database=filename)
    init_tables(conn)
    conn.row_factory = dict_factory  # allows to call sql rows by their field name instead of by index
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


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
