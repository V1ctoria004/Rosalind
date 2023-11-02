#Mendel's second law 
import math
k = 7 #number of generations
n = 37 #number of individuals that have to have the AaBb genome (at least)
individuals= 2**k
temporary = 0
probability = 0
posibilities = math.factorial (individuals) #possibilities how the 
for i in range (n,individuals+1):
    notheterozygous = individuals-i
    temporary = posibilities /(math.factorial(i) * math.factorial(notheterozygous)) * (0.25**i) * (0.75**(notheterozygous)) #posibilities that the individuals could be composedtimes the individuals who are not heterozygous
            #times the prob of the individuals being heterozygous, times the prob that the others arent                                                       
    probability += temporary

print (probability)