import Carta as Carta
from StackEnlazado import StackEnlazado

class ListaEnlazadaFull(StackEnlazado):
    #Lo que hereda con StackEnlazado: empty(), push(x), pop(x), top()
    #Se le añade: encolar(x), desencolar(x), bot(), search()
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

    def insertar(self, insercion, ubicacion):
        b = self.head
        if ubicacion == "head":
            insercion.next = self.head
            self.head = insercion
            self.longitud += 1
        else:
            while b != None:
                if b == ubicacion:
                    insercion.next = b.next
                    b.next = insercion
                    self.longitud += 1
                    break
                b = b.next

    def delete(self, ubicacion):
        b = self.head
        if ubicacion == "head":
            self.head = self.head.next
            self.longitud -= 1
        else:
            while b != None:
                if b == ubicacion:
                    b.next = b.next.next
                    self.longitud -= 1
                    break
                b = b.next

    def search(self,text):
        if self.head.dato == text:
            return "head"
        m = self.head.next
        while m != None:
            if m.next.dato.nombre == text:
                return m
            else:
                m = m.next
        return None

    def searchMayor(self,text):
        if text < self.head.dato.nombre:
            return "head"
        if text > self.tail.dato.nombre:
            return self.tail
        m = self.head.next
        while m != None:
            if m.dato.nombre < text and text < m.next.dato.nombre:
                return m
            else:
                m = m.next
        return None

    def filter(self, search_id, search_by):
        m = self.head
        filtro = []
      
        if search_id == "Rareza": 
            while m != None:
                if m.dato.rareza == search_by:
                    nam = m.dato.nombre
                    col = m.dato.color
                    tip = m.dato.tipo
                    man = m.dato.mana
                    rar = m.dato.rareza
                    card = [nam, col, tip, man, rar]
                    filtro.append(card)
                m = m.next
              
        elif search_id == "Color":
            while m != None:
                if m.dato.color == search_by:
                    nam = m.dato.nombre
                    col = m.dato.color
                    tip = m.dato.tipo
                    man = m.dato.mana
                    rar = m.dato.rareza
                    card = [nam, col, tip, man, rar]
                    filtro.append(card)
                m = m.next
              
        elif search_id == "Tipo":
              while m != None:
                if m.dato.tipo == search_by:
                    nam = m.dato.nombre
                    col = m.dato.color
                    tip = m.dato.tipo
                    man = m.dato.mana
                    rar = m.dato.rareza
                    card = [nam, col, tip, man, rar]
                    filtro.append(card)
                m = m.next
                
        return filtro

    def bot(self):
        return self.tail.dato

    def getName(self):
        return self.head.dato.nombre

    def getColor(self):
        return self.head.dato.color

    def getType(self):
        return self.head.dato.tipo

    def getMana(self):
        return self.head.dato.mana

    def getRarity(self):
        return self.head.dato.rareza
