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
from fractions import gcd


#Functions#
# calculate_e function takes in the user inputs for p and q and evaluates numbers for
# the exponent e that are relatively prime to (q-1)(p-1)
def calculate_e(x):
    for a in range(10000,100000,1110):
        if math.gcd(x,a) == 1:
            print(a, end=" , ")
    return

def calculate_gcd(x,y):
    a = 0
    if math.gcd(x,y) == 1:
        a = 1
    return a
    


#maincode#

""" Wnat the user to be able to click enter to step through and see how the math works for doing an RSA encryption 
    First i need to employ a simple RSA encryption to get full credit for the final project"""

# Step 1 RSA Key Generation
# the "reciever" selects two prime numbers p and q and an exponent e
# p, q, and e are the private key for the reciever
cstr = "Step 1 for RSA Encryption"
print('\n',cstr.center(40, '-'))
print("Say you and a frined want to encrypt a message and send it to one another using RSA ecrpytion methods")
print ("The reciever selects two prime number p and q and an exponent e")
print("Rules for picking P and q".center(40,'*'))
print("1. p and q must be large numbers","\n2. e must be relatively prime to (p-1)X(q-1)")

p = int(input("What would you like your p value to be: "))
q = int(input("What would you like your q value to be: "))
x = (p-1)*(q-1)

print("Based on your p and q values of ",p, " and ", q, "\nyou need to select a value for e that is relativley prime to","\nthe number (q-1)(p-1) which is: ",x)

#yn = input("Would you like to see some values of e that you can use? eneter Y for yes or N for no if you have your own e value in mind \nY for yes, N for no : ")
#YN = yn.upper()

#print (YN)
# while ((yn.upper() != 'Y')  or (yn.upper() != 'N')):
#     print("ooops please enter in either Y for yes or N for no")
#     yn = input("Would you like to see some values of e that you can use? eneter Y for yes or N for no if you have your own e value in mind \nY for yes, N for no : ")
#     if (yn == 'Y') or (yn == 'N'):
#         break

     
# if (yn == 'Y'):
#     calculate_e(x)
# elif((yn == 'N')or(yn == 'n')):
#     e = input("what would you like your e value to be: ")


# checks to make sure that the exponent e is relatively prime to (p-1)(q-1)
while True:
    e = int(input("what would you like your exponent value e to be? :"))
    checkNum = calculate_gcd(e,x)
    #print(checkNum)
    if checkNum == 1:
        break
    else:
        print("That number is not relatively prime to ",x," please try again")

print("Now that the reciever has their private keys p, q, and e")
print("The recievers public key can be computed")
print("The public key is a pair of integers, n = pq, and e")
n = p*q
print("n = ",n, " and e = ", e)

print("The one who wants to send the encrypted message can now take the public\n",
      "key values from the person who is recieving and encrypt a message\n")

print("To encrypt a message and create the cyphertext, the sender uses modular exponentiation\n")

text = input("enter a message that you would like to encrypt below\n")

text_test = ("Hello World")

#############################################################################
# The order in which I would like to go or am thinking of going is as follows:
# STRING -> ASCII -> HEX -> INT -> encrypt data -> decrpyt data -> INT -> HEX -> ASCII -> STRING
#############################################################################

#STEP 1 convert text_test into ASCII
text_test_ASCII = list(bytes(text_test, 'ascii'))
print("This is the message in ascii seperated by character in a list")
print(text_test_ASCII)

#STEP 2 convert ascii values in list into hex values and remove "0x" character from front of each list index
i = 0
for i in range (len(text_test_ASCII)):
    text_test_ASCII[i] = hex(text_test_ASCII[i])

print("This is the ascii message converted into hex values")
print(text_test_ASCII)

# formatting the list without the '0x'
print("removing all of the '0x' characters in front of each hex value")
for i in range(len(text_test_ASCII)):
    text_test_ASCII[i] = (text_test_ASCII[i]).lstrip("0x")

print(text_test_ASCII)

# concatenate all of the hex numbers in the list to be one long hex number 
print("converting to one large hex value")
hex_text_test = ''.join(text_test_ASCII)
print(hex_text_test)

#STEP 3 Convert the hex string into an integer that can do math
int_text_test = int(hex_text_test,16)
print("Converting Hex sting into a single integer")
print(int_text_test)

#STEP 4 RSA ENCRYPTION (this has been the hard part for me which is getting the decryption to work properly)
def mod_exponentiation(M, e, n):
    C = math.pow(M,e)%n
    return C

## NEED TO ADD A CHECK to see make sure n > M , n should be huge honestly
print(" ")
Cyper_text = mod_exponentiation(int_text_test,e,n)
print("This is the cyper text of the integer version of the original text")
print(Cyper_text)


#STEP 5 NEED TO GENERATE d which is the key to decryption, d is the inverse of e%(p-1)(q-1)
# there exists an integer k such that
# ed = 1 + k(p-1)(q-1)



