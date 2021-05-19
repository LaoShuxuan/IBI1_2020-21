#import some modules
from xml.dom.minidom import parse
import xml.dom.minidom
import matplotlib.pyplot as plt
import numpy as np
import os
import warnings
warnings.filterwarnings('ignore')

os.chdir("/python 代码/Practical14")

#get all the element  the file go_obo.xml
dom = xml.dom.minidom.parse("go_obo.xml")
root = dom.documentElement
terms = root.getElementsByTagName("term")

#define a function to find the id(s) in terms, and store them in a dictionary.
def id_found(terms):
    dict={}
    for term in terms:
        #search all the terms with "is_a" and also all the id
        is_a = [child.childNodes[0].data for child in term.getElementsByTagName("is_a")]
        all_id = term.getElementsByTagName("id")[0].childNodes[0].data
        for id_fa in is_a:
            if id_fa in dict:
                dict[id_fa].append(all_id)
            else:
                dict[id_fa] = [all_id]
    return dict

#define a function to search the terms which are related to DNA, RNA, protein and other biomolecules
def related(terms,biomolecule):
    gene = []
    for term in terms:
        defstr = term.getElementsByTagName("defstr")[0].childNodes[0].data
        #find the id related to specific molecule
        id_link = term.getElementsByTagName("id")[0].childNodes[0].data
        if not biomolecule.isupper():
            defstr = defstr.lower()
        if biomolecule in defstr:
            gene.append(id_link)
    return set(gene)

#get all the childnodes
def getnodes(dict,lists):
    allnodes = []
    for i in lists:
        if i in dict:
            a = dict[i]
            allnodes += a
            allnodes += getnodes(dict,a)
    return allnodes

# calculate all the childnodes
def childnodes_number(terms,biomolecule):
    dict = id_found(terms)
    b = related(terms,biomolecule)
    c = getnodes(dict,b)
    num = len(set(c))
    return num

# get and print the number of childnodes of DNA, RNA, protein, and carbohydrate.
DNA = childnodes_number(terms,"DNA")
print("The number of childNodes of all DNA-associated terms is:", DNA)
RNA = childnodes_number(terms,"RNA")
print("The number of childNodes of all RNA-associated terms is:", RNA)
Protein = childnodes_number(terms,"protein")
print("The number of childNodes of all protein-associated terms is:", Protein)
Carbohydrate = childnodes_number(terms,"carbohydrate")
print("The number of childNodes of all carbohydrate-associated terms is:", Carbohydrate)




#make a pie chart
labels = 'DNA', 'RNA', 'Protein', 'Carbohydrate'
sizes = [DNA, RNA, Protein, Carbohydrate]
explode = (0, 0, 0, 0)
plt.title('the numbers of childNodes associated with DNA, RNA, protein and carbohydrate')
plt.pie(sizes,
        explode=explode,
        labels=labels,
        autopct='%1.1f%%',
        shadow=False,
        startangle=90)
plt.show()
