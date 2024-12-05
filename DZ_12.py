import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
file = '/content/Mall_Customers.csv'
df = pd.read_csv(file, sep=',')


df_male = df[df['Genre'] == 'Male']


plt.figure(figsize=(10, 6))
plt.bar(df_male['Age'], df_male['Spending Score (1-100)'])

plt.xlabel('Age')
plt.ylabel('Spending Score (1-100)')
plt.title('Spending Score_Age_Male ')
plt.legend()
plt.grid(True)
plt.show()
###################################################################
grouped = df.groupby(['Genre', 'Annual Income (k$)'])['Spending Score (1-100)'].mean().unstack()


grouped.plot(kind='bar', figsize=(10, 6), color=['blue', 'red']) 

plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.title('Spending Score (1-100)_Annual Income (k$) by Genre')
plt.xticks(rotation=0) 
plt.legend(['Male', 'Female'])
plt.grid(axis='y')  
plt.show()
