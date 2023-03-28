from nodo import Nodo
class Lista:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0
    #METODOS PARA AGREGAR DATOS
    def insertarFinal(self, dato):
        nuevoNodo = Nodo(dato)
        self.size +=1
        #si la lista no tiene ningun dato
        if self.primero == None:
            #el apuntador primero apunta al nuevo nodo
            self.primero = nuevoNodo
            #el apuntador ultimo apunta al nuevo nodo
            self.ultimo = nuevoNodo
        #si la lista ya tiene uno o mas datos se agrega el nuevo nodo
        else: 
            #el apuntador siguiente apunta al nuevo nodo --->
            self.ultimo.siguiente = nuevoNodo
            #el apuntador anterior apunta al nodo anterior  <---
            nuevoNodo.anterior = self.ultimo
            #el apuntador ultimo apunta al nuevo nodo
            self.ultimo = nuevoNodo

    def obtenerSize(self):
        return self.size   

    #METODO PARA DEJAR LA LISTA VACIA
    def inicializarLista(self):
        self.primero = None
        self.ultimo = None
    #METODO PARA VALIDAR SI LA LISTA ESTÁ VACIA
    def estaVacia(self):
        #si el primero es diferente de nulo No está vacia
        if self.primero !=None:
            return True
        #Si el primero es igual a nulo Si está vacia
        if self.primero ==None:
            return False
    
    #METODOS PARA LISTA ELEMENTOS    
    def ObtenerElementos(self, recibiendoCONT):
        contador = 0
        nodoTemporal = Nodo("")
        nodoTemporal = self.primero
        while nodoTemporal != None:
            contador +=1
            if contador == recibiendoCONT:
                return nodoTemporal.dato
            nodoTemporal = nodoTemporal.siguiente 
    def validarRepetidos(self, numeroAtomico_1, simbolo_1, nombre_1):
        nodoTemporal = Nodo("")
        nodoTemporal = self.primero
        booleanoValidador = False
        while nodoTemporal != None:
            if (str(nodoTemporal.dato.getElementoNumAtomico()) == str(numeroAtomico_1)):
                booleanoValidador = True
            if(nodoTemporal.dato.getElementoSimbolo().strip() == simbolo_1.strip()):
                booleanoValidador = True
            if(nodoTemporal.dato.getElementoNombreElemento().strip() == nombre_1.strip()):
                booleanoValidador = True
            nodoTemporal = nodoTemporal.siguiente  
        return booleanoValidador 
    def ordenamientoBurbuja(self):
        #las variables hacen referencia al primer elemento de la lista
        actual = self.primero 
        aux = self.primero
        #si la lista está vacía agrega el dato a la lista
        if actual.siguiente != None and aux != None:
            #obtiene el primer dato de la lista
            i = self.primero
            while i != None:
                #obtiene el dato siguiente de la lista
                j = i.siguiente
                while j != None:
                    #compara los datos para saber cual es el mayor
                    if i.dato.getElementoNumAtomico() > j.dato.getElementoNumAtomico():
                        #cambia el orden de los datos
                        temporal = i.dato
                        i.dato = j.dato
                        j.dato = temporal
                    #pasa al siguiente dato de la lista
                    j = j.siguiente
                #pasa al siguiente dato de la lista
                i = i.siguiente

    #METODOS PARA LISTA MAQUINAS
        #IMPRIMIR LISTA MAQUINAS
    def imprimirMaquinas(self):
        nodoTemporal = Nodo("")
        nodoTemporal = self.primero
        while nodoTemporal != None:
            auxiliar =nodoTemporal.dato.listaPinMaquina
            print(nodoTemporal.dato.nombreMaquina + "    |" + str(nodoTemporal.dato.numeroPinesMaquina) +"    |" + str(nodoTemporal.dato.numeroElementosMaquina))
            print(" Lista Pin")
            auxiliar.imprimirListaPin()
            nodoTemporal = nodoTemporal.siguiente
    def imprimirListaPin(self):
        nodoTemporal = Nodo("")
        nodoTemporal = self.primero
        while nodoTemporal != None:
            auxiliar =nodoTemporal.dato.listaelementoPin
            auxiliar.imprimirListaPinElemento()
            nodoTemporal = nodoTemporal.siguiente
    def imprimirListaPinElemento(self):
        nodoTemporal = Nodo("")
        nodoTemporal = self.primero
        while nodoTemporal != None:
            print(nodoTemporal.dato.elementoSimbolo)
            nodoTemporal = nodoTemporal.siguiente      
        #Obtener Lista Compuestos
    def ObtenerMaquinas(self, recibiendoCont):
        contador = 0
        nodoTemporal = Nodo("")
        nodoTemporal = self.primero
        while nodoTemporal != None:
            contador +=1
            if contador == recibiendoCont:
                return nodoTemporal.dato
            nodoTemporal = nodoTemporal.siguiente    
    
    #METODOS PARA LISTA COMPUESTOS
        #Obtener Lista Compuestos
    def ObtenerCompuestos(self, recibiendoCont):
        contador = 0
        nodoTemporal = Nodo("")
        nodoTemporal = self.primero
        while nodoTemporal != None:
            contador +=1
            if contador == recibiendoCont:
                return nodoTemporal.dato
            #print(str(nodoTemporal.dato.getElementoNumAtomico() )+"    |"+ nodoTemporal.dato.getElementoSimbolo() +"    |" + nodoTemporal.dato.getElementoNombreElemento())
            nodoTemporal = nodoTemporal.siguiente
        #IMPRIMIR LISTA COMPUESTOS
    def imprimirCompuesto(self):
        nodoTemporal = Nodo("")
        nodoTemporal = self.primero
        while nodoTemporal != None:
            auxiliar =nodoTemporal.dato.listaElementosCompuesto
            print(nodoTemporal.dato.nombreCompuesto)
            auxiliar.imprimirCompuestoElementos()
            nodoTemporal = nodoTemporal.siguiente
    def imprimirCompuestoElementos(self):
        nodoTemporal = Nodo("")
        nodoTemporal = self.primero
        while nodoTemporal != None:
            print(nodoTemporal.dato.compuestoSimboloElemento)
            nodoTemporal = nodoTemporal.siguiente
    #hacer metodo para obtener el tamaño del elemento mas grande que es el primero de la lista
    def obtenerTamañoPrimero(self):
        nodoTemporal = Nodo("")
        nodoTemporal = self.primero
        if nodoTemporal != None:
            auxiliar =nodoTemporal.dato.listaElementosCompuesto
            return auxiliar.obtenerSize()
    #ordenando compuestos por medio del tamaño de elementos de cada compuesto
    def ordenamientoBurbujaCompuesto(self):
        #las variables hacen referencia al primer elemento de la lista
        actual = self.primero 
        aux = self.primero
        #si la lista está vacía agrega el dato a la lista
        if actual.siguiente != None and aux != None:
            #obtiene el primer dato de la lista
            i = self.primero
            while i != None:
                #obtiene el dato siguiente de la lista
                j = i.siguiente
                while j != None:
                    #compara los datos para saber cual es el mayor
                    i1 =i.dato.listaElementosCompuesto
                    j1 = j.dato.listaElementosCompuesto
                    if i1.obtenerSize() < j1.obtenerSize():
                        #cambia el orden de los datos
                        temporal = i.dato
                        i.dato = j.dato
                        j.dato = temporal
                    #pasa al siguiente dato de la lista
                    j = j.siguiente
                #pasa al siguiente dato de la lista
                i = i.siguiente