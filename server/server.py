#!/usr/bin/python3
from skey import SKey
import os

class Server:
    def __init__(self):
        self.skey = SKey()
        self.keyFileName = 'skeykeys'
        self.loggedIn = False

    def keyinit(self, secret, n):
        self.setCurrentPassword(self.skey.P(n, secret))
        print("Success, you may now log in with one time password")

    '''
        Updates the skeykeys file with a new password
    '''
    def setCurrentPassword(self, newPassword):
        with open(self.keyFileName, 'w+') as file:
            file.write(newPassword)

    '''
        Reads the current password stored in skeykeys
    '''
    def getCurrentPassword(self):
        try:
            with open(self.keyFileName, 'r') as file:
                return file.readline().strip()
        except:
            return None


    '''
        @param passwordAttempt SHOULD = P_i
        self.currentPassword = P_i+1 = H(P_i)

        If passwordAttempt truly equals P_i, then its Hash should
        match self.currentPassword. If that is the case, then 
        we set self.currentPassword to passwordAttempt and return true
    '''
    def authenticate(self, passwordAttempt):
        currentPassword = self.getCurrentPassword()
        if currentPassword != None:
            hashed = self.skey.getHash(passwordAttempt)
            if (hashed == currentPassword):
                self.setCurrentPassword(passwordAttempt)
                return True
        else:
            print("Use command 'keyinit <secret>'to setup one-time passwords")
            
        return False     


    '''
        Issues a challenge before logging in
    '''
    def login(self):
        if not self.loggedIn:
            passwordAttempt = input('S/KEY password: ')
            if self.authenticate(passwordAttempt):
                print("Login successful")
                self.loggedIn = True
            else:
                print("Login failed")
        else:
            print("Already logged in")

    def logout(self):
        if self.loggedIn:
            self.loggedIn = False
            print("Logged out")
        else:
            print("Not logged in")
        


