#MASTER EXCEPTIONS
#1
while True:
    try:
        chif = int(input("Tape yon chif: "))
        rezilta = chif + 5
        print("Rezilta a + 5 se:", rezilta)
        break  
    except ValueError:
        print("Mwen bezwen yon chif! Tape chif sèlman")

#2
lis = [1, 2, 3, 4, 5]

try:
    endeks = int(input("Tape yon endeks: "))
    valè = lis[endeks]
    print("Valè a nan endeks la se:", valè)
except IndexError:
    print("Endeks la depase longè lis la! Tanpri, antre yon endeks ki nan limit lis la.")
except ValueError:
    print("Mwen bezwen yon chif! Tanpri, antre yon chif sèlman.")

#3
dik = {'nom': 'Jean', 'laj': 30}

try:
    kle = input("Tape yon kle: ")
    valè = dik[kle]
    print("Valè a pou kle", kle, "se:", valè)
except KeyError:
    print("Kle sa pa nan diksyonè a! Nou pral ajoute li ak valè None.")
    dik[kle] = None
    print("Diksyonè a apre ajoute kle la:", dik)

#4
class Ouvriye:
    def __init__(self, non, laj):
        self.non = non
        self.laj = laj

ouvriye1 = Ouvriye("Jean", 30)

try:
    print(ouvriye1.salaire)
except AttributeError:
    ouvriye1.salaire = None
    print("Atribi sa pa ekziste nan klas la. Nou pral ajoute li ak valè None.")

print("Salè ouvriye a se:", ouvriye1.salaire)

#5
class Personne:
    def __init__(self, non):
        self.non = non
    
    def saluer(self):
        return f"Bonjour, je m'appelle {self.non}."

personne1 = Personne("Jean")

try:
    fonction_saluer = personne1.saluer
    if callable(fonction_saluer):
        resultat = fonction_saluer()
        print(resultat)
    else:
        print("Atribi sa pa yon fonksyon.")
except AttributeError:
    print("Atribi sa pa ekziste nan enstans la.")

#6
chif_romèn = "IVXLCDM"
while True:
    chenn = input("Tape yon chenn ki gen sèlman karaktè romèn (IVXLCDM): ")
    si_valid = all(karaktè.upper() in chif_romèn for karaktè in chenn)
    if si_valid and len(chenn) == 1:
        print("Chenn ou antre a korek.")
        break
    else:
        print("Ou dwe antre yon sèl karaktè romèn (IVXLCDM).")
