#mendel's first law 
import math
k = 29
m = 25
n = 18
unsuccessfull = 0 
successfull = 0
total = k + m + n
kafter = k - 1
mafter = m-1
nafter = n-1
totafter = total - 1
#total = math.factorial(k)+ k*m + k*n + math.factorial(m) + m*n + math. factorial(n)
#unsuccessfull route is smaller, calculate that 
'''
successfull = ((k/total)*k)*((k-1/total-1)*k-1) +((k/total)*k)*((m/total)*m) + ((k/total)*k)*((n/total)*n)
successfull += 3/4*((m/total)*m *(m-1/total-1)*m-1) 
successfull += 1/2*((m/total)*m *(n/total)*n)
'''

successfull = k/total*((kafter +m + n)/totafter)
successfull += (m/total)*(k/totafter)
successfull += 3/4*(m/total)*(mafter/totafter)
successfull += (1/2)*(m/total)*(n/totafter)
successfull += n/total * (k/totafter)
successfull += (1/2)*(n/total)*(m/totafter)


print (successfull)

# 29 17 20