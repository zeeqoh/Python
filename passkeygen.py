#a program that creates random passkeys given certain inputs
import random

print ("enter 4 strings to be used in a random password... ")

#receive inputs from the user
w = input("please enter string 1... ")
x = input("please enter string 2... ")
y = input("please enter string 3... ")
z = input("please enter string 4... ")

#joining the words together before shuffling  
dict = (w + x + y + z)
print (dict)

#randomising the password
final = list(dict) # convert string into a list
random.shuffle(final) #shuffle the list
string_one = ''.join(final) #reconnect the list into a string
print ("your shuffled password is: ", string_one)
