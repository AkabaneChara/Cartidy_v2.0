from Carta import Carta
from Nodo import Nodo
from ListaEnlazadaFull import ListaEnlazadaFull as Lista
import functions.print as pr
import functions.create_card as create
import functions.search_data as search
import functions.aesthetic as text
import functions.cards_json as jsonfile
import time, os
from AVL import Arbol as AVL
from functions.aesthetic import TAz, TRo, TVe, FAz, FRo, SRe
Baraja = Lista()

def Menu():
    salir = False
    while not salir:
        os.system('cls' if os.name=='nt' else 'clear')
        text.tittle("Welcome To")
        text.tittle("Cartidy")
        print("\n" + FAz + "Ingrese la operación que quiere ejecutar (Señalada por el entero que le antecede):" + SRe + "\n")
        print(TRo + "1. " + TAz + "Agregar cartas.")
        print(TRo + "2. " + TAz + "Eliminar cartas.")
        print(TRo + "3. " + TAz + "Ordenar cartas.")
        print(TRo + "4. " + TAz + "Simular mazo cartas.")
        print(TRo + "5. " + TAz + "Ver todas las cartas.")
        print(TRo + "6. " + TAz + "Cerrar menú.")
        print(SRe)
        n = input()
        
        if not pr.siEntradaValida(n):
            pr.inputNoValido()
        else:
            n = int(n)
            if n == 1:
                os.system('cls' if os.name=='nt' else 'clear')
                crearCartasMenu()
            elif n == 2:
                os.system('cls' if os.name=='nt' else 'clear')
                eliminarCartaMenu()
            elif n == 3:
                os.system('cls' if os.name=='nt' else 'clear')
                ordenarCartaMenu()
            elif n == 4:
                print(FRo + "\nFunción en proceso..." + SRe)
                pr.pressToContinue()
            elif n == 5:
                os.system('cls' if os.name=='nt' else 'clear')
                mostrarCartas()
            elif n == 6:
                print(FRo + "Gracias por su visita ¡Vuelva pronto!"+ SRe)
                pr.pressToContinue()
                salir = True
            else:
                pr.inputNoValido()

def crearCartasMenu():
    crear = False

    while not crear:
        text.tittle("Crear Cartas")
        print("\n" + FAz + "Ingrese la operación que quiere ejecutar (Señalada por el entero que le antecede):" + SRe + "\n")
        print(TRo + "1. " + TAz + "Añadir datos manualmente.")
        print(TRo + "2. " + TAz + "Testeo automatico.")
        print(TRo + "3. " + TAz + "Menú Principal.")
        print(SRe)
        n = input()
  
        if not pr.siEntradaValida(n):
            pr.inputNoValido()
        else:
            os.system('cls' if os.name=='nt' else 'clear')
            n = int(n)
            if n == 1:
                text.subtittle("I N G R E S O  M A N U A L")

                name, color, tipe, mana, rarity, amount = create.card_manual()

                confirmation = input(FRo + "\n¿Los datos ingresados son correctos? (Y/N)" + SRe + " " + TRo)

                if confirmation == "Y" or confirmation == "y":
                    for i in range(amount):
                        card = Nodo(Carta(name, color, tipe, mana, rarity))
                        if (not Baraja.empty()):
                            next = Baraja.searchMayor(name)
                            Baraja.insertar(card,next)
                        else:
                            Baraja.encolar(card)
                        
                pr.pressToContinue()

            elif n == 2:
                text.subtittle("T E S T E O")
                print(FAz + "Ingrese cuantas cartas quiere crear para el testeo:" + SRe + "\n")
                print(TRo + "1. " + TAz + "10 cartas.")
                print(TRo + "2. " + TAz + "100 cartas.")
                print(TRo + "3. " + TAz + "1.000 cartas.")
                print(TRo + "4. " + TAz + "10.000 cartas.")
                print(TRo + "5. " + TAz + "100.000 cartas.")
                print(TRo + "6. " + TAz + "1'000.000 cartas.")
                print(TRo + "7. " + TAz + "10'000.000 cartas.")
                print(TRo + "8. " + TAz + "100'000.000 cartas.")
                print(TRo + "9. " + TAz + "Menú Principal.")
                print(SRe)
                n = input()
              
                cantidad = 0
              
                if not pr.siEntradaValida(n):
                    pr.inputNoValido()
                else:
                  n = int(n)
                  if n == 1:   cantidad = 10
                  elif n == 2: cantidad = 100
                  elif n == 3: cantidad = 1000
                  elif n == 4: cantidad = 10000
                  elif n == 5: cantidad = 100000
                  elif n == 6: cantidad = 1000000
                  elif n == 7: cantidad = 10000000
                  elif n == 8: cantidad = 100000000
                  elif n == 9: break
                  else:
                    pr.inputNoValido()
                  if n<9: 
                      inicio = time.time()
                      ind = Baraja.longitud+cantidad
                      while Baraja.longitud < ind:
                          name = create.name_auto()
                          color = create.color_auto()
                          tipe = create.tipe_auto()
                          mana = create.mana_auto()
                          rarity = create.rarity_auto()
                          card = Nodo(Carta(name, color, tipe, mana, rarity))
                          if (not Baraja.empty()):
                              next = Baraja.searchMayor(name)
                              Baraja.insertar(card,next)
                          else:
                              Baraja.encolar(card)
                          
                      fin = time.time()
                      print(TVe + f"\nEl tiempo que tomó realizar la operación de insertar {cantidad} cartas al sistema fue de: {fin-inicio} segundos.")
                      pr.pressToContinue()
                
            elif n == 3:
                break
            else:
                pr.inputNoValido()

