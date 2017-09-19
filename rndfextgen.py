#!/usr/bin/python3
import random
import sys

help_text = """
Random file extension generator

Switches:
  --help     = Display this help text and exit
  -l=n       = Set the extension length to n.
  --alphanum = Use alphanumerical characters (including numbers)
  --capitals = print the extension in upper case

Usage:
  Press return to keep generating new extensions.
  To quit, type 'q' before pressing return.
"""

alphabet = "abcdefghijklmnopqrstuvwxyz"
numbers  = "1234567890"

def main():
    # Check if the '--help' option is selected
    if ("--help" in sys.argv) or ("-h" in sys.argv):
        print(help_text)
        return

    # Create the array of legal characters
    if ("--alphanum" in sys.argv):
        legal_chars = list(alphabet) + list(numbers)
    else:
        legal_chars = list(alphabet)
    
    extlen = 3 if ("-l" not in [arg.split('=')[0] for arg in sys.argv]) else int(next(arg.split('=')[-1] for arg in sys.argv if arg.split('=')[0] == "-l"))
    
    run = True

    while run:
        fext = "."

        for i in range(extlen):
            fext += random.choice(legal_chars)
        
        if ("--capitals" in sys.argv):
            fext = fext.upper()
        
        print(fext, end="")

        if (input() == "q"):
            run = False

if __name__ == "__main__":
    main()
