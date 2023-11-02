#finding a shared motif lcsm 

        #first parsing the file
file = open ('rosalind_lcsm.txt')
#creatinga  dictionary with the name of the sequence as a key 
sequences = {}
for line in file:
    if line.startswith('>'):
        name = line[1:].rstrip('\n')
        sequences[name] = ''
    else:
        sequences[name] = sequences[name] +line.rstrip('\n')

substring = ''

if len(sequences) > 1 and len(sequences[0]) >0:
    for index in range(len(sequences[0])):
        for base in range (len(sequences[0])-index+1):
            if base >len(substring) and all(sequences[0][index:index+base] in x for x in sequences):
                substring = sequences[0][index:index+base]

print (substring)