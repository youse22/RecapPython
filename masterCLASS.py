#Master class
#1
import os

class GestionFichye:
    def __init__(self, chemen_fichye):
        self.chemen_fichye = chemen_fichye
    def kreye_fichye(self):
        # Kreye fichye a sèlman si li pa egziste
        if not os.path.exists(self.chemen_fichye):
            with open(self.chemen_fichye, 'w') as fichye:
                fichye.write('')  # Kreye yon fichye vid
            print(f"Fichye '{self.chemen_fichye}' te kreye avèk siksè.")
        else:
            print(f"Fichye '{self.chemen_fichye}' deja egziste.")
    def li(self):
        with open(self.chemen_fichye, 'r') as fichier:
            kontni = fichier.read()
        return kontni

    def ajoute(self, kontni):
        with open(self.chemen_fichye, 'a') as fichier:
            fichier.write(kontni)

    def efase_kontni(self):
        with open(self.chemen_fichye, 'w') as fichier:
            fichier.truncate(0)

    def efase_fichye(self):
        if os.path.exists(self.chemen_fichye):
            os.remove(self.chemen_fichye)
            return True
        else:
            return False

# test
gestion_fichye = GestionFichye("exemple.txt")
gestion_fichye.kreye_fichye()
print(gestion_fichye.li())  
gestion_fichye.ajoute("\nNouvo kontni.")  
print(gestion_fichye.li())  
gestion_fichye.efase_kontni()  
print(gestion_fichye.li()) 
gestion_fichye.efase_fichye()  

#2
class Moun:
    def __init__(self, pye, men, non, laj):
        self.pye = pye
        self.men = men
        self.non = non
        self.laj = laj

    def afiche_tout(self):
        print(f"Non: {self.non}, Men: {self.men}, Pye: {self.pye}, Laj: {self.laj}")

class Vivan(Moun):
    def __init__(self, pye, men, non, laj):
        super().__init__(pye, men, non, laj)
        self.pye = pye
        self.men = men
        self.non = non
        self.laj = laj

    def afiche_tout(self):
        print("Moun Vivan:")
        super().afiche_tout()

class Poul(Moun):
    def __init__(self, non, laj):
        super().__init__(4, 2, non, laj)
        self.pye = 2
        self.men = 2

    def afiche_tout(self):
        print("Poul:")
        super().afiche_tout()

# Kreye yon enstans de klas Vivan
vivan1 = Vivan(2, 2, "Jean", 30)
vivan1.afiche_tout()

# Kreye yon enstans de klas Poul
poul1 = Poul("Koko", 1)
poul1.afiche_tout()