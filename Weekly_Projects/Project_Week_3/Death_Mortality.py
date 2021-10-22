from numpy.lib.polynomial import poly
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 


df=pd.read_csv("data_2.csv")
#cheking if null values are present or not
print(df.isnull().sum())
# Filling the null values in the data
df['High total cholesterol'] = df['High total cholesterol'].fillna(value=df['High total cholesterol'].mean())
df['Outdoor air pollution'] = df['Outdoor air pollution'].fillna(value=df['Outdoor air pollution'].mean())



# ....................LINEAR REGRESSION..............................
def linear_regression_coeff(x,y):
    number_of_observation=np.size(x)
    x_mean=np.mean(x)
    y_mean=np.mean(y)
    xy_sd=np.sum(np.array([i-x_mean for i in x])*np.array([i-y_mean for i in y]))
    xx_sd=np.sum(np.array([i-x_mean for i in x])*np.array([i-x_mean for i in x]))
    m=xy_sd/xx_sd 
    c=y_mean-m*x_mean 
    print("Regression Coeff "+str(m)+"  c value: "+str(c))
    return m,c 

def linear_regression_plotting(x,y,m,c,catogry):
    plt.scatter(x,y,marker='.')
    predicted_y=c+m*x
    plt.xlabel(catogry[0])
    plt.ylabel(catogry[1])
    plt.title(catogry[0]+" vs "+catogry[1])
    plt.ticklabel_format(style='plain', axis='y')
    plt.ticklabel_format(style='plain', axis='x')
    plt.gcf().set_size_inches(8, 8)
    plt.plot(x,predicted_y,color='red')
    plt.savefig("./static/"+catogry[0]+" vs "+catogry[1]+".png",format='png')
    plt.show()


# Non exclusive breastfeeding and High fasting plasma glucose
non_exclusive_breastfeeding=df[df['Entity']=='World']['Non-exclusive breastfeeding'].values
high_fasting_plasma_glucose=df[df['Entity']=='World']['High fasting plasma glucose'].values
m,c=linear_regression_coeff(non_exclusive_breastfeeding,high_fasting_plasma_glucose)
linear_regression_plotting(non_exclusive_breastfeeding,high_fasting_plasma_glucose,m,c,["non_exclusive_breastfeeding","high_fasting_plasma_glucose"])

# High body mass index and High systolic blood pressure
High_body_mass_index=df[df['Entity']=='World']['High body-mass index'].values
High_systolic_blood_pressure=df[df['Entity']=='World']['High systolic blood pressure'].values
m,c=linear_regression_coeff(High_body_mass_index,High_systolic_blood_pressure)
linear_regression_plotting(High_body_mass_index,High_systolic_blood_pressure,m,c,["High_body_mass_index","High_systolic_blood_pressure"])
#Regression Coeff 1.3493372335852778  c value: 3974594.171068143


# high body mass index and high systolic blood pressure
High_body_mass_index=df[df['Entity']=='World']['High body-mass index'].values
High_systolic_blood_pressure=df[df['Entity']=='World']['High systolic blood pressure'].values
m,c=linear_regression_coeff(High_body_mass_index,High_systolic_blood_pressure)
linear_regression_plotting(High_body_mass_index,High_systolic_blood_pressure,m,c,["High_body_mass_index","High_systolic_blood_pressure"])
# Regression Coeff 1.3493372335852778  c value: 3974594.171068143

# High body mas index and high fasting plasma glucose
High_body_mass_index=df[df['Entity']=='World']['High body-mass index'].values
High_fasting_plasma_glucose=df[df['Entity']=='World']['High fasting plasma glucose'].values
m,c=linear_regression_coeff(High_body_mass_index,high_fasting_plasma_glucose)
linear_regression_plotting(High_body_mass_index,high_fasting_plasma_glucose,m,c,["High_body_mass_index","high_fasting_plasma_glucose"])
#Regression Coeff 1.2419553799742353  c value: 734317.9083546093


from sklearn.metrics import r2_score
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# ...........................................Polynomial Regression ...................................
def polynomial_regression_graph(x,y,catogry):
    poly=PolynomialFeatures(degree=2)
    x_poly=poly.fit_transform(x.reshape(-1,1))
    poly_model=LinearRegression()
    poly_model.fit(x_poly,y.reshape(-1,1))
    y_pred=poly_model.predict(x_poly)
    plt.scatter(x,y)
    plt.xlabel(catogry[0])
    plt.ylabel(catogry[1])
    plt.title(catogry[0]+" vs "+catogry[1])
    plt.ticklabel_format(style='plain', axis='y')
    plt.ticklabel_format(style='plain', axis='x')
    plt.gcf().set_size_inches(8, 8)
    plt.plot(x,y_pred,c='red')
    plt.savefig("./static/"+catogry[0]+" vs "+catogry[1]+".png",format='png')
    plt.show()

