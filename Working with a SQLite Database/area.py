import sqlite3 as sq
import pandas as pd

conn=sq.connect('factbook.db')

fact1=pd.read_sql_query("SELECT SUM(area_land) as s FROM FACTS WHERE area_land!='';",conn)
fact2=pd.read_sql_query("SELECT SUM(area_water) as s FROM FACTS WHERE area_land!='';",conn)

area_land=fact1['s']
area_water=fact2['s']

result=area_land/float(area_water)

print(result)