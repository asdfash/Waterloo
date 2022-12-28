import base64
import json
import random
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from sympy import mod_inverse, totient, randprime
from sympy.ntheory import factorint, isprime

def bytes2string(b):
    return base64.urlsafe_b64encode(b).decode('utf-8')

def string2bytes(s):
    return base64.urlsafe_b64decode(s.encode('utf-8'))

def gen_rsa_pk():
    bitlength = 512
    p = random.randint(2 ** (bitlength - 1), 2 ** bitlength)
    if not(isprime(p)): p = random.randint(2 ** (bitlength - 1), 2 ** bitlength)
    q = random.randint(2 ** (bitlength - 1), 2 ** bitlength)
    if not(isprime(q)): q = random.randint(2 ** (bitlength - 1), 2 ** bitlength)
    n = p * q
    e = random.randint(2 ** 128, 2 ** 129 - 1)
    return (n, e)

def gen_prime(bitlength):
    return randprime(2 ** (bitlength-1), 2 ** bitlength)

def do_encryption():
    # read the assignment file to be encrypted
    with open("assignment_in.pdf", 'rb') as fh:
        plaintext = fh.read()

    # generate the RSA public key
    (n, e) = gen_rsa_pk()

    # generate an AES key and convert it to an integer
    aes_key = random.randbytes(16)
    aes_key_int = int.from_bytes(aes_key, byteorder='big')
    
    # encrypt the AES key using RSA encryption
    c_1 = pow(aes_key_int, e, n)

    # pad the plaintext to a multiple of the block length
    padder = padding.PKCS7(128).padder() # 128 is the block size
    padded_data = padder.update(plaintext)
    padded_data += padder.finalize()
    
    # encrypt the plaintext using AES
    cipher = Cipher(algorithms.AES(aes_key), modes.ECB()).encryptor()
    aes_ct = cipher.update(padded_data) + cipher.finalize()

    # output the data in a JSON data structure for easy parsing
    output = {}
    output["n"] = n
    output["e"] = e
    output["c_1"] = c_1
    output["c_2"] = bytes2string(aes_ct)
    with open("encrypted_assignment.json.txt", 'w') as fh:
        fh.write(json.dumps(output))

def do_decryption():
    
    # Read and parse the JSON data structure
    with open("encrypted_assignment.json.txt", 'r') as fh:
        input = json.loads(fh.read())
    n = input["n"]
    e = input["e"]
    c_1 = input["c_1"]
    c_2 = string2bytes(input["c_2"])

    # TODO
    phi = totient(n)
    d = mod_inverse(e,phi)
    aes_key_int = pow(c_1,d,n)
    aes_key = aes_key_int.to_bytes((aes_key_int.bit_length()+7)//8,byteorder='big')
    cipher = Cipher(algorithms.AES(aes_key),modes.ECB())
    decryptor = cipher.decryptor()
    padded = decryptor.update(c_2)+decryptor.finalize()
    unpadder = padding.PKCS7(128).unpadder()
    plaintext = unpadder.update(padded)+unpadder.finalize()
    # write the decrypted assignment to a file
    with open("assignment_out.pdf", 'wb') as fh:
        fh.write(plaintext)

do_decryption()
