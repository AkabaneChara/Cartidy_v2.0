from functions.aesthetic import TAz, SRe

class Nodo:
    def __init__(self, dato, padre):
        self.dato = dato
        self.izquierda = None
        self.derecha = None
        self.padre = padre
      
class Arbol:
    def __init__(self, dato):
        self.raiz = Nodo(dato, None)

    def insertar(self, dato, nodo):
        if dato.mana < nodo.dato.mana:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(dato, nodo)
            else:
                self.insertar(dato, nodo.izquierda)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(dato, nodo)
            else:
                self.insertar(dato, nodo.derecha)
        bal = self.balance(nodo)
        if bal > 1:
          if dato.mana <= nodo.izquierda.dato.mana:
                return self.rotarDerecha(nodo)
          else:
                nodo.izquierda = self.rotarIzquierda(nodo.izquierda)
                return self.rotarDerecha(nodo)
        if bal < -1:
            if dato.mana >= nodo.derecha.dato.mana:
                return self.rotarIzquierda(nodo)
            else:
                nodo.derecha = self.rotarDerecha(nodo.derecha)
                return self.rotarIzquierda(nodo)
        return nodo


    def rotarDerecha(self, nodo):
        P = nodo.padre
        Y = nodo.izquierda
        B = Y.derecha
        Y.padre = P
        if nodo == self.raiz:
          self.raiz = Y
          self.raiz.derecha = nodo
        else:
          if nodo == P.derecha:
            P.derecha = Y
          else:
            P.izquierda = Y
        nodo.padre = Y
        Y.derecha = nodo
        if B != None:
          B.padre = nodo
        nodo.izquierda = B
        return Y

    def rotarIzquierda(self, nodo):
        P = nodo.padre
        Y = nodo.derecha
        B = Y.izquierda
        Y.padre = P
        if nodo == self.raiz:
          self.raiz = Y
          self.raiz.izquierda = nodo
        else:
          if nodo == P.derecha:
            P.derecha = Y
          else:
            P.izquierda = Y
        nodo.padre = Y 
        Y.izquierda = nodo
        if B != None:
          B.padre = nodo 
        nodo.derecha = B
        return Y

    def balance(self, nodo):
        if nodo == None:
            return 0
        return self.getAltura(nodo.izquierda) - self.getAltura(nodo.derecha)
  
    def getAltura(self, nodo):
      if nodo == None:
        return 0
      else:
        return 1+max(self.getAltura(nodo.derecha),self.getAltura(nodo.izquierda))
    
    def addDato(self, dato):
        self.insertar(dato, self.raiz)
      
    def inFijo(self):
        self.inOrden(self.raiz)

    def inOrden(self, nodo):
        if nodo is not None:
            self.inOrden(nodo.izquierda)
            print(f"{TAz}Nombre: {SRe}{nodo.dato.nombre}. {TAz}Color: {SRe}{nodo.dato.color}. {TAz}Tipo: {SRe}{nodo.dato.tipo}. {TAz}Mana: {SRe}{nodo.dato.mana}. {TAz}Rareza: {SRe}{nodo.dato.rareza}.")
            self.inOrden(nodo.derecha)