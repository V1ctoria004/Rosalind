#Finding a motif in DNA 

s_mainstring = 'GATATATGCATATACTT'
t_substring = 'ATAT'
occurences = 0
occurences = []

if len(t_substring) < len(s_mainstring):
  for letter in s_mainstring:
     if s_mainstring(letter) == t_substring(letter): 
        True
else:
   False


from Bio import motifs