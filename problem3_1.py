#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

#SOLUTION 1 (Using for-loop and break after getting the first result i.e. largest prime factor of num):
import math

num = 600851475143
hell = range(-int(math.sqrt(num)), -1)

for i in hell:
    if num % abs(i) == 0:
        if all(abs(i) % j for j in range(2, abs(i))):
            print(abs(i))
            break

