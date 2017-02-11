"""
An implementation of the Vigenere Cipher that utilizes modular arithmetic.
Filename: vigenere.py
Author: Steven
Date Last Modified: 2/11/2017
Email: bouwkast@mail.gvsu.edu

"""


alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def encrypt_or_decrypt(key, message, mode='e'):
    key = key.upper()

    index = 0

    new_message = []

    for character in message:
        encoding = alphabet.find(character.upper())  # returns -1 if not found (punctuation)
        if encoding >= 0:
            if mode == 'e':
                encoding += alphabet.find(key[index])
            else:
                encoding -= alphabet.find(key[index])
            encoding %= len(alphabet)

            if character.isupper():
                new_message.append(alphabet[encoding])
            else:
                new_message.append(alphabet[encoding].lower())

            index += 1
            if index == len(key):
                index = 0
        else:
            new_message.append(character)

    return ''.join(new_message)


our_key = 'HELLO'
our_message = 'This is a test message to encrypt.'

print(our_message)

encrypted = encrypt_or_decrypt(our_key, our_message)


print(encrypted)

decrypted = encrypt_or_decrypt(our_key, encrypted, 'd')
print(decrypted)