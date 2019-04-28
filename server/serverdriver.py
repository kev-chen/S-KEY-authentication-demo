#!/usr/bin/python3

from server import Server
import os

def main():
    server = Server()

    while(True):
        # Get command - keyinit, login, logout, or quit
        inp = input("> ")
        if inp.strip()[:len('keyinit')] == 'keyinit':
            try:
                spaceIndex = inp.index(' ')
                password = inp[spaceIndex+1:]
                if password == '':
                    throw
                server.keyinit(password, 100)
            except Exception as e:
                print(e)
                print("Usage: keyinit <secret>")
        elif inp.strip() == 'login':
            server.login()
        elif inp.strip() == 'logout':
            server.logout()
        elif inp.strip() == 'quit':
            quit()
        elif inp.strip() == 'clear':
            if os.path.exists('skeykeys'):
                os.remove('skeykeys')
        else:
            print("Command not recognized. Available commands: keyinit, login, logout, clear, quit")

if __name__ == "__main__":
    main()