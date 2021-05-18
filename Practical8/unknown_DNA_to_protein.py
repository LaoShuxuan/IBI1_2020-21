import re
# read .fa file as a list
import re
#give the codon dictionary
codon = {
                "TTT": 'F', "TTC": 'F', "TTA": 'L', "TTG": 'L',
                "TCT": 'S', "TCC": 'S', "TCA": 'S', "TCG": 'S',
                "TAT": 'Y', "TAC": 'Y', "TAA": 'STOP', "TAG": 'STOP',
                "TGT": 'C', "TGC": 'C', "TGA": 'STOP', "TGG": 'W',
                "CTT": 'L', "CTC": 'L', "CTA": 'L', "CTG": 'L',
                "CCT": 'P', "CCC": 'P', "CCA": 'P', "CCG": 'P',
                "CAT": 'H', "CAC": 'H', "CAA": 'Q', "CAG": 'Z',
                "CGT": 'R', "CGC": 'R', "CGA": 'R', "CGG": 'R',
                "ATT": 'I', "ATC": 'I', "ATA": 'J', "ATG": 'M',
                "ACT": 'T', "ACC": 'T', "ACA": 'T', "ACG": 'T',
                "AAT": 'N', "AAC": 'B', "AAA": 'K', "AAG": 'K',
                "AGT": 'S', "AGC": 'S', "AGA": 'R', "AGG": 'R',
                "GTT": 'V', "GTC": 'V', "GTA": 'V', "GTG": 'V',
                "GCT": 'A', "GCC": 'A', "GCA": 'A', "GCG": 'A',
                "GAT": 'D', "GAC": 'D', "GAA": 'E', "GAG": 'E',
                "GGT": 'G', "GGC": 'G', "GGA": 'G', "GGG": 'G',
            }

open_file = open("unknown_function.fa", 'r')
lines = open_file.readlines()
output = []
#get the gene name
for line in lines:
    if line.startswith(">"):
        output.append(line)
    else:
        #translate and get the protein sequence
        protein = ""
        for i in range(0, len(line), 3):
            if codon[line[i:i+3]] != "STOP":
                protein += codon[line[i:i+3]]
            else:
                break
        protein += "\n"
        output.append(protein)
print(output)
#count the length of protein sequence
for i in range(len(output)):
    if output[i].startswith(">"):
        output[i] = re.findall(r'>.+? ', output[i])[0]
        output[i] += str(len(output[i+1]))
        output[i] += "\n"

# write the results in a new file
new_file = open('unknown_proteins.fa', 'w')
for line in output:
        new_file.write(line)
new_file.close()



