import sys

def main():
    print(sys.argv)
    somma = 0
    for arg in sys.argv[1:]:
        somma += int(arg)
    print(somma)

if __name__ == '__main__':
    main()