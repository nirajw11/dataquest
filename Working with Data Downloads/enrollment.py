import pandas as pd

data=pd.read_csv("data/CRDC2013_14.csv",encoding="Latin-1")

data['total_enrollment']=data['TOT_ENR_M']+data['TOT_ENR_F']

s=0
all_enrollment=sum(data['total_enrollment'])
for col in data.columns:
    if col.startswith('SCH_ENR_') & (len(col)==12):
       print(col," : ",round(float(sum(data[col])/all_enrollment),2))

