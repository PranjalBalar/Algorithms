#This program prints all the prime numbers between 0 and 1000
#It has a complexity of n²

list = range(2, 1000)

for i in list:
    for j in range(2, i):
        if i % j == 0:
            break
            
    else:
        print str(i), "is prime"
        
