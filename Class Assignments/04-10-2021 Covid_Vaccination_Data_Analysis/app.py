'''
PROGRAM DESCRIPITON:
	Find out the total vaccinations administered in India and USA from the given CSV file.
    Also find out what is the % rate of US as compared to INdia in vaccine adminstration?
    Consider the total vbaccines adminstred 
'''

# PROGRAMMED BY: PULI SNEHITH REDDY
# MAIL ID : snehithreddyp@gmail.com
# DATE    : 04-10-2021
# VERSION python: 3.7.9
# CAVEATS : None
# LICENSE : None

import pandas as pd 
import numpy as np 
from statistics import mode 
from collections import Counter 

# data extraction from the given csv file.
df = pd.read_csv('country_vaccinations.csv')

#list of all countries present in the file
country_list = df['country'].unique()
#list of all unique vaccines given in countries in the file.
vaccine_ava = df['vaccines'].unique()

#Finding the most frequently used vaccine per country.
vaccine_used = []
for i in country_list:
    vaccine_used.append(df[df['country']==i]['vaccines'].mode(0))

vaccine_used = pd.Series(vaccine_used)

#Storing the each vaccine count used in the entire countries.
vaccine_mode = []
for i in range(0, 102):
    vaccine_mode.append(vaccine_used[i][0])
words_to_count = (word for word in vaccine_mode if word[:1].isupper())
c = Counter(words_to_count)
count = []

print("Most widely used vaccine # ", mode(vaccine_mode))
print("vaccines used in India # ", df[df['country']=='India']['vaccines'].mode(0)[0])


#calculating the total count of vaccinations done in each country
country_vaccinated_number = []
for i in country_list:
    country_vaccinated_number.append([i,df[df['country']==i]['people_vaccinated'].sum(0)])
#print(country_vaccinated_number)

#From total vaccinations done in each country finding out the unvaccinated country i.e. where sum=0
country_unvaccinated=[]
for i in country_vaccinated_number:
    if i[1]==0:
        country_unvaccinated.append(i[0])
#print(country_unvaccinated)

#Getting information of total vaccinations done in a country month wise
def country_vaccinated_month(country_name):
    date_vaccinated=pd.Series(df[df['country']==country_name]['date'])
    people_vaccinated=pd.Series(df[df['country']==country_name]['people_vaccinated'])
    country_vaccination=[]
    for i,j in zip(date_vaccinated,people_vaccinated):
        dates=i.split('/')
        country_vaccination.append([[dates[0],dates[2]],j])
    country_vaccination_per_month={}
    for i in country_vaccination:
        if str(i[0][0])+','+str(i[0][1]) in country_vaccination_per_month:
            country_vaccination_per_month[str(i[0][0])+','+str(i[0][1])]+=i[1]
        else:
            country_vaccination_per_month[str(i[0][0])+','+str(i[0][1])]=i[1]
    
    return country_vaccination_per_month

#Analysis of vaccination done between 2 countries.
def vaccination_administration_between_countries(country1,country2):
    country1_vaccination_per_month=country_vaccinated_month(country1)
    country2_vaccination_per_month=country_vaccinated_month(country2)
    print(country1+" ",country1_vaccination_per_month)
    print(country2+" ",country2_vaccination_per_month)
    month={'1':'January','2':'Febrauary','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
    for i in country1_vaccination_per_month.copy():
        if i not in country2_vaccination_per_month:
            print(country1+" % of vaccinated more than "+country2+" in "+month[i.split(',')[0]]+" year "+i.split(',')[1]+" is 100")
            country1_vaccination_per_month.pop(i)
    for i in country2_vaccination_per_month.copy():
        if i not in country1_vaccination_per_month:
            print(country2+" % of vaccinated more than "+country1+" in "+month[i.split(',')[0]]+" year "+i.split(',')[1]+" is 100")
            country2_vaccination_per_month.pop(i)
    for i,j in zip(country1_vaccination_per_month,country2_vaccination_per_month):
        x=country2_vaccination_per_month[j]
        y=country1_vaccination_per_month[i]
        if x>y:
            if x==0:
                percentage_variying=100
            else:
                percentage_variying=((x-y)*100)/x
            print(country2+" % of vaccinated more than "+country1+" in "+month[i.split(',')[0]]+" year "+i.split(',')[1]+" is ",percentage_variying)

        else:
            if y==0:
                percentage_variying=100
            else:
                percentage_variying=((y-x)*100)/y
            print(country1+" % of vaccinated more than "+country2+" in "+month[i.split(',')[0]]+" year "+i.split(',')[1]+" is ",percentage_variying)


vaccination_administration_between_countries('India','United States')

''' OUTPUT 

Most widely used vaccine #  Pfizer/BioNTech
vaccines used in India #  Covaxin, Oxford/AstraZeneca

India  {'1,2021': 28323206.0, '2,2021': 153284083.0}
United States  {'12,2020': 9044666.0, '1,2021': 318860802.0, '2,2021': 736674472.0}

United States % of vaccinated more than India in December year 2020 is 100
United States % of vaccinated more than India in January year 2021 is  91.11737603921601
United States % of vaccinated more than India in Febrauary year 2021 is  79.19242639373012

'''
