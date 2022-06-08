from colorama import Fore, Back, Style
from pyfiglet import figlet_format

TVe = Fore.GREEN
TAz = Fore.BLUE
TRo = Fore.RED
TMa = Fore.MAGENTA
TAm = Fore.YELLOW

FVe = Back.GREEN
FAz = Back.BLUE
FRo = Back.RED
FMa = Back.MAGENTA
FAm = Back.YELLOW

SRe = Style.RESET_ALL

font_1 = 'slant'
font_2 = 'mini'

cartas = []

def tittle(text):
    print(figlet_format(text, font=font_1, justify='center'))

def subtittle(text):
    print (figlet_format(text, font=font_2, width=200))