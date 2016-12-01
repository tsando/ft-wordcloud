from flask import render_template
from app import app

from app.db import connect_db


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Tanya'}
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        SELECT
            *
        FROM
            ftdb
    """)
    rows = cur.fetchall()
    return render_template('index.html', title='Home', user=user, rows=rows)

app.run(debug=True)
