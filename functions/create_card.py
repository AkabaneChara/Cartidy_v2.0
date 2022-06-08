import functions.define as define
import functions.print as pr
from functions.datos_random import colores, mana, tipo, adjetivos, sustantivos, rareza
import random
from functions.aesthetic import TAz, TRo, FAz, SRe

def card_manual():
    print(FAz + "Ingrese los datos de la carta:" + SRe + "\n")
    print(TAz + "\nNombre: " + SRe)
    name = input()
              
    while True:
        print(TAz + "\nColor: " + SRe)
        print(TRo+"1. "+TAz+"Azul.  "+TRo+"2. "+TAz+"Rojo.  "+TRo+"3. "+TAz+"Blanco. ")
        print(TRo+"4. "+TAz+"Negro. "+TRo+"5. "+TAz+"Verde. ")
        color = input(SRe)
        if not pr.siEntradaValida(color):
            pr.inputNoValidoSC()
        else:
            color = int(color)
            if color<6:
                color = define.color(color)
                break
            else:
                pr.inputNoValidoSC()

    while True:
        print(TAz + "\nTipo: " + SRe)
        print(TRo+"1. "+TAz+"Tierra.   "+TRo+"2. "+TAz+"Encantamiento. "+TRo+"3. "+TAz+"Instantaneo.  "+TRo+"4. "+TAz+"Artefacto. ")
        print(TRo+"5. "+TAz+"Criatura. "+TRo+"6. "+TAz+"Conjuro.       "+TRo+"7. "+TAz+"Planeswalker. ")
        tipe = input(SRe)
        if not pr.siEntradaValida(tipe):
            pr.inputNoValidoSC()
        else:
            tipe = int(tipe)
        if tipe<8:
            tipe = define.tipe(tipe)
            break
        else:
            pr.inputNoValidoSC()

    while True:
        print(TAz + "\nManá: " + SRe)
        mana = input(SRe)
        if not pr.siEntradaValida(mana):
            pr.inputNoValidoSC()
        else:
            break

    while True:              
        print(TAz + "\nRareza: " + SRe)
        print(TRo+"1. "+TAz+"Común. "+TRo+"2. "+TAz+"Poco Común. "+TRo+"3. "+TAz+"Rara. "+TRo+"4. "+TAz+"Mítica. ")
        rarity = int(input(SRe))
        if not pr.siEntradaValida(rarity):
            pr.inputNoValidoSC()
        else:
            rarity = int(rarity)
            if rarity<5:
                rarity = define.rarity(rarity)
                break
            else:
                pr.inputNoValidoSC()

    while True:
        print(TAz + "\nCantidad de Cartas: " + SRe)
        amount = input()
        if not pr.siEntradaValida(amount):
            pr.inputNoValidoSC()
        else:
            amount = int(amount)
            break

    return name, color, tipe, mana, rarity, amount

def name_auto():
    return random.choice(adjetivos) + random.choice(sustantivos)

def color_auto():
    return random.choice(colores)

def tipe_auto():
    return random.choice(tipo)

def mana_auto():
    return random.choice(mana)

def rarity_auto():
    return random.choice(rareza)

def card_automatic():
    name = random.choice(adjetivos) + random.choice(sustantivos)
    color = random.choice(colores)
    tipe = random.choice(tipo)
    mana_ = random.choice(mana)
    rarity = random.choice(rareza)
    Card = [name, color, tipe, mana_, rarity]
    return Card