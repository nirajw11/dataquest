import sqlite3 as sq

conn=sq.connect("factbook.db")
query="select name from facts order by population asc limit 10;"
results = conn.execute(query).fetchall()
print(results)
conn.close()