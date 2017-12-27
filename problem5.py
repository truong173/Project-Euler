#2520 is the smallest number that can be divided
#by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number
#that is evenly divisible by all of the numbers from 1 to 20?

#This feels like a shitty solution, because I'm not certain about my algorithm yet, but I'm gonn keep tinkering with it for a while

# WORKING SOLUTION FINALLY!

def lcm(max_num):
    
    #define a function to get the product of all value of an input list
    def product(input_list):
        p = 1
        for factor in input_list:
            p *= factor
        return p

    #get the true list from 11 to 21
    num_list = range(2, max_num + 1)

    #separate the primes from the true list
    primes = [x for x in num_list if all(x % y != 0 for y in range(2, x))]

    #separate the non-prime numbers from the true list
    non_primes = [z for z in num_list if z not in primes]

    divs = []

    for np1 in non_primes:
        if product(primes) % np1 != 0:
            divs = divs + [div for div in primes if np1 % div == 0 and div not in divs]

    multi = 1

    for d in divs:
        for np2 in non_primes:
            for power in range(1, 10):
                if ( product(primes) * multi ) % np2 == 0:
                    break
                else:
                    if np2 < d ** power:
                        for reverse in range(1, power):
                            multi = int(multi / (d ** reverse))
                        break
                    else:
                        multi = multi * (d ** power)
                        pass

    result = product(primes) * multi
    return result
