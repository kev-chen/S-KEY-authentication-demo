#!/usr/bin/python3

from hashlib import sha256

class SKey:
    def __init__(self, secretKey):
        self.secretKey = secretKey

    def P(i):
        if i == 0: # P_0 is just the secret
            return self.secretKey
        else:
            return self.getHash(P(i-1))

    def getHash(bstr):
        # Get the byte string if it's not already bytes
        try:
            bstr = bstr.encode() 
        except:
            pass

        return sha256(bstr).hexdigest()
