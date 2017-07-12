import read
from collections import Counter

stories=read.load_data()

combined=''
for line in stories['headline']:
    combined=combined+" "+str(line).lower()
    
combined_list=combined.split()

cnt =Counter()

for word in combined_list:
    cnt[word]+=1
    
print(cnt.most_common(100))