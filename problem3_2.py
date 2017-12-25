#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?
    
#SOLUTION 2 (Using generator comprehension):

import math
num = 600851475143

print(next((-i for i in range(-int(math.sqrt(num)), -1)
            if num % abs(i) == 0 and
            all(abs(i) % j for j in range(2, abs(i))))))
