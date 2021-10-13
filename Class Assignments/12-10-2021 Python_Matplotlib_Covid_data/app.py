
import matplotlib.pyplot as plt 
from matplotlib import markers 
import pandas as pd 
import numpy as np 
from statistics import mode 
from collections import Counter

# data extraction from the given csv file.
df = pd.read_csv('country_vaccinations.csv')

#list of all countries present in the file
country_list = df['country'].unique()
#list of all unique vaccines given in countries in the file.
vaccine_available = df['vaccines'].unique()

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
names_vaccine=[]
for i in range(0,19):
    count.append(c.most_common()[i][1])
    names_vaccine.append(c.most_common()[i][0])


print("Most widely used vaccine # ", mode(vaccine_mode))
print("vaccines used in India # ", df[df['country']=='India']['vaccines'].mode(0)[0])

fig=plt.figure()
plt.title("Vaccination Details")
axs=fig.add_axes([0.1,0.00001,0.7,1])
#Plotting pie chart for vaccinations count used by various countries
axs.pie(count,labels=names_vaccine,autopct='%1.1f%%')
#plt.savefig("Pie_chart_Vaccinations_count_world.png",format='png')
plt.show()
df1=pd.DataFrame()
dates= [pd.to_datetime(i) for i in df[df['country']=='India']['date']]
vaccinations=[int(i) for i in df[df['country']=='India']['total_vaccinations']]

#Plotting graph on data total vaccinations per day in India
plt.title("Vaccinations per day in India")
plt.xlabel("Date")
plt.ylabel("Total_vaccinations")
plt.ticklabel_format(style='plain')
plt.plot(dates,vaccinations)
plt.savefig("Graph_total_Vaccinations_per_date.png",format='png')
plt.show()

#........................................................................................................................

#                            USA and INDIA Graph on MONTH / STANDARAD DEVIATION

#Function which groups data based on country, date and then calculates standard deviation and returns it.
def month_wise(country):
    country_data=pd.DataFrame(df[df['country']==country])
    lst=[]
    country_data['date']= pd.to_datetime(country_data['date'])
    month_wise_lst=dict(country_data.groupby(country_data['date'].dt.strftime('%B'))['total_vaccinations'].std(0))
    return month_wise_lst

#Getting deatils of std deviation of total_vaccinations in India month wise
India_month_wise=month_wise("India")
plt.ticklabel_format(style='plain')
#Plotting the details of std deviations where keys are months and values are std deviations.
plt.plot(list(India_month_wise.keys()),list(India_month_wise.values()),marker='o',label="India")
#Getting deatils of std deviation of total_vaccinations in USA month wise
USA_month_wise=month_wise("United States")
plt.title("United States & India Std. Deviations over month of January and Febraury")
USA_month_wise.pop("December")
plt.plot(list(USA_month_wise.keys()),list(USA_month_wise.values()),marker='o',label="United States")
#combining the both plots together
plt.legend()
plt.savefig("USA_INIDA_std-deviation_month_wise.png",format="png",dpi=100)
plt.show()


#........................................................................................................................

#                          Plotting of line graph for Fully and Partial Vaccination in India and USA. 


names=["India","United States"]

#Function which plots the graphs 
def vaccination_graph(names,catogery):
    vaccination_1_date=[pd.to_datetime(i) for i in df[df['country']==names[0]]['date']]
    vaccination_2_date=[pd.to_datetime(i) for i in df[df['country']==names[1]]['date']]
    vaccination1_done_catogery=df[df['country']==names[0]][catogery]
    vaccination2_done_catogery=df[df['country']==names[1]][catogery]
    plt.title("Graph of "+catogery+" in India vs USA")
    plt.xlabel("Date")
    plt.ylabel(catogery)
    plt.ticklabel_format(style='plain')
    plt.plot(vaccination_1_date,vaccination1_done_catogery,label=names[0])
    plt.plot(vaccination_2_date,vaccination2_done_catogery,label=names[1])
    plt.legend()
    plt.savefig("Graph_of_"+catogery+"_in_USA_INDIA.png",format='png',dpi=100)
    plt.show()

#Plotting line graph for fully vaccinated people in India vs USA
vaccination_graph(names,'total_vaccinations')
#Plotting pie chart for partially vaccinated people in India vs USA
vaccination_graph(names,'people_vaccinated')



#........................................................................................................................

#                          Plotting of PIE chart for Fully and Partial Vaccination in India and USA. 


#Functions which plots the pie chart based on the country names and given catogery.
def vaccination_details(names,catogery):
    #Finding sum of all values on a catogery on country 1 from names.
    vaccinations_1=df[df['country']==names[0]][catogery].sum(0)
    #Finding sum of all values on a catogery on country 2 from names.
    vaccinations_2=df[df['country']==names[1]][catogery].sum(0)
    #Finding the percentages
    x=(vaccinations_1/(vaccinations_1+vaccinations_2))*100
    y=(vaccinations_2/(vaccinations_1+vaccinations_2))*100
    percentages_fully_vaccinated=[x,y]
    fig=plt.figure()
    plt.title(catogery)
    axs=fig.add_axes([0.2,0.001,0.7,1])
    #plotting the pie chart
    axs.pie(percentages_fully_vaccinated,labels=names,autopct='%1.1f%%')
    plt.savefig("PieChart"+catogery+".png",format="png",dpi=100)
    plt.show()
    
#Plotting pie chart for fully vaccinated people in India vs USA
vaccination_details(names,"people_fully_vaccinated")
#Plotting pie chart for partial vaccination in India vs USA.
vaccination_details(names,"people_vaccinated")
