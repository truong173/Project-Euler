#2520 is the smallest number that can be divided
#by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number
#that is evenly divisible by all of the numbers from 1 to 20?

#This feels like a shitty solution, because I'm not certain about my algorithm yet, but I'm gonn keep tinkering with it for a while

# WORKING SOLUTION FINALLY!

#input number
max_num = int(input("small number pls: "))

#define a function to get the product of all value of an input list
def product(input_list):
    p = 1
    for il in input_list:
        p *= il
    return p

#get the true list from 11 to 21
true_list = range(2, max_num + 1)

#separate the primes from the true list
primes = [x for x in true_list if all(x % y != 0 for y in range(2, x))]

#separate the non-prime numbers from the true list
rest = [z for z in true_list if z not in primes]

divs = []

for r in rest:
    if product(primes) % r != 0:
        divs = divs + [div for div in primes if r % div == 0 and div not in divs]

multi = 1

for d in divs:
    for r in rest:
        for power in range(1, 10):
            if ( product(primes) * multi ) % r == 0:
                break
            else:
                if r < d ** power:
                    for reverse in range(1, power):
                        multi = int(multi / (d ** reverse))
                    break
                else:
                    multi = multi * (d ** power)
                    pass

result = product(primes) * multi
print(result)
