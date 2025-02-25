import os

def ksa(key): 
    key_length = len(key)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i] 
    return S

def gen_key(length):
    key = os.urandom(length)
    return key

def prga(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]  
        K = S[(S[i] + S[j]) % 256]
        yield K 

def rc4_encrypt(key, plaintext):
    S = ksa(key)
    keystream = prga(S)
    encrypted = bytearray()
    for byte in plaintext:
        encrypted.append(byte ^ next(keystream))
    return encrypted

def rc4_decrypt(key, ciphertext):
    return rc4_encrypt(key, ciphertext) 
