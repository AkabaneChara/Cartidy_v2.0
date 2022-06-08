from ListaEnlazada import ListaEnlazada
from Nodo import Nodo

class ColaEnlazada(ListaEnlazada):
    def __init__(self):
        self.head = None
        self.tail = None

    def encolar(self,item):
        self.longitud += 1
        if self.empty():
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def desencolar(self):
        if self.empty():
            print("No se puede desencolar. Está vacía.")
        else:
            self.longitud -= 1
            valor = self.head.dato
            self.head = self.head.next
            return valor

    def top(self):
        return self.head.dato
    




