# rock, paper, scissors, lizard spock... (CLI)

from modules.utils import *
import sys, os, random, time

def main():
    while True:
        userInput = input("~/rpsls.py$ ").strip()
        uI_parts = userInput.split()
        cmd = uI_parts[0].lower()
        func = chkcmd(cmd)
        func()

if __name__ == "__main__":
    main()