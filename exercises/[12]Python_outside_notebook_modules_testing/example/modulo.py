import sys
import utils

def main():
    print(utils.somma_vettore(sys.argv[1:]))
    print(utils.controlla_email("simone@gmail.com"))
    print(utils.controlla_email("@gmail.it"))

if __name__ == '__main__':
    main()