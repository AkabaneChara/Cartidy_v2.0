from ListaEnlazada import ListaEnlazada
from Nodo import Nodo

class StackEnlazado(ListaEnlazada):
    def __init__(self):
        self.head = None
        self.tail = None
        self.longitud = 0

    def push(self,item):
        self.longitud += 1
        if self.empty():
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def pop(self):
        if self.empty():
            print("No se puede hacer pop. Está vacía.")
        elif self.longitud == 1:
            self.longitud -= 1
            val = self.head.dato
            self.tail = None
            self.head = None
            return val
        else:
            self.longitud -= 1
            valor = self.tail.dato
            contador = self.head
            while contador.next != self.tail:
                contador = contador.next
            self.tail = contador
            return valor

    def top(self):
        return self.tail.dato



