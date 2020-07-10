import base64
import urllib.parse
import hashlib

def xor_encrypt(plaintext, key):
    return "".join([chr(ord(c1) ^ ord(c2)) for (c1,c2) in zip(plaintext, key)])

def xencode(plaintext):
    key=plaintext
    pass2=str(key)
    pass2=hashlib.sha256(pass2.encode()).hexdigest()
    return pass2
  
def xdecode(pass3):
    key=pass3
    pass2=str(key)
    pass2=hashlib.sha256(pass2.encode()).hexdigest()
    pass2=bytes(pass2,encoding = "utf-8")
    return pass2
