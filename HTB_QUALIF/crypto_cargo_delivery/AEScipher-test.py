from crypto.Cipher import AES
import os
import random

BLOCK_SIZE = AES.block_size

iv = os.urandom(BLOCK_SIZE)

print(iv)