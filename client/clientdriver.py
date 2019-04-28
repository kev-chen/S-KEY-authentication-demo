#!/usr/bin/python3

from client import Client
import os


def main():
    client = Client()

    while(True):
        # Get command - keyinit, login, logout, or quit
        inp = input("> ")
        if inp.strip()[:len('keyinit')] == 'keyinit':
            try:
                spaceIndex = inp.index(' ')
                password = inp[spaceIndex+1:]
                if password == '':
                    throw
                client.keyinit(password, 100)
            except Exception as e:
                print(e)
                print("Usage: keyinit <secret>")
        elif inp.strip() == 'new':
            print(f'New one-time Password:\n{client.requestNewPassword()}')
        elif inp.strip() == 'current':
            print(f'Current one-time Password:\n{client.getCurrentPassword()}')
        elif inp.strip() == 'quit':
            quit()
        elif inp.strip() == 'clear':
            if os.path.exists('keyindex'):
                os.remove('keyindex')
            if os.path.exists('keys'):
                os.remove('keys')
        else:
            print("Command not recognized. Available commands: keyinit, new, current, clear, quit")

if __name__ == "__main__":
    main()