#2520 is the smallest number that can be divided
#by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number
#that is evenly divisible by all of the numbers from 1 to 20?

#This feels like a shitty solution, because I'm not certain about my algorithm yet, but I'm gonn keep tinkering with it for a while

import math

#input number
max_num = int(input())

#define a function to get the product of all value of an input list
def product(input_list):
    p = 1
    for i in input_list:
        p *= i
    return p

#simplify the solution by using the lcm from 1 to 10 already provided in the problem
num = 2520
placeholder = 1

#get the true list from 11 to 21
true_list = range(11, max_num + 1)

#separate the primes from the true list
primes = [x for x in true_list if all(x % y != 0 for y in range(2, x))]

#get the product of all primes and the lcm from 1 to 10
products = product(primes) * num

#separate the non-prime numbers from the true list
rest = [i for i in true_list if i not in primes]

#separate the non-prime numbers that is not a factor of num
others = [o for o in rest if num % o != 0]

for n in others:
	while placeholder < math.sqrt(n):
		if products % placeholder == 0:
			placeholder = placeholder + 1
		print(placeholder)
			
result = products * placeholder
print(products)
