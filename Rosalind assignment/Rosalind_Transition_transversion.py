#Transitions and Transversions

from Bio import SeqIO
s1= []
s2 = []
for nucleicacid in SeqIO.parse("", "fasta"):
    if nucleicacid == 0:
        s1.append(nucleicacid)
    elif nucleicacid == 1:
        s2.append(nucleicacid)

print(s1,s2)
transition = 0 
transversion = 0 
for index in s1:
    if s1[index] != s2 [index]:
        #then we have a mutation 
        if s1[index] == 'A' and s2 [index] == 'G' or s1 [index] == 'G' and s2[index]=='A':
            transition+=1
        elif s1[index] == 'C' and s2[index]=='T' or s1[index]=='T' and s2[index]=='C':
            transition+=1
        elif s1[index] == 'A' and s2[index]=='C' or s1[index] == 'C' and s2[index]=='A':
            transversion+=1
        elif s1[index] == 'A' and s2[index]=='T' or s1[index] == 'T' and s2[index]=='A':
            transversion+=1
        elif s1[index] == 'G' and s2[index]=='C' or s1[index] == 'C' and s2[index]=='G':
            transversion+=1
        elif s1[index] == 'G' and s2[index]=='T' or s1[index] == 'T' and s2[index]=='G':
            transversion+=1
        
Ratio = transition/transversion
print (Ratio)
        

