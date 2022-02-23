from Nodo import *
 
class Arbol:

    def __init__(self,dato):
        self.raiz = Nodo(dato)

    def agregar(self, dato):
        self.insertar(dato, self.raiz)
    
    def insertar(self,dato, nodo):
        if dato > nodo.dato:
            if nodo.derecha is None:
               nodo.derecha = Nodo(dato)
            else:
                if nodo.izquierda is None:
                    nodo.izquierda = Nodo(dato)
                else:
                    self.insertar(dato, nodo.izquierda)
        
    