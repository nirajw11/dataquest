from dateutil.parser import parse

import read
stories = read.load_data()

def get_submission_hour(stime):
    dt=parse(stime)
    return dt.hour

def get_submission_month(stime):
    dt=parse(stime)
    return dt.month

stories['submission_hour']=stories['submission_time'].apply(get_submission_hour)
stories['submission_month']=stories['submission_time'].apply(get_submission_month)
print(stories['submission_hour'].value_counts().head(10))
print(stories['submission_month'].value_counts().head(10))