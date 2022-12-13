import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Reading data to dataframe

df_stolen18 = pd.read_csv("2018.csv")
df_stolen19 = pd.read_csv("2019.csv")
df_stolen18_full = pd.read_csv("2018 full table.csv")
df_stolen19_full = pd.read_csv("2019 full table.csv")
df_bank_nifty = pd.read_csv("Nifty_bank.csv")

print(df_stolen19['Stolen'])


#Plotting bar graph

plt.figure()
plt.bar(df_stolen18['Type of property'], df_stolen18['Stolen'], alpha = 0.7 , label = 'Stolen')
plt.bar(df_stolen18['Type of property'], df_stolen18['Recovered'], alpha = 0.7 , label = 'Recovered')
plt.xlabel("Type of Property")
plt.ylabel("Number of item stolen")
plt.legend()
plt.title('2018')
plt.xticks(rotation = 90)
plt.show()


plt.figure()
plt.bar(df_stolen19['Type of property'], df_stolen19['Stolen'], alpha = 1.0 , label = 'Stolen')
plt.bar(df_stolen19['Type of property'], df_stolen19['Recovered'], alpha = 0.9 , label = 'Recovered')
plt.xlabel("Type of Property")
plt.ylabel("Number of items stolen")
plt.legend()
plt.title('2019')
plt.xticks(rotation = 90)
plt.show()

#Plotting subplots of above bar graphs

plt.figure()
plt.subplot(2,2,1)
plt.bar(df_stolen19['Type of property'], df_stolen19['Stolen'], alpha = 1.0 , label = 'Stolen')
plt.legend()
plt.title('2019')
plt.xticks(rotation = 90)

plt.subplot(2,2,2)
plt.bar(df_stolen19['Type of property'], df_stolen19['Recovered'], alpha = 0.5 , label = 'Recovered')
plt.xticks(rotation = 90)
plt.legend()
plt.show()

#plt.figure()
plt.subplot(2,2,1)
plt.bar(df_stolen18['Type of property'], df_stolen18['Stolen'], alpha = 1.0 , label = 'Stolen')
plt.legend()
plt.title('2018')
plt.xticks(rotation = 90)

plt.subplot(2,2,2)
plt.bar(df_stolen18['Type of property'], df_stolen18['Recovered'], alpha = 0.8 , label = 'Recovered')
plt.xticks(rotation = 90)
plt.legend()
plt.show()


#plotting pie graph

plt.figure(figsize=(10,10))
plt.pie(df_bank_nifty['WEIGHT'],labels = df_bank_nifty['COMPANY NAME'], pctdistance= 1) 
#plt.pie()
plt.title('NIFTY BANK WEIGHTAGE')
plt.show()

#plotting line graph

plt.figure()
plt.plot(df_stolen18_full['State'], df_stolen18_full['Number of agencies reporting an incident'], label = 'Incidents reported by agencies')
plt.plot(df_stolen18_full['State'], df_stolen18_full['Number of incidents reported'],label = 'Incidents reported')
plt.xticks(rotation = 90)
plt.legend()
plt.show()