def eliminarCartaMenu():
    eliminar = False
    while not eliminar:
        text.tittle("Eliminar Cartas")
        print("\n" + FAz + "Ingrese el filtro para buscar la carta a eliminar (Señalada por el entero que le antecede):" + SRe + "\n")
        print(TRo + "1. " + TAz + "Rareza.")
        print(TRo + "2. " + TAz + "Color.")
        print(TRo + "3. " + TAz + "Tipo.")
        print(TRo + "4. " + TAz + "Testeo.")
        print(TRo + "5. " + TAz + "Menu Principal.")
        print(SRe)
        n = input()
      
        if not pr.siEntradaValida(n):
            pr.inputNoValido()
        else:
            os.system('cls' if os.name=='nt' else 'clear')
            n = int(n) 
            if n<=3:
                search_id, search_by = search.search_data(n)
                if search_by!=0:
                    os.system('cls' if os.name=='nt' else 'clear')
                    print("\n")
                  
                    i = Baraja.filter(search_id, search_by)
                    delete = []
                  
                    for x in range(len(i)):
                        print(f"{TRo}{x+1}) {TAz}Nombre: {SRe}{i[x][0]}. {TAz}Color: {SRe}{i[x][1]}. {TAz}Tipo: {SRe}{i[x][2]}.{TAz}Mana: {SRe}{i[x][3]}. {TAz}Rareza: {SRe}{i[x][4]}.")
                        delete.append(i[x][0])
                    print("\n" + FAz + "Ingrese por número y separados por coma las cartas que desea eliminar: (Ejemplo: 2,3,5,9)" + SRe + "\n")
                    try: index = [int(x) for x in input().split(",")]
                    except: pr.inputNoValido()

                    for i in range(len(index)):
                        prev = Baraja.search(delete[index[i]-1])
                        Baraja.delete(prev)
                    
                    pr.pressToContinue()
                  
                else:
                    os.system('cls' if os.name=='nt' else 'clear')
            elif n == 4:
                search_id, search_by = search.search_data(n)
                if search_by!=0:
                    os.system('cls' if os.name=='nt' else 'clear')
                    print("\n")
                    inicio = time.time()
                  
                    i = Baraja.filter(search_id, search_by)
                    delete = []
                  
                    for x in range(len(i)):
                        print(f"{TRo}{x+1}) {TAz}Nombre: {SRe}{i[x][0]}. {TAz}Color: {SRe}{i[x][1]}. {TAz}Tipo: {SRe}{i[x][2]}.{TAz}Mana: {SRe}{i[x][3]}. {TAz}Rareza: {SRe}{i[x][4]}.")
                        delete.append(i[x][0])
                    print("\n" + FAz + "Ingrese por número y separados por coma las cartas que desea eliminar: (Ejemplo: 2,3,5,9)" + SRe + "\n")

                    index = range(1, len(delete))

                    for i in range(len(index)):
                        prev = Baraja.search(delete[index[i]-1])
                        Baraja.delete(prev)
                  
                    fin = time.time()
                    print(TVe + f"\nEl tiempo que tomó realizar la operación de eliminar {Baraja.longitud} cartas al sistema fue de: {fin-inicio} segundos.")
                    pr.pressToContinue()

                    for i in range(len(index)):
                        prev = Baraja.search(delete[index[i]-1])
                        Baraja.delete(prev)

                    
                    pr.pressToContinue()
                  
            elif n == 5:
                break
            else:
                pr.inputNoValido()

