import random

def worker(x):
    print "entered worker"
    1/0

def main(x):
    print "entered main"
    worker(x)

if __name__ == "__main__":
    main(random.random())
