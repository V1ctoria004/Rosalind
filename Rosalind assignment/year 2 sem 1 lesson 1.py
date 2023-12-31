'''dna = "GCCAATACAGCGCCCTGAGTTCTGAATCCCGTCAACACTTCAGGAACGCGAGAATATCGGATGATGCCACTCCGCTGTGTCATAGGTCATTACCTACACCGCTACAAAGTAAGCAGCGGCCTCCTAGTTGGCTCTCTTTACTACTGACCTAGCAGCAACCGCAAAGGGCCAGTGTTCACATCGCAGTATGTTCGAGACAAGCAACTTCTGCTGATGAGCAGACTTATCCGACAAGTCTTGATTGCATACTATAACGTCACTCAGGCTGCTATAAGATTGACTTACTCATGCGTCCTAGTCAGATTCTAAACTGGGCGGAGTGGGGGCTTAAATGTCCTCATAACCAATTGACTACGCTGAGCGTGGCACCATTTAACTAAGCAACTATGAATTCGTTAGCAAGTGCGCATCTATTAGTGATTGTTGCCTACGGTTATTGACAAGGCGCCACGTGTCCTCCAGCGGTACGATCCCTCCCTTGCGTAGAACAAAGTCCCACCAGGTCGCCTACCTTGGTTCACTTTTTTTTTTCCAACACAGATCTTGCAAGCTATATACGAGAACTTTAAATAGTCTCGGGATCACATGAGTCAGCTTCGCTAATAGCGATATGTCTCCGAGACAGTAAGATAATCAACGTGAAGCTGACTATACGCGCGGACGGATGACGATGTCGAAGCCACATAATCCGCGGTTGCTAGACGTTACACGCGAGAAAGAGACGGCAAGAGCCTGCCCGCCTTTGATATACACAGGTTGGGCGAACTCTTATGTCCGGGATACCTCTATTGGCGCATCCATGAAAGAGTCCAGGGA"

#create counters 
a= 0
t= 0 
g= 0 
c= 0

for base in dna:
    if base == 'A':
        a+= 1
    elif base == 'T':
        t+= 1
    elif base == 'G':
        g+= 1
    else:
        c+= 1

print (a,c,g,t)

________________

dict_count = {'A':0, 'T': 0, 'C':0, 'G':0}
for symbol in dna:
    dict_count[symbol] += 1

print (dict_count)

#slay 

from collections import Counter 
base_count = Counter(dna)

print (base_count)

_____________

dnastrng = "AACACCTCCCCCTCTAGTAAGGCGATCAGGCGAGCGTAGATAGGTCAAGGGGATCAGATGTATCAGTGGTTTGCTCTCGGATACAACACTTAGTGCTGTAAGTATTCCATCGAGGTGCACTAATGGAGCCATTACGGCTCGTGCGGTTGTGGTATTGCCATAAATTTACTGGCGTGAAACCTTGTTTGTACCCTACTGAAATATGACCGCCAATCCCCAACATAACTTGAACAATAATTGCAATGTCAACTCGGAGATCAGTTCTTCGAAATCCGGCTTATGCGCCGTTGGGTGTTTACTCCGCCAACGTAAAACGCCCATTTCACTACATGTACTCCCGTAGCAGCACGTAATGACCGCTGACTACCAACAACCTTTACTCACCCTGAGCGTTATGCATACTAGTGGGACTCACACGGTCGCAGGCAGTCCCGAGTTAGACGGAAGGGCGTGAGCCCCCGAAGTGGTATGATATCATGCCGATCCCCCTCCGTGTCGGCAGACACGAACTCCACACACGTAGCGGCGTAGAAAAACACCTATAGCCAGTGCAGTGTTCGCCATCGATGATGAGAGCAGTGCTTACAAGATCAGCGCGGTTTTCAGCGCGCCTGTGTCCAAATCGCTGCCCTTCATCCATGCCAAACTGGTCCAAACATCCCTAAGAAGCCTTTTGGCTAATCGTGCGCTCCCCTATAGCACTGTCTGGACCTCTCCTAGTCCGCATCGCTACCAGTGTGATTATTAATGGTACGGAGTTCTCAGCGATGGATCGACAACGAGCCTAAGGCTGAGCGGGTTCGGCTTTCGGATCAAAGCACGGCTGGTGCCTATTGACACCAACACACAATTATGGTCCCGCGATGGTCGCGATTCTCGGAAGTCTCACTGGTATCTAAGGAAACGGCCGTTATGTCATAGAGAATGCTGCGCCAAAAGAATTAGTCGGCTTGCTATCGCTTAGCGTAGATTGCATCCG"

rnastrng = ""

for base in dnastrng:
    if base != 'T':
        rnastrng += base
    else:
        rnastrng += "U"

print (rnastrng)

'''
________
dna_string = "AAACAAATAGGACCCTCCCGTTCGCTAGCCGTTAATTTATGGCGTATGACCACGTCACCGAGGATAACTGCACCCCAATCGCTAGTAACGCAACTTTTTCGGATCGCGTCTGCTATTGTAAGGGCCTGGCCAGCTCTGGCTTTGTCATTATAACCGCTGGAGGTAGGATCTGTCCGGACCTTTAGCCCTCCGTAAAGCAAGCGTTCCTTACAGGCAAAATAGTACCGCTACAACATCATTTACATTCTGCAGTAGACTCCATAGCGTCCTGTCACTAGCCACCGTTAGGTCTCTCGAGAGATACAGTGCGCGGATGAATTCCAGACCCCAGCGCGCCCGCAGCAGACGTCGGTACCGTTGCAACGACGAGGACACACGTGGCAGTCTCGCGGTCGGGGTGGAGTAACAACATTGACACAAGGGGATGCCACGATGCCCCGCGTCGAGTGTTAGCATGTTCAGAACTATGGTACATGCCATAGTTACAAGTAATCTGCGTTAGCGCCGTGATTAGGGGATCCAACGTACTCAATCTCATACGGAATAGTTCAAGGTTAATGACCTTTAAGTACCACCATAGTGACGTGATATCTTGTATAGGCGACAACGAGAGGTAGAGCTCGTCCCTGAACAGAATCGCCACGGTGAACGAGATGTGCCTGTTTCCTTCTAGGCTTCACGTCGCCAGGCCAGCCGTAGACTGAACACATCGTGACGTCGAGACCTGCACCGTTTCACTAGAGGTTATCCTCAAGCTGACTTACAGTAACTATCTCACGAACGCGTTGAGCGGAGGATAGTGATGCAGCCCCGCTTGTCGTAGTTTATGTGAGTACGTTCTCGCATCGTCTTATTCACATGCTTGCCTGAGTAGTTCCTCCCGCCCCCGAAATAGACAGGAAATTGACCACTCCCGTAGTGTATGTAGTGAAGTGGCGGTTGGTAC"
compliment = ""

for base in dna_string:
    if base == 'A':
        compliment += 'T'
    elif base == 'T':
        compliment += 'A'
    elif base == 'C':
        compliment += 'G'
    else:
        compliment += 'C'

rvrs_compliment = ""
rvrs_compliment = compliment [::-1]
#print (compliment)
print (rvrs_compliment)

#the code shouldn't be repetitive we shouldn't copy paste 
______

#other way of doing it more efficient 
new_sequence = ''
dict_conversion = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}

for pos in range(len(dna_string)-1, -1, -1):
    #goes backwards from length until 0 by steps of -1
    new_sequence += dict_conversion [pos]
