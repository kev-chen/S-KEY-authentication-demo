#!/usr/bin/python3

from hashlib import sha256

class SKey:
    def P(self, i, secretKey):
        if i == 0: # P_0 is just the secret
            return secretKey
        else:
            return self.getHash(self.P(i-1, secretKey))

    def getHash(self, bstr):
        # Get the byte string if it's not already bytes
        try:
            bstr = bstr.encode() 
        except:
            pass

        return sha256(bstr).hexdigest()