# calculating r2 score
def r_score(x,y):
    poly=np.poly1d(np.polyfit(x,y,4))
    return (r2_score(y,poly(x)))

# function to predict the dependent value 
def multiple_regression_predict(x,y,value):
    poly=np.poly1d(np.polyfit(x,y,4))
    return(poly(value))

# smoking and secondhand smoking using polynomial regression
smoking=df[df['Entity']=='World']['Smoking'].values
Secondhand_smoke=df[df['Entity']=='World']['Secondhand smoke'].values
polynomial_regression_graph(smoking,Secondhand_smoke,["smoking","Secondhand_smoke"])

# Alcohol and iron deficiency  using polynomial regression
Alcohol=df[df['Entity']=='World']['Alcohol use'].values
Iron_Deficiency=df[df['Entity']=='World']['Iron deficiency'].values
polynomial_regression_graph(Alcohol,Iron_Deficiency,["Alcohol","Iron_Deficiency"])
print(r_score(Alcohol,Iron_Deficiency))

# High Diet in sodium and high systolic blood pressure using polynomial regression
High_Diet_in_sodium=df[df['Entity']=='World']['Diet high in sodium'].values
High_systolic_blood_pressure=df[df['Entity']=='World']['High systolic blood pressure'].values
polynomial_regression_graph(High_Diet_in_sodium,High_systolic_blood_pressure,["Diet high in sodium","High_systolic_blood_pressure"])
print(r_score(High_Diet_in_sodium,High_systolic_blood_pressure)) #0.9937590089936722

# Alcohol and high systolic blood pressure using polynomial regression
Alcohol=df[df['Entity']=='World']['Alcohol use'].values
High_systolic_blood_pressure=df[df['Entity']=='World']['High systolic blood pressure'].values
polynomial_regression_graph(Alcohol,High_systolic_blood_pressure,["Alcohol","High_systolic_blood_pressure"])
print(r_score(Alcohol,High_systolic_blood_pressure)) # 0.983292155827949

#Alcohol and high fasting plasma glucose using polynomial regression
Alcohol=df[df['Entity']=='World']['Alcohol use'].values
High_fasting_plasma_glucose=df[df['Entity']=='World']['High fasting plasma glucose'].values
polynomial_regression_graph(Alcohol,High_fasting_plasma_glucose,["Alcohol","High_fasting_plasma_glucose"])
print(r_score(Alcohol,High_fasting_plasma_glucose)) # 0.9926971195939249

# Smoking and high systolic blood pressure using polynomial regression
smoking=df[df['Entity']=='World']['Smoking'].values
High_systolic_blood_pressure=df[df['Entity']=='World']['High systolic blood pressure'].values
polynomial_regression_graph(smoking,High_systolic_blood_pressure,["Smoking","High_systolic_blood_pressure"])
print(r_score(smoking,High_systolic_blood_pressure)) #0.9768429674909027

# Low physical activity and high fasting plasma glucose using polynomial regression
Low_physical_activity=df[df['Entity']=='World']['Low physical activity'].values
High_fasting_plasma_glucose=df[df['Entity']=='World']['High fasting plasma glucose'].values
polynomial_regression_graph(Low_physical_activity,high_fasting_plasma_glucose,["Low_physical_activity","high_fasting_plasma_glucose"])
print(r_score(Low_physical_activity,high_fasting_plasma_glucose)) # 0.9966596200271718

# Low physical activity and high body mass index using polynomial regression
Low_physical_activity=df[df['Entity']=='World']['Low physical activity'].values
High_body_mass_index=df[df['Entity']=='World']['High body-mass index'].values
polynomial_regression_graph(Low_physical_activity,High_body_mass_index,["Low_physical_activity","High_body_mass_index"])
print(r_score(Low_physical_activity,High_body_mass_index)) #0.9971709855181173

# Low physical activity and high total cholesterol using polynomial regression
Low_physical_activity=df[df['Entity']=='World']['Low physical activity'].values
High_total_cholesterol=df[df['Entity']=='World']['High total cholesterol'].values 
polynomial_regression_graph(Low_physical_activity,High_total_cholesterol,["Low_physical_activity","High_total_cholesterol"])
print(r_score(Low_physical_activity,High_total_cholesterol)) #0.04922471230385417

# Smoking and high fasting plasma glucose using polynomial regression
smoking=df[df['Entity']=='World']['Smoking'].values
High_fasting_plasma_glucose=df[df['Entity']=='World']['High fasting plasma glucose'].values
polynomial_regression_graph(smoking,High_fasting_plasma_glucose,["Smoking","High_fasting_plasma_glucose"])
print(r_score(smoking,High_fasting_plasma_glucose)) #0.9557790268077183


