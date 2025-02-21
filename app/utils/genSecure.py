# -*- coding: utf-8 -*-
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
import os
import sys
import utils.params as const

def generate_key():
    return os.urandom(32)

def encrypt(text, key):
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(pad(text.encode(), AES.block_size))
    return base64.b64encode(iv + encrypted).decode()

def decrypt(encrypted_text, key):
    encrypted_data = base64.b64decode(encrypted_text)
    iv = encrypted_data[:16]
    encrypted_text = encrypted_data[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(encrypted_text), AES.block_size)
    return decrypted.decode()

if __name__ == "__main__":
    command = sys.argv[1]
    key = bytes.fromhex(const.key)

    if len(sys.argv) == 2:
        if command == "getKey":
            print(key.hex())
    elif len(sys.argv) == 3:
        message = sys.argv[2]
        if command == "encrypt":
            print(encrypt(message, key))
        elif command == "decrypt":
            print(decrypt(message, key))
        else:
            print("Invalid Input")

    else:
        print("Invalid Input")
        sys.exit(1)

    
   