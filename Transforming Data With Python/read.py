import pandas as pd
def load_data():
    stories=pd.read_csv("hn_stories.csv")
    stories.columns=['submission_time','upvotes','url','headline']
    return stories
if __name__ == "__main__":
    print("Welcome to a Python script")
    stories=load_data()
    print(stories.head())
          
          
          
          