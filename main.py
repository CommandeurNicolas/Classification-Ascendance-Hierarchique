# argecho.py
import sys
import point
data = []

if __name__ == "__main__":
    if(len(sys.argv) < 2):
        print('usage: python main.py [file]')
        exit(0)
    file = open(sys.argv[1])
    for line in file:
        s = line.split()
        data.append(point.Point(s[0],s[1],s[2]))
    print(data)
    