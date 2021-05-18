import re
file=open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa","r")
line = file.readlines()
output = []
# find unknown function DNA
for i in range(len(line)):
    if line[i].startswith('>') and re.search(r'unknown function', line[i]):
        name=re.search(r'(>.+?)_',line[i])
        # get the name of the gene
        Gene_name = name.group()
        Gene_name = re.sub('_','',Gene_name)
        output.append(Gene_name)
        a = ''
        for k in range(len(line[i:-1])):
            if line[i+k+1].startswith('>'):
              break
            else:
              a += line[i+k+1][:-1]
        a += "\n"
        output.append(a)
# get the length of the gene
for i in range(len(output)):
    if output[i].startswith('>'):
        length=str(len(output[i+1])-1)
        output[i] += "  "
        output[i] += length + "\n"
#write the results in a new file
fout = open('unknown_function.fa', 'w')
results = ''
results =''.join(output)
fout.write(results)
fout.close()