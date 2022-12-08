##################################################################
#Author: Anton Vandenberge
#Date 12/5/2022
#Description:
#   Final discrete mathematics project, Implementing
#   an RSA encryption method to encrypt the users message and 
#   and then decrypt the same message
#Bonus: 
##################################################################
#Imports#
from typing import Tuple
import sympy

#Functions#
def extendedEclid(a: int, b: int) -> Tuple[int, int, int]:
    """Returns the GCD of a and b and the Bezout Coeffiecients."""
    if b == 0:
        return(a,1,0)
    q,r = divmod(a,b)
    g,s,t = extendedEclid(b,r)
    #print("g = :",g)
    #print("t = :",t)
    #print("last value = :",s-q*t)
    return g,t, s-q*t

def linearCongruence(a: int, b: int, mod: int):
    g,s,t = extendedEclid(a, mod)
    if g != 1:
        #GCD != 1
        return None
    else: #GCD = 1 Bezout's identity applies ax = b(mod m)
        # if GCD is 1, and s = a' and t = m' (' means inverse) from extended Euclid function
        # x is congruent sb (mod m)
        # x = sbmod(m)
        x = (s*b)%mod
        #print('d =',x)
        #print('s =',s)
        return x,s

def mod_exponent(b: int, n: int, m:int) ->int:
    """Computes b to the n mod m"""
    if n < 0: raise ValueError('n <= 0')
    if m < 1: raise ValueError('m < 1')
    power, square, exp = 1, b%m, n
    while exp > 0:
        if exp % 2 == 1:
            power = (power * square) % m
        square = (square*square)%m
        exp = exp // 2
    return power

#Create the private and public keys 
