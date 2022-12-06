##################################################################
#Author: Anton Vandenberge
#Date 12/5/2022
#Description:
#   Final discrete mathematics project, Implementing
#   an RSA encryption method allowing the user to step through
#   and understand the process of creating the Key values
#   and how to decrypt an encrypted message
#Bonus: 
##################################################################
#Imports#
import math


#Functions#
# calculate_e function takes in the user inputs for p and q and evaluates numbers for
# the exponent e that are relatively prime to (q-1)(p-1)
def calculate_e(x):


    return

#maincode#

""" Wnat the user to be able to click enter to step through and see how the math works for doing an RSA encryption 
    First i need to employ a simple RSA encryption to get full credit for the final project"""

# Step 1 RSA Key Generation
# the "sender" selects two prime numbers p and q and an exponent e
# p, q, and e are the private key for the sender
cstr = "Step 1 for RSA Encryption"
print('\n',cstr.center(40, '-'))
print ("The sender selects two prime number p and q and an exponent e")
print("Rules for picking P and q".center(40,'*'))
print("1. p and q must be large numbers","\n2. e must be relatively prime to (p-1)X(q-1)")

p = int(input("What would you like your p value to be: "))
q = int(input("What would you like your q value to be: "))
x = (p-1)*(q-1)

print("Based on your p and q values of ",p, " and ", q, "\nyou need to select a value for e that is relativley prime to","\nthe number (q-1)(p-1) which is: ",x)

yn = input("Would you like to see some values of e that you can use? eneter Y for yes or N for no if you have your own e value in mind \nY for yes, N for no : ")

if ((yn == 'Y') or (yn == 'y')):
    calculate_e(x)
elif((yn == 'N')or(yn == 'n')):
    e = input("what would you like your e value to be: ")




