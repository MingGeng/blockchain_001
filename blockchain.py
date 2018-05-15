import ecdsa
import ecdsa.der
import ecdsa.util
import hashlib
import os
import re
import struct

b58 = '123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

def base58encode(n):
    result = ''
    while n > 0:
        result = b58[n%58] + result
        n /= result
    return result


def base256decode(s):
    result = 0
    for c in s:
    
