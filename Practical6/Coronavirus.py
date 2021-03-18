#input data to a new dictionary 
rates = {'USA':29862124,'India':11285561,'Brazil':11205972,'Russia':4360823,'UK':4234924}
#output the dictionary
print(rates)
#add a plot
import matplotlib.pyplot as plt
#pie chart,where the slices will ordered and plotted counter-clockwise
labels = 'USA','India','Brazil','Russia','UK'
sizes = [29862124,11285561,11205972,4360823,4234924]
explode = (0,0,0,0,0)
#specifies the fraction of the radius with which to offset each wedge
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90)
#Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')
#show the plot
plt.show()
