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

    def ordenamientoBurbuja(self):
        actual = self.primero
        aux = self.primero
        #si la lista está vacía agrega el dato a la lista
        if actual.siguiente != None and aux != None:
            i = self.primero
            while i != None:
                j = i.siguiente
                while j != None:
                    if i.dato.getElementoNumAtomico() > j.dato.getElementoNumAtomico():
                        temporal = i.dato
                        i.dato = j.dato
                        j.dato = temporal
                    j = j.siguiente
                i = i.siguiente
        
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



'''


#METODO PARA EL ORDENAMIENTO BURBUJA DE PATRONES
    def ordenamiento(self):
        actual = self.cabeza
        aux = self.cabeza
        if actual.siguiente != None and aux != None:
            i = self.cabeza
            while i != None:
                j = i.siguiente
                while j != None:
                    if(int(ord(i.codigo[0].upper())) > int(ord(j.codigo[0].upper()))):
                        temporal1 = i.codigo
                        temporal2 = i.listaceldas
                        i.codigo = j.codigo
                        i.listaceldas = j.listaceldas
                        j.codigo = temporal1
                        j.listaceldas = temporal2
                    j =j.siguiente
                i = i.siguiente

 #METODO PARA ORDENAR LA LISTA EN ORDEN ALFABETICO POR MEDIO DEL ORDENAMIENTO BURBUJA
    def ordenamiento(self):
        actual = self.cabeza
        aux = self.cabeza
        if actual.siguiente != None and aux != None:
            i = self.cabeza
            while i != None:
                j = i.siguiente
                while(j != None):
                    if int(ord(i.nombre[0].upper())) > int(ord(j.nombre[0].upper())):
                        temporal1 = i.nombre
                        temporal2 = i.fila
                        temporal3 = i.columna
                        temporal4 = i.costointercambiar
                        temporal5 = i.costovoltear
                        temporal6 = i.listapatrones
                        i.nombre = j.nombre
                        i.fila = j.fila
                        i.columna = j.columna
                        i.costointercambiar = j.costointercambiar
                        i.costovoltear = j.costovoltear
                        i.listapatrones = j.listapatrones
                        j.nombre = temporal1
                        j.fila = temporal2
                        j.columna = temporal3
                        j.costointercambiar = temporal4
                        j.costovoltear = temporal5
                        j.listapatrones = temporal6
                    j = j.siguiente
                i = i.siguiente
'''