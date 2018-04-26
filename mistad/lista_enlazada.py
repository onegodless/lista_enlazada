from nodo import Nodo

class ListaEnlazada(object):
    
    def __init__(self):
        
        self.prim = None
        self.len = 0
        
    def __str__(self):
        n_ant = self.prim
        n_act = n_ant.prox
        print n_ant.dato
        for x in range (1, len-1):
            print n_act.dato
    
    def __len__(self):
        return self.len

    def append(self,nuevo_nodo):        
        
        #caso en el que la lista está vacia
        if self.len == 0:
            self.prim = nuevo_nodo
            self.len += 1
        #caso en el que previamente haya elementos en la lista.
        else:
            i = self.len
            n_ant = self.prim
            n_act = n_ant.prox
            for x in range (1, i):
                n_ant = n_act
                n_act = n_act.prox
            n_act.prox = nuevo_nodo
            self.len += 1
                
    def index(self, x):
        n_ant = self.prim
        n_act = n_ant.prox
        posicion = 0
        
        #caso en el que el elmento que se busca sea el primero de la lista
        if n_ant.dato == x:
            return posicion
        
        #caso en el que la lista este vacia.
        elif self.len == 0:
            raise IndexError("Lista vacia.")
        
        #caso general
        posicion = 1
        while n_act.prox != None:
            if n_act.dato == x:
                return posicion
            posicion += 1
        raise ValueError("No existe el dato en la lista.")
        
    def insert(self,i=None):
        
        if i < 0 or i > self.len:
            raise IndexError("Indice fuera de rango")
        
        nuevo = nodo(x)
        if i == 0:
            nuevo.prox = self.prim
            self.prim = nuevo
            sle
        else:
            n_ant = self.prim
            for pos in range(1,i):
                n_ant = n_ant.prox
                self.len += 1
        
    
    def remove(self, x):
        
        if self.len == 0:
            raise ValueError("Lista vacia")
        
        elif self.prim.dato == x:
            self.prim = self.prim.prox
        
        n_ant = self.prim
        n_act = n_ant.prox
        
        while n_act.dato != x and n_act.prox != None:
            
            n_ant = n_act
            n_act = n_ant.prox
            
        if n_act == None:
            raise ValueError("El valor no esta en la lista")
        
        
        else:
            n_ant.prox = n_act.prox
            
    def pop(self,i):
        
        if(i < 0) or (i >= self.len):
            raise IndexError("Indice fuera de rango")
        
        elif i == None:
            i = self.len -1 
        
        elif i==0:
            dato = self.prim.dato
            self.prim = self.prim.prox
        
        else:
            n_ant = self.prim
            n_act = n_ant.prox
            for x in xrange(1,i):
                n_ant = n_act
                n_act = n_ant.prox
            dato = n_act.dato
            n_ant.prox = n_act.prox
            self.len -= 1
            return dato