import math
import random

p = 41
q = 61

private_key = (p-1)*(q-1)

public_key = p*q

magic_power = random.randrange(private_key)
while math.gcd(private_key, magic_power) != 1:
    magic_power = random.randrange(private_key)

def cipher(plain):
    return (plain ** magic_power) % public_key

def decipher(encrypted):
    inverse = None
    for i in range(private_key):
        for j in range(private_key):
            if magic_power * i == j * private_key + 1:
                inverse = i
                break
    print('inverse', inverse)
    return (encrypted ** inverse) % public_key


plain_num = 1080
encrypted_num = cipher(plain_num)
print(encrypted_num, magic_power)

print(decipher(encrypted_num))

