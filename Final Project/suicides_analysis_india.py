
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns


df=pd.read_csv("Suicides in India 2001-2012.csv")
print(df.info())
print(df['Type_code'].unique())
# rename states

df.replace('A & N Islands (Ut)', 'A & N Islands', inplace=True)
df.replace('Chandigarh (Ut)', 'Chandigarh', inplace=True)
df.replace('D & N Haveli (Ut)', 'D & N Haveli', inplace=True)
df.replace('Daman & Diu (Ut)', 'Daman & Diu', inplace=True)
df.replace('Lakshadweep (Ut)', 'Lakshadweep', inplace=True)
df.replace('Delhi (Ut)', 'Delhi', inplace=True)

df.replace('By Other means (please specify)', 'By Other means', inplace=True) 

df = df.drop(df[(df.State == 'Total (Uts)') | (df.State == 'Total (All India)') | 
               (df.State == 'Total (States)')].index)
print(df['Type_code'].unique())
df= df.drop(df[df.Total==0].index)
print(df['Type_code'].unique())
#df= df.drop(df[(df['Age_group'] == '0-100+')].index)
print(df['Type_code'].unique())
print(df['Type_code'].unique())


fig=plt.figure() 
year=df['Year'].unique()
year_count=df.groupby('Year').sum()['Total']
plt.bar(year,year_count)
plt.gcf().set_size_inches(8,8)
plt.xlabel("Year")
plt.ylabel("Total number of suicides")
plt.show()

data_per_state = df.groupby('State').sum()['Total'].reset_index().sort_values(by='Total',ascending=False)

print(data_per_state) 
states=[str(i) for i in data_per_state['State']]
state_count=[i for i in data_per_state['Total']]
plt.bar(states,state_count)
plt.gcf().set_size_inches(8,8)
plt.xticks(rotation=90)
plt.show()


def plot_type(type):
    suicide_type_data=df[df['Type_code']==type]
    data=suicide_type_data.groupby('Type').sum()['Total']
    data=data.sort_values(ascending=False)
    plt.bar([i for i in data.keys()],[i for i in data])
    plt.gcf().set_size_inches(10,15)
    plt.xticks(rotation=90)
    plt.savefig("Suicide by "+type+".png",format='png')
    plt.show()

