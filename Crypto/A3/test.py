import os
import base64
import getpass
import sys
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms
from cryptography.hazmat.primitives.ciphers.modes import CBC

print()
h = hashes.Hash(hashes.SHA256())
h.update(b'0')
k=h.finalize()
print(k)
print(k[0:16])
print(len(k))