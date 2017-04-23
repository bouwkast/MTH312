"""
Implementation of the Affine Shift Cipher
Requires a translation table - in this case a list of the alphabets ordering
Utilizes the function: f(x) = (a * x + b)
Apply function modulo m to each


Filename: affine_shift.py
Author: Steven
Date Last Modified: 1/22/2017
Email: bouwkast@mail.gvsu.edu

"""


def gen_default_translation():
    """
    Return the default translation table for use in the cipher.
    :return: a dictionary containing the translation table
    """
    char_list = list('abcdefghijklmnopqrstuvwxyz')
    alpha_table = {}
    index = 0
    for char in char_list:
        alpha_table[char] = index
        index += 1
    return alpha_table


def number_encoding(plaintext, translation_table):
    """
    Return the encoded numbers that represents the plaintext
    :param plaintext: is the string to encode
    :param translation_table: is the table to encode the plaintext with
    :return: a list containing the encoded plaintext as ints
    """
    to_encode = list(plaintext.lower())
    encoded = []
    for char in to_encode:
        if not char.isalpha():
            exit(1)  # TODO do
        else:
            encoded.append(translation_table[char])

    print(encoded)
    return encoded


def affine_shift_enc(a, b, m, plaintext, translation):
    """
    Encrypt the plaintext using the affine shift cipher.
    f(x) = a * x + b % m
    Requirement: a and m must be at least coprime
    :param a: is any non-zero integer
    :param b: is any integer
    :param m: is the length of the translation table
    :param plaintext: is the string we are encrypting
    :param translation: is the dictionary containing the table
    :return: the encrypted string
    """
    if inverse_mod(a, m) is None:
        print('a and m must be coprime. Exiting.')
        exit(1)
    encoded = number_encoding(plaintext, translation)
    output_nums = []
    #  First change encoded to proper numbers with function
    for num in encoded:
        result = (a * int(num) + b) % m
        output_nums.append(result)
    print(output_nums)
    encrypted = ''
    for encoded_num in output_nums:
        for key in translation:
            if encoded_num == translation[key]:
                encrypted += key
    return encrypted


def affine_shift_dec(a, b, m, ciphertext, translation):
    """
    Return the decrypted cipher text using the affine shift cipher
    :param a: is any non-zero integer
    :param b: is any integer
    :param m: is the length of the translation table
    :param ciphertext: is the string we are decrypting
    :param translation: is the translation table to use (dictionary)
    :return: a string containing the decrypted text
    """
    encoded = number_encoding(ciphertext, translation)
    output_nums = []

    mod_mult = inverse_mod(a, m)

    for num in encoded:
        output_nums.append(mod_mult * (num - b) % m)

    decrypted = ''
    for encoded_num in output_nums:
        for key in translation:
            if encoded_num == translation[key]:
                decrypted += key
    return decrypted


def inverse_mod(a, m):
    """
    Calculate what the modular multiplicative inverse of a mod m
    modular inverse of a mod m is a^-1 such that:
    a*a^-1 CONGRUENT 1 (mod m)
    :param a: is any non-zero integer
    :param m: is the length of the translation table
    :return: an int which is the modular multiplicative inverse, otherwise None
    """
    for i in range(1, m):
        if (m * i + 1) % a == 0:
            return m * i + 1  # a
    return None


table = gen_default_translation()

plaintext = 'CRYPTOGRAPHY'

ciphertext = affine_shift_enc(11, 0, len(table), plaintext, table)

print(plaintext)

print(ciphertext)

print("Affine Shift the Ciphertext.")

# ciphertext_shift = affine_shift_dec(11, 0, len(table), ciphertext, table)
ciphertext_shift = affine_shift_enc(19, 0, len(table), ciphertext, table)
print(ciphertext_shift)

print(table)
