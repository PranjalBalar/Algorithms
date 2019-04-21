# -*- coding: utf-8 -*-

#This program prints all the prime numbers between 0 and 10000 
#It's complexity is order of n

import math
prime_numbers = []
list = range(2, 10000)

for i in list:
    x = math.sqrt(i)
    for j in prime_numbers:
        if i % j == 0:
            break  
        elif j > x:
            prime_numbers.append(i)
            print str(i), "is prime"
            break
    else:
        prime_numbers.append(i)
        print str(i), "is prime"