# Discontonued breastfeeding and child stunting using polynomial regression
Discontinued_breastfeeding=df[df['Entity']=='World']['Discontinued breastfeeding'].values
Child_Stunting=df[df['Entity']=='World']['Child stunting'].values
polynomial_regression_graph(Discontinued_breastfeeding,Child_Stunting,["Discontinued_breastfeeding","Child_Stunting"])
print(r_score(Discontinued_breastfeeding,Child_Stunting)) #0.9926684191510694


from sklearn import linear_model

#.................... MULTIPLE REGRESSION .......................................................
def multiple_regression(x_data,y_data):
    regression_object=linear_model.LinearRegression()
    regression_object.fit(x_data,y_data)
    print(regression_object.coef_)

#calculating coefficient of multiple regression
def cov_mr(x_data,y_data):
    regression_object=linear_model.LinearRegression()
    regression_object.fit(x_data,y_data)
    return (regression_object.coef_)

# Unsafe water source, No acces to handwashing facility and unsafe sanitation
data_1=df[['Unsafe water source','No access to handwashing facility']]
data_2=df['Unsafe sanitation']
multiple_regression(data_1,data_2)
print(cov_mr(data_1,data_2))
# [0.62798671 0.20555965]

# Discontinued breastfeeding, Low bone minearl density and child Stunting using multiple regression

data_1=df[['Discontinued breastfeeding','Low bone mineral density']]
data_2=df['Child stunting']
multiple_regression(data_1,data_2)
print(cov_mr(data_1,data_2))
#[30.69259285 -0.08042504] 


# Householf air pollution from solid fuels, Outdoor air pollution and Air pollution
data_1=df[['Household air pollution from solid fuels','Outdoor air pollution']]
data_2=df['Air pollution']
multiple_regression(data_1,data_2)
print(cov_mr(data_1,data_2))
#[0.96990517 0.96099744] 

#Alcohol use, Smoking and high systolic blood pressure
data_1=df[['Alcohol use','Smoking']]
data_2=df['High systolic blood pressure']
multiple_regression(data_1,data_2)
print(cov_mr(data_1,data_2))
#[1.7269133 0.6494313] 

#Diet low in fruits, Diet low in vegetables and Vitamin A deficiency
data_1=df[['Diet low in fruits','Diet low in vegetables']]
data_2=df['Vitamin A deficiency']
multiple_regression(data_1,data_2)
print(cov_mr(data_1,data_2))
#[-0.64413383  1.40914561] 

#Low physical activity, High body mass index and High fasting plasma glucose
data_1=df[['Low physical activity','High body-mass index']]
data_2=df['High fasting plasma glucose']
multiple_regression(data_1,data_2)
print(cov_mr(data_1,data_2))
#[1.58234191 0.93088658] 

#Low physical activity, High body mass index and High total cholesterol
data_1=df[['Low physical activity','High body-mass index']]
data_2=df['High total cholesterol']
multiple_regression(data_1,data_2)
print(cov_mr(data_1,data_2)) 
#[ 0.98984082 -0.09115213] 

# Non-exclusive breastfeeding, Low bone mineral density and Child stunting
data_1=df[['Non-exclusive breastfeeding','Low bone mineral density']]
data_2=df['Child stunting']
multiple_regression(data_1,data_2)
print(cov_mr(data_1,data_2))
#[ 2.17804356 -0.34999538] 

# Alcohol use, Secondhand smoke and high systolic blood pressure.
data_1=df[['Alcohol use','Secondhand smoke']]
data_2=df['High systolic blood pressure']
multiple_regression(data_1,data_2)
print(cov_mr(data_1,data_2))
#[3.14795451 0.59080186] 

# For pollting the average number of deaths caused by each factor in entire world.
import seaborn as sns
world = df[df['Entity']=='World']

risk_factors = [i for i in world.columns if i not in ['Entity','Year','Code']]

average_deaths = []

for i in risk_factors:
    average_deaths.append(world[i].mean())

df1 = pd.DataFrame(list(zip(risk_factors,average_deaths)),columns=['Risk Factor','Avg. Deaths']).sort_values(by='Avg. Deaths',ascending=False)

plt.figure(figsize=(20,8),dpi=300)
sns.barplot(y='Risk Factor',x='Avg. Deaths',data=df1)
plt.title('Avg. Deaths due to Each Factor - WORLD')
plt.xlabel('Avg. Deaths (in. lakhs)')
plt.savefig('Avg. Deaths due to Each Factor - WORLD.png',format='png')
plt.show()

#Printing the plots of all factors on number of deaths from 1990 to 2017.
risk_factors = [i for i in world.columns if i not in ['Entity','Year','Code']]

plt.figure(figsize=(18,50))

for index,i in enumerate(risk_factors):
    plt.subplot(10,3,index+1)
    plt.bar(world['Year'],world[i],label=i)
    plt.title(i)
    plt.ylabel('Deaths')
    plt.xlabel('Year')
plt.savefig("Number_of_deaths_of_each_factor.png",format='png')
plt.show()
