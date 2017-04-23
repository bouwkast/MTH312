"""Implementation of the simple substitution cipher utilizing the
secrets module to provide a cryptographically secure key.
This doesn't mean it is a necessarily strong cipher.

File Name: simple_sub.py
Author: Steven Bouwkamp
Date Last Modified: 1/22/2017
Email: bouwkast@mail.gvsu.edu
"""
import secrets


def generate_cipher_alpha():
    """
    Take the standard alphabet and rearrange its order securely.
    :return: the key in dictionary format (ciphered alphabet)
    """
    pre_random = list('abcdefghijklmnopqrstuvwxyz')
    reference = list('abcdefghijklmnopqrstuvwxyz')
    ciphered = {}
    index = 0
    while len(pre_random) > 0:
        charac = secrets.choice(pre_random)
        ciphered[reference[index]] = charac
        pre_random.remove(charac)
        index += 1
    return ciphered


def encrypt(plaintext, key_as_dict):
    """
    Encrypts some given plaintext with the given key using the simple
    substitution cipher.
    :param plaintext: is the string to encrypt
    :param key_as_dict: is the key to use
    :return: the encrypted string
    """
    to_encrypt = plaintext.lower()
    encrypted = ''
    for char in to_encrypt:
        if not char.isalpha():
            encrypted += char
        else:
            encrypted += key_as_dict[char]
    return encrypted.upper()


def decrypt(ciphertext, key_as_dict):
    """
    Decrypt the ciphertext using the given key with the simple
    substitution cipher.
    :param ciphertext: is the encrypted string to decrypt
    :param key_as_dict: is the key to decrypt with
    :return: the decrypted string
    """
    to_decrypt = ciphertext.lower()
    decrypted = ''
    for char in to_decrypt:
        if not char.isalpha():
            decrypted += char
        else:
            for key in key_as_dict:
                if char == key_as_dict[key]:
                    decrypted += key
    return decrypted.lower()


def format_key(key_as_dict):
    """
    Return the string representation of the key.
    :param key_as_dict: the dictionary that contains the key
    :return: the string containing the key
    """
    cipher_key = ''
    for key in key_as_dict:
        cipher_key += key_as_dict[key]
    return cipher_key.upper()


plain_alpha = 'abcdefghijklmnopqrstuvwxyz'
cipher_alpha = generate_cipher_alpha()

print('Plaintext alphabet: \t', plain_alpha)
print('Ciphertext alphabet: \t', format_key(cipher_alpha))

# plaintext = '\nFor me, it is far better to grasp the Universe as it really is than' \
#             ' to persist in delusion, however satisfying and reassuring.'
plaintext = '\n Hello'
print("Plaintext: ", plaintext)

ciphertext = encrypt(plaintext, cipher_alpha)
print('\nCiphertext: ', ciphertext)

decrypted_str = decrypt(ciphertext, cipher_alpha)
print('Decrypted: ', decrypted_str)
