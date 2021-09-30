import requests
import json 
import numpy as np
import math
def create_json(data,file_name):
    with open(file_name,"w") as f:
        return json.dump(data,f)


list_1=list(range(10,200))
list1={}
for i in range(len(list_1)):
    list1[i]=np.math.factorial(list_1[i])


list_2=list(range(1,10000))
list_3={}
for i in list_2:
    j=str(i*i) 
    for k in range(1,len(j)):
        x=int(j[:k])+int(j[k:])
        if x==i:
            list_3[i]="Karperkar Number"
            break 
res={"Factorial":list1,"Karperkar Number":list_3}

create_json(res,"Numbers.json")


