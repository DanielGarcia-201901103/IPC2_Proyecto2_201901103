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
        if self.primero == None:
            self.primero = nuevoNodo
            self.ultimo = nuevoNodo
        else: 
            self.ultimo.siguiente = nuevoNodo
            self.ultimo = nuevoNodo
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
    #METODOS PARA REALIZAR IMPRESIONES
        #IMPRIMIR LISTA ELEMENTOS
    def ObtenerElementos(self, recibiendoCONT):
        contador = 0
        nodoTemporal = Nodo("")
        nodoTemporal = self.primero
        while nodoTemporal != None:
            contador +=1
            if contador == recibiendoCONT:
                return nodoTemporal.dato
            #print(str(nodoTemporal.dato.getElementoNumAtomico() )+"    |"+ nodoTemporal.dato.getElementoSimbolo() +"    |" + nodoTemporal.dato.getElementoNombreElemento())
            nodoTemporal = nodoTemporal.siguiente 

    def obtenerSize(self):
        return self.size   

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

    #
        #IMPRIMIR LISTA MAQUINAS
    def imprimirMaquinas(self):
        contador = 0
        nodoTemporal = Nodo("")
        nodoTemporal = self.primero
        while nodoTemporal != None:
            contador +=1
            auxiliar =nodoTemporal.dato.listaPinMaquina
            print(nodoTemporal.dato.nombreMaquina + "    |" + str(nodoTemporal.dato.numeroPinesMaquina) +"    |" + str(nodoTemporal.dato.numeroElementosMaquina))
            #print(" Lista Pin")
            auxiliar.imprimirListaPin()
            nodoTemporal = nodoTemporal.siguiente
    def imprimirListaPin(self):
        contador = 0
        nodoTemporal = Nodo("")
        nodoTemporal = self.primero
        while nodoTemporal != None:
            contador +=1
            #print("pin" + str(contador))
            auxiliar =nodoTemporal.dato.listaelementoPin
            auxiliar.imprimirListaPinElemento()
            nodoTemporal = nodoTemporal.siguiente
    def imprimirListaPinElemento(self):
        nodoTemporal = Nodo("")
        nodoTemporal = self.primero
        while nodoTemporal != None:
            print(nodoTemporal.dato.elementoSimbolo)
            nodoTemporal = nodoTemporal.siguiente      
    #
        #IMPRIMIR LISTA COMPUESTOS
    def imprimirCompuesto(self):
        contador = 0
        nodoTemporal = Nodo("")
        nodoTemporal = self.primero
        while nodoTemporal != None:
            contador +=1
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
