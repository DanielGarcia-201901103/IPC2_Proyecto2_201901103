class Elemento:
    def __init__(self, elementoNumeroAtomico, elementoSimbolo, elementoNombreElemento):
        self.elementoNumeroAtomico = elementoNumeroAtomico
        self.elementoSimbolo = elementoSimbolo
        self.elementoNombreElemento = elementoNombreElemento

    def setElementoNumAtomico(self,elementoNumeroAtomico):
        self.elementoNumeroAtomico = elementoNumeroAtomico

    def getElementoNumAtomico(self):
        return self.elementoNumeroAtomico
    
    def setElementoSimbolo(self,elementoSimbolo):
        self.elementoSimbolo = elementoSimbolo

    def getElementoSimbolo(self):
        return self.elementoSimbolo
    
    def setElementoNombreElemento(self,elementoNombreElemento):
        self.elementoNombreElemento = elementoNombreElemento
        
    def getElementoNombreElemento(self):
        return self.elementoNombreElemento