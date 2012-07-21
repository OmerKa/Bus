import sqlite3

conn = sqlite3.connect('./DB/tranz.sqlite')
conn.text_factory = str

def Query(sql):
    c = conn.cursor()
    c.execute(sql)
    l = c.fetchall()
    c.close()
    return l

def First(l):
     return [r[0] for r in l]

def get_trips_ids(col,l):
    sql = 'select distinct id from trips where {0} in {1}'.format(col,tuple(l))
    return First(Query(sql))
