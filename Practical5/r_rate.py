#R rate
#the number of IBI1 students=84
#the infected rate=1.2
#every time the number of infected students=the number of infected students last time*1.2
r=1.2
total=84
i=0
while i<5:
   m=r*total
   total=total+m
   i=i+1
print("r rate is", str(r),"after 5 rounds of infection for a given r rate the number of infected individuals is",str(total)) 




















