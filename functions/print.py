import os
from functions.aesthetic import TAz, TMa, SRe

def inputNoValido():
    print(TAz + "\nPor favor digíte una opción válida.")
    pressToContinue()
    
def pressToContinue():
    input(TMa + "Press Enter to continue..." + SRe)
    os.system('cls' if os.name=='nt' else 'clear')

def siEntradaValida(num):   
    try:
        num = int(num)
    except ValueError:
        return False
    if num>0: return True
    else:  return False

def inputNoValidoSC():
    print(TAz + "\nPor favor digíte una opción válida.")
    input(TMa + "Press Enter to continue..." + SRe)