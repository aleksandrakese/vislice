import model

# Funkcije, ki generirajo izpis za igralca

def izpis_poraza(igra):
    return 'Porabili ste preveč poskusov, pravilno geslo je {}.'.format(igra.geslo)

def izpis_zmage(igra):
    return 'Uspešno ste uganili geslo {}!'.format(igra.geslo)

def izpis_igre(igra):
    tekst = (
        '========================================\n\n'
        '    {trenutno_stanje}\n\n'
        'Neuspešni poskusi: {poskusi}\n\n'
        '========================================'
    ).format(trenutno_stanje=igra.pravilni_del_gesla(), poskusi=igra.nepravilni_ugibi())

    return tekst

def zahtevaj_vnos():
    vnos = input('Poskusi uganit črko: ')
    return vnos

def preveri_vnos(vnos):
    ''' Funkcija vrne True, če je vnos primeren, sicer igralca opozori in vrne False'''
    if len(vnos) != 1:
        print('Neveljaven vnos! Vnesi zgolj eno črko.')
        return False
    else:
        return True

# Izvajanje vmesnika

def zazeni_vmesnik():
    igra = model.nova_igra()

    while True:
        # izpišemo stanje
        print(izpis_igre(igra))
        # igralec ugiba
        poskus = zahtevaj_vnos()  # !!! ŠE NI NAPISANO !!!
        if not preveri_vnos(poskus):
            continue  # Preskoči preostanek zanke
        rezultat = igra.ugibaj(poskus)
        # preverimo, če je igre konec
        if igra.poraz():  # if rezultat == model.PORAZ
            print(izpis_poraza(igra))
            return
        elif igra.zmaga():
            print(izpis_zmage(igra))
            return
    return

# zares poženi igro
zazeni_vmesnik()