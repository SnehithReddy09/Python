'''
PROGRAM DESCRIPITON:
	Creating a json file and readin from it.
    Checking the URL and Retrieving data from URL and print details of breed. 
'''

# PROGRAMMED BY: PULI SNEHITH REDDY
# MAIL ID : snehithreddyp@gmail.com
# DATE    : 20-09-2021
# VERSION : 3.7.9
# CAVEATS : None
# LICENSE : None



import requests
import json

class json1:
    def create_json(self, data):
        with open("welcome.json", "w") as file:
            return json.dump(data, file)
    
    def read_json(self, file):
        with open(file)as file:
            return json.load(file)

    def url_check(self,url):
        try:
            url=requests.get(url)
            return True
        except:
            return False
    def read_url(self,url):
        url = requests.get(url)
        return url.json()

url="https://api.thedogapi.com/v1/breeds"

a=json1()
#checking url is present or not. Enters if True.
if a.url_check(url):
    #reading data from URL and json file is returned
    x=a.read_url(url)
    #iterating the json file
    for i in x:
        if 'breed_group' in i:
            print(i['breed_group'])
            print(i['image'])
            print()
        else:
            print("No breed group present")
            print(i['image'])
            print()