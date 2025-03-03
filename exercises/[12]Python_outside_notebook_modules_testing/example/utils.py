import re

def somma_vettore(vettore):
    somma = 0
    for valore in vettore:
        somma += int(valore)
    return somma

'''
controlla se una email e' in forma 
nome@dominio.com
senza numeri
'''
def controlla_email(s):
    occ = re.match('\w+@\w+\.com', s)
    return occ != None