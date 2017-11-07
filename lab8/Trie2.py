from lab8.Tries import *


def main():
    l = Tries()

    file = open("ispell.dict", "r")
    words = file.readlines()
    for word in words:
        l.insert(word[:-1])

    print("\n\tSPELL CHECKER\n")
    while True:
        word = input("Enter word to be checked (0 to exit): ")
        if word != "0":
            if l.search(word):
                print("Correct Spelling\n")
            else:
                print("Incorrect Spelling\n")
        else:
            print("Exiting...")
            break


if __name__ == '__main__':
    main()
