import os
import pandas as pd
# noinspection PyUnresolvedReferences
import matplotlib.pyplot as plt
# noinspection PyUnresolvedReferences
import numpy as np
os.chdir("/python 代码/Practical7")
covid_data = pd.read_csv("full_data.csv")

s = covid_data.iloc[0:11:2, :]
print(s)
d = covid_data.loc[(covid_data.loc[:, "location"] == "Afghanistan"), "total_cases"]
print(d)

#calculate some important numbers
e = covid_data.loc[(covid_data.loc[:, "location"] == "World"), "new_cases"]
a = np.array(e)
b = np.mean(a)
c = np.median(a)
print(b)
print(c)

#draw the boxplot of world new cases
f = covid_data.loc[(covid_data.loc[:, "location"] == "World"), "new_cases"]
score1 = f
color = ['pink']
plt.title("new cases around the world")
plt.xlabel("world")
plt.ylabel("new cases")
plt.boxplot(score1, notch=False, vert=True, whis=1.5, patch_artist=True, meanline=True, showbox=True, showfliers=True)
plt.show()

#draw the plot of world new cases and world new deaths
g = covid_data.loc[(covid_data.loc[:,"location"] == "World"), "new_deaths"]
plt.title("new cases and new deaths worldwide")
plt.xlabel("world new cases")
plt.ylabel("world new deaths")
plt.plot(f, g, 'b+')
plt.show()

#question code
Surinamenewcases = covid_data.loc[(covid_data.loc[:,"location"] == "Suriname"),"new_cases"]
time = covid_data.loc[(covid_data.loc[:,"location"] == "Suriname"), "date"]
plt.title("new cases over time in Suriname")
plt.xlabel("time")
plt.ylabel("cases")
plt.plot(time,Surinamenewcases,'r+')
plt.legend(['Surinamenewcases'],loc='upper left')
plt.show()
