# argecho.py
import sys

if __name__ == "__main__":
    if(len(sys.argv) < 2):
        print('usage: python main.py [file]')
        exit(0)
    file = open(sys.argv[1])
    for line in file:
        print(line,end='')