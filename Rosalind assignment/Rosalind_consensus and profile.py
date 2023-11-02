#consensus and profile 

#need to create a list within a list 
sequences2 = []
sequences = {}
composite = []
max_count = 0 
consensus = ''
valA = ''
valC = ''
valG = ''
valt = ''

file = open ("rosalind_cons.txt")
for line in file:
    if line.startswith('>'):
        name = line[1:].rstrip('\n')
        sequences[name] = ''
    else:
        sequences[name] = sequences[name] +line.rstrip('\n')

for item in sequences.keys ():
    sequences2.append (sequences[item])

n = len(sequences2[0])

matrix = {
    "A":[0]*n,
    "C":[0]*n,
    "G":[0]*n,
    "T":[0]*n
}

for dna in sequences2:
    for position, nucleotide in enumerate(dna):
        matrix [nucleotide][position] += 1 

for position in range(n):
    max_nucleotide = None
    for nucleotide in ['A','C','G','T']:
        count = matrix [nucleotide][position]
        if count > max_count:
            max_count = count
            max_nucleotide = nucleotide
    consensus += max_nucleotide
    max_count = 0

print(consensus)

for name in matrix['A']:
    valA += str(name) +' '
for rose in matrix['C']:
    valC += str(rose)+ ' '
for street in matrix['G']:
    valG += str(street)+ ' '
for shoe in matrix['T']:
    valt += str(shoe)+' '


print('A:',valA)
print ('C:',valC)
print ('G:',valG)
print ('T:',valt)
