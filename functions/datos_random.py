from Carta import Carta
import random

colores = ["Azul", "Rojo", "Blanco", "Negro", "Verde"]
mana = ["0", "1", "2", "3", "4"]
tipo = ["Tierra", "Encantamientos", "Instantáneos", "Artefactos", "Criaturas", "Conjuros", "Planeswalkers"]
rareza = ["Común", "Rara", "Poco Común", "Mítica"]
sustantivos = ["Angel","Artist","Autopsy","Avatar","Bat","Beast","Behemoth","Berserker","Blade",
"Blessing","Brute","Brute","Burglar","Catastrophe","Crow","Curse","Decay","Devil","Disciple","Eldrazi",
"Elf","Elk","End","Face","Familiar","Fiend","Frost","Gargoyle","General","Giant","Goblin","Golem",
"Gremlin","Growth","Guardian","Harpy","Herald","Hierophant","Horror","Nightmare","Alligator","Wyvern",
"Griffin","Metamorphosis","Tornado","Knight","Rot","Hellkite","Frog","War Priest","Strength",
"Pyromancer","Prophecy","Breath","Plate Mail","Abomination","Ox","Monument","Blood","Cow","Archer",
"Village","Banner","Offering","Armor","Manticore","Embrace","Orc","Horror","Hounds","Alien","Warrior",
"Healer","Mage","Sphinx","Rogue","Champion","Heart","Mentor","(of the) World","Elements","Eminence",
"(the) Unseen","King","Queen","Nectar","Guildgate","Bloom","Moon","Dryad","Cutthroat","Mastodon",
"Verdict","Praetor","Strix","(of) Youth","Charm","Ascension","Disenchant","Plant","Pirate"]

adjetivos = ["Abundant", "Adversary (of)","Æther","Angelic","Apocalypse of (the)","Architect"
,"Army of (the)","Avatar of (the)","Avenging","Awaken the","Blinding","Bloodcrazed","Celestial",
"Commander (of)","Cunning","Cursed","Cyclops","Demonic","Devout","Divine","Dragonscale",
"Elixir of (the)","Fearless","Feral","Flying","Forgotten","Goblin","Hellspawn","Hero (of)",
"Hypnotized","Illicit","Illusionary","Indestructible","Keeper of (the)","Lord (of)","Messenger",
"Mutating","Ogre","Phallic","Phantom","Primeval","Putrid","Radiant","Sad","Servant of (the)","Hidden",
"Shadowborn","Shamanic","Shimmering","Soaring","Solemn","Spectral","Spiteful","Sprawling","Spreading",
"Staff of (the)","Starving","Steel","Sturdy","The","Throbbing","Treacherous","Triumphant","Turn To",
"Twisted","Undead","Unstoppable","Unyielding","Vengeful","Vile","Villanous","Voice (of)","Void",
"Volatile","Volcanic","Wall of","Wasting","Weeping","Wild","Wind","Worshipped","Wounded","Zany",
"Oracle (of)","Hell's","Thunder","Hornet","Fungal","Ageless","Forsaken","Raging","Siege","Name's",
"Sanguine","Parasitic","Fountain","Great Oak","(Blank)","Platinum"]

cartas = []
for i in range(3):
   cartas.append(Carta(random.choice(adjetivos) + random.choice(sustantivos),random.choice(colores),random.choice(tipo),random.choice(mana),random.choice(rareza)))