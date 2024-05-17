#MASTER FUNCTION CONCEPT
#1
v=input('entrer une phrase: ')
def envès(mot):
    return mot[::-1]

#test
mo_envès = envès(v)
print(mo_envès)  
#2
import random
import string

def jenere_kod_aleyatwa(n):
    kod = ''.join(random.choices(string.ascii_lowercase, k=n))
    return kod

# test
n = 8
kod_aleyatwa = jenere_kod_aleyatwa(n)
print(kod_aleyatwa)
#3
import random
import string

def jenere_kod_aleyatwa(n):
    lèt_alfabetik = string.ascii_lowercase
    kod = ''.join(random.sample(lèt_alfabetik, k=n))
    return kod
#test
n = 8
kod_aleyatwa = jenere_kod_aleyatwa(n)
print(kod_aleyatwa)
#4
import random
import string

def jenere_kod_aleyatwa(n):
    chif_lèt_alfanumerik = string.digits + string.ascii_letters
    kod = ''.join(random.sample(chif_lèt_alfanumerik, k=n))
    return kod

#test
n = 10
kod_aleyatwa = jenere_kod_aleyatwa(n)
print(kod_aleyatwa)
#5
import re

def jenere_slug(chenn):
    slug = re.sub(r'[^a-zA-Z0-9]+', '-', chenn)
    slug = re.sub(r'-+', '-', slug)
    slug = slug.strip('-')
    return slug.lower()

# test
chenn = "Hello World! How are you?"
slug = jenere_slug(chenn)
print(slug)
#6
def separe_let_ak_vigil(mot, vigil):
    mo_separe = vigil.join([let for let in mot])
    return mo_separe

# test
mot = "hello"
vigil = ","
mo_separe = separe_let_ak_vigil(mot, vigil)
print(mo_separe)
#7
def kripte_mo(mot):
    mo_kripte = '-'.join(str(ord(let) - ord('A')) for let in mot)
    return mo_kripte

# test
mot = "ALO"
mo_kripte = kripte_mo(mot)
print(mo_kripte)
#8
def dekripte_mo(mo_kripte):
    mot = ''.join(chr(int(ind) + ord('A')) for ind in mo_kripte.split('-'))
    return mot

# test
mo_kripte = "0-11-14"
mot = dekripte_mo(mo_kripte)
print(mot)
#9
def retounen_tuple(valè1, valè2):
    return (valè1, valè2)

# test
valè1 = 10
valè2 = "Hello"
rezilta = retounen_tuple(valè1, valè2)
print(rezilta)
#10
def retounen_inisyal(non):
    inisyal = ''.join(mot[0] for mot in non.split('-') if mot)
    return inisyal

# test
non = "Jean-Baptiste Jean"
inisyal = retounen_inisyal(non)
print(inisyal)
