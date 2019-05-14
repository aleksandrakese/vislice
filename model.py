import random

# Definiramo konstante
STEVILO_DOVOLJENIH_NAPAK = 10

PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'

ZMAGA = 'W'
PORAZ = 'X'

# Definiramo logični model igre

class Igra:

    def __init__(self, geslo, crke):
        self.geslo = geslo.upper() # string
        self.crke = crke # list
        return 

    def napacne_crke(self):
        seznam_napacnih_crk = []
        for x in self.crke:
            if x not in self.geslo:
                seznam_napacnih_crk.append(x)
        return seznam_napacnih_crk
    
    def pravilne_crke(self):
        seznam_pravilnih_crk = []
        for x in self.crke:
            if x in self.geslo:
                seznam_pravilnih_crk.append(x)
        return seznam_pravilnih_crk

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK

    def zmaga(self):
        for crka in self.geslo:
            if crka not in self.crke:
                return False
        return True

    def pravilni_del_gesla(self):
        niz = ''
        for crka in self.geslo:
            if crka in self.crke:
                niz += ' ' + crka
            else:
                niz += ' _'
        niz = niz.strip() # Počistimo presledke
        return niz

    def nepravilni_ugibi(self):
        return ' '.join(self.napacne_crke())

    def ugibaj(self, crka): # spreminja stanje igre (ostale: komunikacija z zunanjim svetom)
        crka = crka.upper()
        if crka in self.crke:
            return PONOVLJENA_CRKA
        elif crka in self.geslo:
            self.crke.append(crka)
            if self.zmaga:
                return ZMAGA
            else:
                return PRAVILNA_CRKA
        else:
            self.crke.append(crka)
            if self.poraz():
                return PORAZ
            else:
                return NAPACNA_CRKA

# Izluščimo vse slovenske besede
bazen_besed = []

with open("vislice.txt", 'r', encoding='utf-8') as datoteka:
    for vrstica in datoteka.readlines():
        beseda = vrstica.strip()
        bazen_besed.append(beseda)

# Funkcije za generiranje iger

def nova_igra():
    geslo = random.choice(bazen_besed)
    return Igra(geslo, [])


