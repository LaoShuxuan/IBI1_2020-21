#make new lists
gene_lengths=[9410,394141,4442,105338,19149,76779,126550,36296,842,15981]
exon_counts=[51,1142,42,216,25,650,32533,57,1,523]
#calculate the ten average numbers
average=[gene_lengths[i]/exon_counts[i] for i in range(10)]
#returns sorted list, does not mutate average
sorted(average)
average=sorted(average)
average.sort()
#output the sorted list
print(average)
#add a boxplot
import numpy as np
import matplotlib.pyplot as plt
#specifies the properties of the boxplot
n = 10
score = average
plt.boxplot(score,vert=True,whis=1.5,patch_artist=True,meanline=False,showbox=True,showcaps=True,showfliers=True,notch=False)
#show the boxplot
plt.show()

