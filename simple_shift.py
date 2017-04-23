"""
This program demonstrates a very simple implementation of a shift cipher
Filename: simple_shift.py
Author: Steven
Date Last Modified: 4/23/2017
Email: bouwkast@mail.gvsu.edu

"""

alphabet_size = 1114111  # for simplicity assuming unicode alphabet

message = input('Please enter a message to decrypt:')

amount = int(input('Please enter an amount to shift the message:'))
if amount > alphabet_size:
    print('too large shift value')
    exit(1)

print('Encrypting message: ')

encrypted = ''

for char in message:
    encrypted += chr((ord(char) + amount) % alphabet_size)

print('Encrypted message: ' + encrypted)



print('\nDecrypting message:')
decrypted = ''

for char in encrypted:
    decrypted += chr((ord(char) - amount) % alphabet_size)

print('Decrypted message: ' + decrypted)