import pandas as pd
import matplotlib.pyplot as plt

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
