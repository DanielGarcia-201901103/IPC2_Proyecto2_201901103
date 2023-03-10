import os
import random
from tkinter import filedialog
import sys
from tkinter.messagebox import showerror, showinfo, showwarning
import xml.etree.cElementTree as ET
import graphviz
from lista import Lista
from elemento import Elemento
from compuesto import Compuesto, ElementoCompuesto
from maquina import Maquina , ElementoPin, Pin

#Variables de lista
listaElementos = Lista()
listaMaquinas = Lista()
listaCompuestos = Lista()

def cargarArchivo():
    #usando element tree
    
    # abre ventana para seleccionar archivo
    urlarchivo = filedialog.askopenfilename(initialdir="./", title="Seleccione un Archivo", filetypes=(("xml", "*.xml"), ("all files", "*.*")))
    # urlarchivo = input()
    if urlarchivo != "":
        documento = ET.parse(urlarchivo)
        #Obtiene la raíz CONFIG
        root = documento.getroot() 
        #dentro de la raíz recorre los hijos
        for elemento in root: 
            if elemento.tag == "listaElementos":
                for elemento1 in elemento:
                    if elemento1.tag == "elemento":
                        for elemento2 in elemento1:
                            if elemento2.tag == "numeroAtomico":
                                elemento_numeroAtomico = elemento2.text
                            elif elemento2.tag == "simbolo":
                                elemento_simbolo = elemento2.text
                            elif elemento2.tag == "nombreElemento":
                                elemento_nombreElemento = elemento2.text
                        #Aca se envia al objeto listaElementos elemento
                        objetoElemento = Elemento(int(elemento_numeroAtomico), str(elemento_simbolo),str(elemento_nombreElemento))
                        #enviando objeto a la lista
                        listaElementos.insertarFinal(objetoElemento)
            elif elemento.tag == "listaMaquinas":
                for maquina in elemento:
                    if maquina.tag == "Maquina":
                        liPinMaquina = Lista()
                        for maquinaDatos in maquina:
                            if maquinaDatos.tag == "nombre":
                                maquinaDatos_nombre = maquinaDatos.text
                            elif maquinaDatos.tag == "numeroPines":
                                maquinaDatos_numeroPines = maquinaDatos.text
                            elif maquinaDatos.tag == "numeroElementos":
                                maquinaDatos_numeroElementos = maquinaDatos.text
                            elif maquinaDatos.tag == "pin":
                                for elementos in maquinaDatos:
                                    if elementos.tag == "elementos":
                                        listaelementoPin = Lista()
                                        for elementos1 in elementos:
                                            if elementos1.tag == "elemento":
                                                pin_simboloElemento = elementos1.text
                                            ObjetoelementoPin = ElementoPin(pin_simboloElemento)
                                            listaelementoPin.insertarFinal(ObjetoelementoPin)
                                ObjetoPinMaquina = Pin(listaelementoPin)
                                liPinMaquina.insertarFinal(ObjetoPinMaquina)
                        #aca se guarda la lista maquinas 
                        objetoMaquina = Maquina(str(maquinaDatos_nombre),int(maquinaDatos_numeroPines), int(maquinaDatos_numeroElementos), liPinMaquina)  
                        listaMaquinas.insertarFinal(objetoMaquina)                        
            elif elemento.tag == "listaCompuestos":
                for compuestos in elemento:
                    if compuestos.tag == "compuesto":
                        for compuestosDatos in compuestos:
                            if compuestosDatos.tag == "nombre":
                                compuesto_nombre = compuestosDatos.text
                            elif compuestosDatos.tag == "elementos":
                                liElementosCompuesto = Lista()
                                for compuestoDElemento in compuestosDatos:
                                    if compuestoDElemento.tag == "elemento":
                                        compuesto_elemento = compuestoDElemento.text
                                    objetoElementoCompuesto = ElementoCompuesto(compuesto_elemento)
                                    liElementosCompuesto.insertarFinal(objetoElementoCompuesto)
                        #objeto
                        objetoCompuesto = Compuesto(str(compuesto_nombre),liElementosCompuesto)
                        listaCompuestos.insertarFinal(objetoCompuesto)
        showinfo(title="Guardado", message="Archivo leído exitosamente")
        # imprimiendo datos
        #print("Lista de elementos")
        #print("numeroAtomico    |simbolo    |nombreElemento")
        #listaElementos.imprimirElementos()
        #print("Lista de Compuestos")
        #listaCompuestos.imprimirCompuesto()
        #print("Lista de maquinas")
        #listaMaquinas.imprimirMaquinas()
    else :
        print("canceló la opción\n")


if __name__ == '__main__':
    cargarArchivo()