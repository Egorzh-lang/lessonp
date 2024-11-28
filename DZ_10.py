import pandas as pd
df1 = pd.DataFrame({'A': [1, 2], 'B': [4, 5]})
df2 = pd.DataFrame({'A': [1, 5], 'B': [4, 1]})

result1 = pd.merge(df1, df2, left_index=True, right_index=True, how='outer')
result2 = pd.concat([df1, df2])
print("\nОбъединение с помощью pd.merge():\n", result1)
print("\nОбъединение с помощью pd.concat:\n", result2)
#############################################################################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


dt= { 'Time': [1, 2, 3, 4, 5, 6, 7, 8, 9], "longitude" : [14.310, 18.47, 10.57, 114.570, 16.58, 114.58, 13.59, 89.59, 114.6], "latitude": [32, 35, 36, 34.34, 34, 41, 46, 99, 60]}

df = pd.DataFrame(dt)
plt.figure(figsize=(10, 6))

plt.plot(df['Time'], df["longitude"], label="longitude")
plt.plot(df['Time'], df["latitude"], label="latitude")
plt.xlabel('Time')
plt.ylabel("longitude")
plt.title("shjgcls,gj")
plt.legend()
plt.grid()
plt.show()
