'''
PROGRAM DESCRIPITON: 
	Find the factorial of numbers in given range using numpy and store them in a JSON file.
    Also find the karperkar numbers in given range and store them in same JSON file.
'''

# PROGRAMMED BY: PULI SNEHITH REDDY
# MAIL ID : snehithreddyp@gmail.com
# DATE    : 28-09-2021
# VERSION : 3.7.9
# CAVEATS : None
# LICENSE : None

import requests
import json 
import numpy as np
import math

#Creation of JSON file by opening file and writing data into it using dump().
def create_json(data,file_name):
    with open(file_name,"w") as f:
        return json.dump(data,f)


list_1=np.arange(0,200)
list1={}
for i in range(len(list_1)):
    #finding factorial of number using np.math.factorial() and appending them in dictionary.
    list1[i]=np.math.factorial(list_1[i])


list_2=np.arange(1,10000)
list_3={}
for i in list_2:
    j=str(i*i)
    #Iterating the number for splitting it in two parts.
    for k in range(1,len(j)):
        x=int(j[:k])+int(j[k:])
        #Checking whether the same number is obtained when both added
        if x==i and x%10!=0:
            list_3[i]="Karperkar Number"
            break 
res={"Factorial":list1,"Karperkar Number":list_3}
#Sending the file to create a JSON file.
create_json(res,"Numbers.json")


