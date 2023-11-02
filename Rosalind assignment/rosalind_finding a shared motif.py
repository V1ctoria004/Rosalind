#defining characters
substring = ''
sequences=[]
shortest = 1000

from Bio import SeqIO
for seq_record in SeqIO.parse("rosalind_lcsm.txt", "fasta"):
    sequences.append(seq_record.seq)


#finding the shortest sequence of all of them 
shortest = min(len(seq) for seq in sequences) 

for index in range(shortest):
    for base in range(index + len(substring) + 1, shortest + 1):
        common = sequences[0][index:base]
        if all(common in seq for seq in sequences):
            substring = common


print(substring)