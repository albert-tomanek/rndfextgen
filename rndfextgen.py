import random

alphabet = "abcdefghijklmnopqrstuvwxyz"
numbers  = "1234567890"

def main():

    extlen = 3
    run = True

    while run:
        fext = "."

        for i in range(extlen):
            fext += random.choice(alphabet)

        print(fext, end="")

        if (input() == "q"):
            run = False

if __name__ == "__main__":
    main()
