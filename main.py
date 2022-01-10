import sys
from package import *

cluster = Cluster()
if __name__ == "__main__":
    if(len(sys.argv) < 2):
        print('usage: python main.py [file]')
        exit(0)
    file = open(sys.argv[1])

    for line in file:
        s = line.split()
        p = Point(s[0], int(s[1]), int(s[2]))
        cluster.add(p)
    cluster.show()
    print(cluster.min(Point("g",7,13)))
    print(cluster.max(Point("g",7,13)))
    exit(0)
1