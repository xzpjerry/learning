# !/usr/bin/engv python3
import random
'''
	Substitution encryptor and decryptor. 

	Author: Zhipeng Xie

	Credits: 'python.org' official document

	Using substitution method to encrypt inputed
	text and then print the decrypted text.
'''


def get_alphabet(pos=None):
    '''
    (opt number) -> list[number] or list[]

    It's used to get certain character in alphabet
    or whole alphabet list.
    Inputing the position number,
    output the character of that position in the alphabet

    >>> print(get_alphabet())
    'abcdefghijklmnopqrstuvwxyz'
    >>> print(get_vowel(0))
    'a'
    '''
    result = ''
    for i in range(97, 97 + 26):
        result = result + chr(i)
    if pos == None:
        return result
    return result[pos]


def substitutionEncrypt(plaintext, the_key):
    '''
    (string, string) -> string

    First, eliminate any space in the text and
    then lower every character in the text.
    Inputing plaintext and generated key and
    using simple substitution method to regenerate
    string.

    >>> print('abcdefg', 'ihxudkbjrywzqvanpfctogmsle')
    'ihxudkb'
    >>> print('aaaa', 'ihxudkbjrywzqvanpfctogmsle')
    'iiii'
    '''
    plaintext = ''.join(plaintext.split())
    plaintext = plaintext.lower()
    ciphertext = ''
    alphabet = get_alphabet()
    for ch in plaintext:
        index = alphabet.find(ch)
        ciphertext = ciphertext + the_key[index]
    return ciphertext


def substitutionDecrypt(ciphertext, the_key):
    '''
    (string, string) -> string

    To do the Decrypting procedure.
    Inputing encrypted string and generated key,
    using reverse method to regenerate the original
    string.

    >>> print('ihxudkb', 'ihxudkbjrywzqvanpfctogmsle')
    'abcdefg'
    >>> print('iiii', 'ihxudkbjrywzqvanpfctogmsle')
    'aaaa'
    '''
    plaintext = ''
    alphabet = get_alphabet()
    for ch in ciphertext:
        index = the_key.find(ch)
        plaintext = plaintext + alphabet[index]
    return plaintext


def genKeyFromPass(psw):
    '''
    (number or string) -> string

    To generate random Key by the seed user
    put in.
    Inputing anything to become the seed of 
    random number generator, using a while loop
    to let every number(from 0 to 25) only appear
    exactly one time, this function can generate a
    controllable key string.(If the psw didn't change, 
    outputed key wouldn't change, since the seed
    is not changed.)

    >>> print(genKeyFromPass('test'))
    'ihxudkbjrywzqvanpfctogmsle'
    >>> print(genKeyFromPass(123))
    'yhzsjmqrftvoudplgewinaxkcb'
    '''
    key = ''
    exception = []
    random.seed(psw)
    for i in list(range(26)):
        tmp_num = random.randrange(0, 26)
        while tmp_num in exception:
            tmp_num = random.randrange(0, 26)
        key = get_alphabet(tmp_num) + key
        exception.append(tmp_num)
    return key

    '''
	I have found a better way to create random key, using the
	random function. 

def removeDupes(original_psw):
	new_psw = ''
	for ch in original_psw:
		if ch not in new_psw:
			new_psw = new_psw + ch
	return new_psw

def removeMatches(original_str, exception_str):
	new_str = ''
	for ch in original_str:
		if ch not in exception_str:
			new_str = new_str + ch
	return new_str
	'''

plaintext = raw_input('plaintext: ')
the_key = genKeyFromPass('test')
encryptedtext = substitutionEncrypt(plaintext, the_key)
decryptedtext = substitutionDecrypt(encryptedtext, the_key)
print('You have entered: ' + plaintext)
print('The key is: ' + the_key)
print('Encrypted_text is: ' + encryptedtext)
print('Decrypted_text is: ' + decryptedtext)