def ordenarCartaMenu():
    ordenar = False
    while not ordenar:
        text.tittle("Ordenar Cartas")
        print("\n" + FAz + "Ingrese el filtro para buscar la carta a eliminar (Señalada por el entero que le antecede):" + SRe + "\n")
        print(TRo + "1. " + TAz + "Rareza.")
        print(TRo + "2. " + TAz + "Color.")
        print(TRo + "3. " + TAz + "Tipo.")
        print(TRo + "4. " + TAz + "Menu Principal.")
        print(SRe)
        n = input()
      
        if not pr.siEntradaValida(n):
            pr.inputNoValido()
        else:
            os.system('cls' if os.name=='nt' else 'clear')
            n = int(n) 
            if n<4:
                search_id, search_by = search.search_data(n)
                if search_by!=0:
                    print("\n")
                    inicio = time.time()
                    i = Baraja.filter(search_id, search_by)
                    for x in range(len(i)):
                        carta = Carta(i[x][0], i[x][1], i[x][2], i[x][3], i[x][4])
                        if (x != 0):
                              Filtro.addDato(carta)
                        else:
                              Filtro = AVL(carta)
                    Filtro.inFijo()
                    fin = time.time()
                    print(TVe + f"\nEl tiempo que tomó realizar la operación de filtrar {Baraja.longitud} cartas al sistema fue de: {fin-inicio} segundos.")
                    pr.pressToContinue()
                else:
                    os.system('cls' if os.name=='nt' else 'clear')
            elif n == 4:
                break
            else:
                pr.inputNoValido()

def mostrarCartas():
    text.tittle("Mostrar Cartas")
    print("\n" + FAz + f"A continuación están las {Baraja.longitud} cartas de su baraja:" + SRe + "\n")
    inicio = time.time()
    i = Baraja.printLista()
    if not Baraja.empty():
        for x in range(len(i)):
            print(f"{TRo}{x+1}) {TAz}Nombre: {SRe}{i[x][0]}. {TAz}Color: {SRe}{i[x][1]}. {TAz}Tipo: {SRe}{i[x][2]}. {TAz}Mana: {SRe}{i[x][3]}. {TAz}Rareza: {SRe}{i[x][4]}.")
        print("\n")
    fin = time.time()
    print(TVe + f"\nEl tiempo que tomó realizar la operación de mostrar {Baraja.longitud} cartas al sistema fue de: {fin-inicio} segundos.")
    pr.pressToContinue()
    
def cargar_cartas():
    cartas = jsonfile.load_cards()
    for i in cartas:
        nam = i[0]
        col = i[1]
        tip = i[2]
        man = i[3]
        rar = i[4]
        card = Nodo(Carta(nam, col, tip, man, rar))
        Baraja.encolar(card)

def guardar_cartas():
    Cartas = []
    for i in range(Baraja.longitud):
        try:
            nam = Baraja.getName()
            col = Baraja.getColor()
            tip = Baraja.getType()
            man = Baraja.getMana()
            rar = Baraja.getRarity()
            card = [nam, col, tip, man, rar]
            Cartas.append(card)
            Baraja.desencolar()
        except:
          break
    jsonfile.save_cards(Cartas) 

cargar_cartas()
Menu()
guardar_cartas()