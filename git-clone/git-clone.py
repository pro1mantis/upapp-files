#bin/bash/  /usr/bin/python
import random
import os
import sys

git = (random.randint(-1,-1))


print("Type -1 to run!")
while True:
        odg = input("Type command:")
        try:
            odg = int(odg)
            if odg == git:
                print("I clone some folders and files from git repo...")
                os.system('sudo apt update')
                os.system('sudo apt install git')
                os.system('git clone https://github.com/pro1mantis/UPapp')
                break
        except ValueError:
            print("That isn't a command!")
