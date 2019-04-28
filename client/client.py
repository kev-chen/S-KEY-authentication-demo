#!/usr/bin/python3

from skey import SKey

class Client:
    def __init__(self):
        self.skey = SKey()
        self.passwordList = list()

        try:
            with open('keys', 'r') as file:
                password = file.readline()
                while password != '':
                    self.passwordList.append(password.strip())
                    password = file.readline()
        except:
            pass

    def keyinit(self, secret, n):
        with open('keys', 'w+') as file:
            self.passwordList.clear()
            for i in range(1, n):
                P_i = self.skey.P(i, secret)
                file.write(P_i + '\n')

                self.passwordList.append(P_i)

        self.setPasswordIndex(len(self.passwordList))
        print("Success, you may now generate one-time passwords")

    def setPasswordIndex(self, i):
        with open('keyindex', 'w+') as file:
            file.write(str(i))
    
    def getPasswordIndex(self):
        try:
            with open('keyindex', 'r') as file:
                index = int(file.readline().strip())
                return index if index >= 0 else None
        except:
            return None
        
    def requestNewPassword(self):
        try:
            self.setPasswordIndex(self.getPasswordIndex() - 1)
            newPassword = self.getCurrentPassword()
            
            return newPassword
        except Exception as e:
            print(e)
            print("No passwords. Use command keyinit <secret> to initialize one-time passwords")
            return None

    def getCurrentPassword(self):
        try:
            return self.passwordList[self.getPasswordIndex()]
        except:
            if self.getPasswordIndex() != len(self.passwordList):
                print("No passwords. Use command keyinit <secret> to initialize one-time passwords")
            else:
                print("No current password yet, request a new one.")

            return None

