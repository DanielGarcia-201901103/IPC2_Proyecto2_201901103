class Maquina:
    def __init__(self, nombreMaquina, numeroPinesMaquina, numeroElementosMaquina, listaPinMaquina):
        self.nombreMaquina = nombreMaquina
        self.numeroPinesMaquina = numeroPinesMaquina
        self.numeroElementosMaquina = numeroElementosMaquina
        self.listaPinMaquina = listaPinMaquina

class Pin:
    def __init__(self,listaelementoPin):
        self.listaelementoPin = listaelementoPin

class ElementoPin:
    def __init__(self,elementoSimbolo):
        self.elementoSimbolo = elementoSimbolo