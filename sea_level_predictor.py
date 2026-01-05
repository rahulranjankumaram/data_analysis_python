import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from scipy.stats import linregress
f='https://raw.githubusercontent.com/rahulranjankumaram/data_analysis_python/refs/heads/main/epa-sea-level.csv'
df=pd.read_csv(f)

plt.figure(figsize=(9,6))
x = df['Year']
y = df['CSIRO Adjusted Sea Level']
plt.scatter(x,y,color='yellow')
plt.plot(x,y,color='yellow')

result = linregress(x,y,nan_policy='omit')
ny = np.array(np.arange(1880,2076))
py = result.slope * ny + result.intercept
plt.plot(ny,py,color='blue')
plt.scatter(ny[170],py[170],color='blue',marker='o')

ny1 = np.array(np.arange(2000,2076))
result1 = linregress(ny,py)
py1 = result1.slope * ny1 + result1.intercept
plt.plot(ny1,py1,color='red')
plt.scatter(ny1[0],py1[0],color='red',marker='o')
plt.scatter(ny1[23],py1[23],color='red',marker='o')
plt.scatter(ny1[50],py1[50],color='red',marker='o')

lines = [Line2D([0],[0],label='1880 to 2050',color='blue'),
          Line2D([0],[0],label='2000,2023,2050',color='red'),
          Line2D([0],[0],label='1880 to 2023',color='yellow',marker='o')
]
plt.legend(loc='upper left',title='Lines',fontsize=9,handles=lines)
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
plt.show()