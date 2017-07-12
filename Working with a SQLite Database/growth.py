import sqlite3 as sq
import pandas as pd
import math

conn=sq.connect("factbook.db")

fact = pd.read_sql_query("select * from facts;",conn)

print(fact.shape)
fact=fact[fact['area_land']!=0]
print(fact.shape)

def pop_growth(pop,growth):

    result=float(pop)*(math.e**((growth/100)*35))
    return result

fact['population_2050']=fact[['population','population_growth']].apply(lambda x:pop_growth(*x),axis=1)
fact.sort_values(by='population_2050',ascending=False,inplace=True)

print(fact['name'].head(10))

conn.close()