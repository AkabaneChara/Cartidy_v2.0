from Nodo import Nodo
import Carta as Carta

class ListaEnlazada(): #Clase lista enlazada
    def __init__(self):  #Crearla, cabeza y cola vacias
        self.head = None
        self.tail = None
        self.count = 0

    def empty(self): #Si está vacío
        if self.head == None:
            return True
        else:
            return False

    def printLista(self):   #Print de lista
        if self.empty():    #Decir si está vacía
            print("La lista está vacía.")
        else:               #Si no, recorrerla toda
            temp = self.head    #Inicializar apuntador para recorrer
            lista = []      #String donde se guarda lista
            count = 1
            while temp != None:
                aux = [temp.dato.nombre, temp.dato.color, temp.dato.tipo, temp.dato.mana, temp.dato.rareza]
                lista.append(aux)
                temp = temp.next
                count += 1
            return lista
