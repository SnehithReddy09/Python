 
'''
PROGRAM DESCRIPITON: 
	Retrive the data from URL and converting it into DataFrame Object and storing it in .csv file.
'''

# PROGRAMMED BY: PULI SNEHITH REDDY
# MAIL ID : snehithreddyp@gmail.com
# DATE    : 01-10-2021
# VERSION : 3.7.9
# CAVEATS : None
# LICENSE : None


import json
import requests 
import pandas as pd
class One:
    #checking whether url exists or not.
    def url_check(self,url):
        try:
            url=requests.get(url)
	    #return True if URL exits
            return True
        except:
	    #return False if URL not exits
            return False

    #Reading from url and returning data in json format.
    def read_url(self,url):
        url = requests.get(url)
        return url.json()

url="https://api.thedogapi.com/v1/breeds"
a=One()
if a.url_check(url):
    
    x=a.read_url(url)
    name=[]
    bred_for=[]
    country=[]
    image=[]
    for i in x:
        if "name" in i:
            name.append(i["name"])
        else:
            name.append("-")
        if "bred_for" in i:
            bred_for.append(i["bred_for"])
        else:
            bred_for.append("-")
        if "country" in i:  
            country.append(i["Country"])
        else:
            country.append("-")
        if "image" in i:
            image.append(i["image"]["url"])
        else:
            image.append("-")
    y=pd.DataFrame([name,bred_for,country,image],index=["name","bred_for","country","image"])
    y.to_csv('panda.csv')
    df = pd.read_csv('panda.csv', index_col=0)
    print(df)
