#GC content 

from Bio import SeqIO
from Bio.SeqUtils import gc_fraction
gccontent = []
largestcontent = 0
for seq_record in SeqIO.parse("Rosalind_gc.txt", "fasta"): #file name to parse?
    gccontent.append (gc_fraction(seq_record)*100)
for percent in gccontent:
    if percent > largestcontent:
       largestcontent = percent
    else:
        largestcontent = largestcontent
print(gccontent)
print(largestcontent)
