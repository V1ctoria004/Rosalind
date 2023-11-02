
'''


def rabbits (n,m): #n number of months, m number of months of life 
    babynow = 1 #defining variable
    babyprev = 0
    adultR = 0
    totalR = 0
    for n in range (1, n):
        babyprev = babynow  #the babies that were born last month are equal to the babies from last cycle
        babynow = 0
        babynow = adultR*2 #the babies now are k times the amount of adults, minus the babies from last month
        adultR = adultR + babyprev #the adults are the adults from the previous month(s) plus the former babies
        totalR = adultR +babynow #total number of rabbits is the adults plus the babies now  
    return totalR

print (rabbits(36,3))

'''



def mortalRabbits (n,m):
    Rpergen = [1,]
    babyrabbit = 1
    teenrabbit = 0 
    adultrabbit = 0
    totalafterdeath = 0
    for generation in range (1,n):
        teenrabbit = babyrabbit  #the babies that were born last month are equal to the babies from last cycle
        babyrabbit = 0
        babyrabbit = adultrabbit #each adult rabbit only has one baby in this case
        adultrabbit = adultrabbit + teenrabbit #the adults are the adults from the previous month(s) plus the former babies
        Rpergen.append (babyrabbit)
        if m+1 > len(Rpergen):
            totalafterdeath = adultrabbit + babyrabbit
        else:
            totalafterdeath = adultrabbit + babyrabbit - Rpergen [generation-m] #total number of rabbits is the adults plus the babies now minus the ones that died
            adultrabbit = adultrabbit - Rpergen [generation-m]
    return totalafterdeath

print (mortalRabbits(86,18))
