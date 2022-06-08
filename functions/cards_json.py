import Carta as Carta
import os
import json

dictlist = []
file = os.path.join("functions/cards.json")

def load_cards():
    Cartas = []
    with open(file) as f:
        dictlist = json.load(f)
        for amp in dictlist:
            nam = amp.get("name")
            col = amp.get("color")
            typ = amp.get("type")
            man = amp.get("mana")
            rar = amp.get("rarity")
            card = [nam, col, typ, man, rar]
            Cartas.append(card)
    return Cartas

def save_cards(Cards):
    os.remove('functions/cards.json')
    with open("functions/cards.json", 'a') as x:
        x.write("[\n")
        card = "a"
        for i in Cards:
            if card != "a":
                x.write(",\n")
            nom = i[0]
            col = i[1]
            tip = i[2]
            man = i[3]
            rar = i[4]
            card = f'{{"name":"{nom}", "color":"{col}", "type":"{tip}", "mana":"{man}", "rarity":"{rar}"}}'
            x.write(card)
        x.write("\n]")