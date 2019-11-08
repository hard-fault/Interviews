import collections
import math
from sys import stdin, stdout

def primeFactors(n):           
    primes = [] 
    while n % 2 == 0: 
        primes.append(2) 
        n = n / 2
    for i in range(3,int(math.sqrt(n))+1,2):  
        while n % i== 0: 
            primes.append(i) 
            n = n / i 
    if n > 2: 
        primes.append(n)
    return primes

def getPrimes(cipher):
    primes = []
    for i in range(len(cipher)):
        factors = primeFactors(cipher[i])
        if i == 0:
            primes.extend(factors)
        elif i == 1:
            second = list(set(primes).intersection(factors))[0]
            if primes[1] != second:
                primes[0], primes[1] = primes[1], primes[0]
            factors.remove(second)
            primes.extend(factors)
        else:
            factors.remove(primes[-1])
            primes.extend(factors)

    return primes

t = input()
index = 1
while index <= t:
    #n,l = stdin.readline().split()
    n,l = map( int, stdin.readline().rstrip().split() )
    cipher = []
    #cipher=list(map(int,input().split()))
    cipher = [int(x) for x in stdin.readline().rstrip().split()]
    primes = getPrimes(cipher)

    primesCopy = sorted(list(set(primes)))
    encodingDict = {}
    start = 65
    for prime in primesCopy:
        encodingDict[prime] = chr(start)
        start += 1

    #Decode
    result = ""
    for prime in primes:
        result += encodingDict[prime]

    print ("Case #{}: {}".format(index, result))
    index +=1