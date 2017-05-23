import argparse
import copy
import math
import pickle
import random
from itertools import combinations

def gcd(a, b):
    a = abs(a)
    b = abs(b)
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

def coPrime(t):
    for i in range(int(math.sqrt(t)),2,-1):
        if gcd(i,t) ==1:
            return i

def extendedEuclid(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = extendedEuclid(b % a, a)
        return g, x - (b // a) * y, y

def invModulo(e, t):
    linearCombination = extendedEuclid(e, t)
    return linearCombination[1] % t

def int2baseTwo(x):
    """x is a positive integer. Convert it to base two as a list of integers
    in reverse order as a list."""
    # repeating x >>= 1 and x & 1 will do the trick
    assert x >= 0
    bitInverse = []
    while x != 0:
        bitInverse.append(x & 1)
        x >>= 1
    return bitInverse

def modExp(m, e, n):
    """returns m ** e (mod n)"""
    assert e >= 0
    assert n >= 0
    base2D = int2baseTwo(e)
    base2DLength = len(base2D)
    modArray = []
    result = 1
    for i in range(1, base2DLength + 1):
        if i == 1:
            modArray.append(m % n)
        else:
            modArray.append((modArray[i - 2] ** 2) % n)
    for i in range(0, base2DLength):
        if base2D[i] == 1:
            result *= base2D[i] * modArray[i]
    return result % n

def main():
    message = raw_input("Please enter the message to be encrypted: ")
    enc = []
    for ch in range(len(message)):
        enc.append(ord(message[ch]))
    enc_n, enc_e = input('Please provide the encryption public key n, e: ')
    for i in range(len(enc)):
        enc[i-1] = modExp(enc[i-1], enc_e, enc_n)
    print 'The encrypted message is: '
    for i in range(len(enc)):
        print(enc[i-1])
    
main()
