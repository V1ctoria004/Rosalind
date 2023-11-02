#Fibonaci Rabbits



def rabbits (n,k):
    babynow = 1 #defining variable
    babyprev = 0
    adultR = 0
    totalR = 0
    for n in range (1, n):
        babyprev = babynow  #the babies that were born last month are equal to the babies from last cycle
        babynow = 0
        babynow = adultR*k #the babies now are k times the amount of adults, minus the babies from last month
        adultR = adultR + babyprev #the adults are the adults from the previous month(s) plus the former babies
        totalR = adultR +babynow #total number of rabbits is the adults plus the babies now  
    return totalR

print (rabbits(36,3))
    
