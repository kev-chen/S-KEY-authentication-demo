#!/usr/bin/python3


class User:

    def __init__(self, secretKey, n):
        self.skey = SKey(secretKey)
        self.n = n
        self.currentPassword = ''

    '''
        Returns a list of passwords generated via SKey
        Sets self.currentPassword to P_n
    '''
    def computePasswords():
        oneTimePasswords = list()
        for i in range(0, self.n):
            oneTimePasswords.append(self.SKey.P(i))
        
        self.currentPassword = oneTimePasswords[-1]
        return oneTimePasswords


    '''
        @param passwordAttempt SHOULD = P_i
        self.currentPassword = P_i+1 = H(P_i)

        If passwordAttempt truly equals P_i, then its Hash should
        match self.currentPassword. If that is the case, then 
        we set self.currentPassword to passwordAttempt and return true
    '''
    def validatePassword(passwordAttempt):
        if self.currentPassword != '':
            if (self.SKey.getHash(passwordAttempt) == passwordAttempt):
                self.currentPassword = passwordAttempt
                return true
        
        return false            


