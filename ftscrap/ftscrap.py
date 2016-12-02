# Webscraping
import requests
from lxml import html

# Database
import sqlite3 as sqlite
from datetime import datetime

# Wordcloud
from wordcloud import WordCloud
import matplotlib.pyplot as plt


# --------- Webscraping ---------

# Webscrap the FT commodities headlines
page = requests.get("https://www.ft.com/markets/commodities")
tree = html.fromstring(page.content)
headlines = tree.xpath('//a[@data-trackable="main-link"]/text()')

# join the headlines into single string
headlines_str = ' ,,, '.join(headlines)


# --------- Database ---------

# Feed latest entry to 'historical' database
con = sqlite.connect(database='ftdb.sqlite')
cur = con.cursor()

# Check table exists
cur.execute("""
        CREATE TABLE IF NOT EXISTS
        ftdb
        (
        id INTEGER PRIMARY KEY,
        datetime DATETIME,
        corpus TEXT
        )
    """)

# Timestamp
now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Insert values. NULL automatically fills in primary key
cur.execute("INSERT INTO ftdb VALUES (NULL, ?, ?)", (now, headlines_str))
con.commit()

# In case need to delete rows from table, e.g. delete row with id=2
# cur.execute("DELETE FROM ftdb WHERE id=?", (2,))
# con.commit()
# con.close()

# Check contents from db
cur.execute("SELECT * FROM ftdb")
ftdb_all = cur.fetchall()
con.close()

# --------- Wordcloud ---------

# Create simple wordcloud out of all the historical headlines in FT database

# Get the corpuses and join them to single string
# see http://stackoverflow.com/questions/6547658/how-to-remove-u-from-sqlite3-cursor-fetchall-in-python
con = sqlite.connect(database='ftdb.sqlite')
# con.row_factory = sqlite.Row  # dictionary cursor - see http://zetcode.com/db/sqlitepythontutorial/
con.text_factory = str
cur = con.cursor()
cur.execute("SELECT corpus FROM ftdb")
ftdb_corpus = cur.fetchall()
ftdb_corpus = ' ::: '.join(i[0] for i in ftdb_corpus)  # must do this as fetchall returns tuple

# Create simple wordcloud
wc = WordCloud().generate(headlines_str)
plt.imshow(wc)
plt.show()

# --------- D3 ---------

# Convert to JSON - main idea:
# from flask import jsonify
# json = jsonify(ftdb_all)
