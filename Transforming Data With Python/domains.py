import read

stories = read.load_data()

domains=stories['url'].value_counts()

#for name,row in domains.items():
#    print("{0}: {1}".format(name,row))
          
def remove_subdomains(domain):
    split_list=[]
    split_list=str(domain).split('.')
    length=len(split_list)
    dom=split_list[length-2]+"."+split_list[length-1]
    return dom

stories['url_mod']=stories['url'].apply(remove_subdomains)

domains=stories['url_mod'].value_counts()

for name,row in domains.items():
    print("{0}: {1}".format(name,row))