plot_type('Causes')
'''
plot_type('Education_Status')
plot_type('Means_adopted')
plot_type('Professional_Profile')
plot_type('Social_Status')



#...........................AGE.............................. 



plt.figure(figsize=(12,6))
data = df[['Age_group','Total']]
edSort = data.groupby(['Age_group'],as_index=False).sum()
sns.barplot(x='Age_group',y='Total',data=edSort,palette='RdBu')
plt.gcf().set_size_inches(8,8)
plt.show()

#data_per_state =[ i for i in df.groupby('State').sum()['Total'].reset_index().sort_values(by='Total',ascending=False)['State']]

data = df[['Age_group','Total','Year']]
edSort = data.groupby(['Age_group','Year'],as_index=False).sum()
sns.barplot(x='Age_group',y='Total',hue='Year',data=edSort,palette='RdBu')
plt.gcf().set_size_inches(8,8)
plt.show()



data = df[['Gender','Total']]
edSort = data.groupby(['Gender'],as_index=False).sum()
sns.barplot(x='Gender',y='Total',data=edSort,palette='RdBu')
plt.gcf().set_size_inches(8,8)
plt.show()


data = df[['Gender','Total','Year']]
edSort = data.groupby(['Gender','Year'],as_index=False).sum()
sns.barplot(x='Gender',y='Total',hue='Year',data=edSort,palette='RdBu')
plt.gcf().set_size_inches(8,8)
plt.show()

plt.figure(figsize=(12,6))
data = df[['Age_group','Gender','Total']]
edSort = data.groupby(['Age_group','Gender'],as_index=False).sum()
sns.barplot(x='Age_group',y='Total',hue='Gender',data=edSort,palette='RdBu')
plt.gcf().set_size_inches(8,8)
plt.show()


def plot_type(type):
    suicide_type_data=df[df['Type_code']==type]
    suicide_type_data=suicide_type_data[['Type','Gender','Total']]
    data=suicide_type_data.groupby(['Type','Gender'],as_index=False).sum().sort_values(by='Total')
    print(data)
    sns.barplot(x='Type',y='Total',hue='Gender',data=data,palette='RdBu')
    plt.gcf().set_size_inches(8,8)
    plt.xticks(rotation=90)
    plt.show()
    #data=data.sort_values(ascending=False)
    

plot_type('Causes')

#plot_type('Education_Status')
plot_type('Means_adopted')
plot_type('Professional_Profile')
#plot_type('Social_Status')


causes = df[df['Type_code'] == 'Causes']
causes=causes[causes.Type!='Unknown']
causes= causes.sort_values(by='Total',ascending=False)
age_set = causes[['Type','Age_group','Total']]
age_grp = causes['Age_group'].value_counts().index
age_grp = list(age_grp)
for x in age_grp:
    group_set = age_set[age_set['Age_group'] == x ]
    group_set =group_set.groupby('Type').sum().sort_values('Total', ascending = False)
    group_set = group_set.head(5)
    group_set.plot(kind = 'bar', figsize = (15,5), title = 'Age Group '+x+ ' Suicide Reasons',\
                   color=(0.2, 0.4, 0.6, 0.6))
    plt.gcf().set_size_inches(8,8)
    plt.show()


age_set = df[df['Type_code']=='Means_adopted'][['Type','Age_group','Total']]
age_grp = df[df['Type_code']=='Means_adopted']['Age_group'].value_counts().index
age_grp = list(age_grp)
for x in age_grp:
    group_set = age_set[age_set['Age_group'] == x ]
    group_set =group_set.groupby('Type').sum().sort_values('Total', ascending = False)
    group_set = group_set.head(5)
    group_set.plot(kind = 'bar', figsize = (15,5), title = 'Age Group '+x+ ' Suicide Methods',\
                   color=(0.2, 0.4, 0.6, 0.6))
    plt.gcf().set_size_inches(8,8)
    plt.show() 


# Suicide rate every year

year_wise = df.groupby('Year').sum()['Total']
print(year_wise)
year_wise.plot(kind='line', figsize=(6,6), title = 'Suicide rate per year')
plt.xlabel('\nYear')
plt.ylabel('Count\n')
sns.set_style('whitegrid')
plt.gcf().set_size_inches(8,8)
plt.show()


# Education Status by gender
print(df['Type_code'].unique())
plt.figure(figsize=(12,5))
edu_gen = df[df['Type_code'] == 'Education_Status'].groupby(['Type','Gender'],as_index=False).sum().sort_values('Total',ascending=False)
print(df[df['Type_code'] == 'Education_Status'])
sns.barplot(x = 'Type', y ='Total',hue='Gender', data = edu_gen,palette='RdBu')
plt.gcf().set_size_inches(8,8)
plt.xticks(rotation=90)
plt.show()


suicide_by_hanging_insecticde= df[(df.Type=='By Hanging') | (df.Type=='By Consuming Insecticides')]
plot = sns.catplot(x='Year', y='Total',  hue="Gender", col="Type",kind='bar',\
                      data=suicide_by_hanging_insecticde, estimator=sum, palette=sns.color_palette("Set2"), height=6, aspect=3)
plot.set_xticklabels(rotation=45, horizontalalignment='right');
plt.gcf().set_size_inches(8,8)
plt.show()

'''
suicide_by_hanging= df[(df.Type=='Love Affairs')]
sns.barplot(x='Year', y='Total',  hue="Age_group", data=suicide_by_hanging,estimator=sum)
plt.xticks(rotation=45);
plt.gcf().set_size_inches(15,8)
plt.show()