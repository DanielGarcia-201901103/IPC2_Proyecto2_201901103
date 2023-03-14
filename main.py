import sys
import tkinter as tk
from tkinter import CENTER, RIGHT, Y, Scrollbar, filedialog, Tk, ttk
from tkinter.messagebox import showerror, showinfo, showwarning
import xml.etree.cElementTree as ET
import graphviz
from lista import Lista
from elemento import Elemento
from compuesto import Compuesto, ElementoCompuesto
from maquina import Maquina , ElementoPin, Pin
import webbrowser
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

def guardarArchivo():
    pass

def inicializacion():
    pass

def gestionarElemento():
    '''
    a. Ver listado de elementos químicos ordenado por número atómico
    b. Agregar un nuevo elemento químico (no deben haber elementos químicos con
        el mismo número atómico, el mismo símbolo o el mismo nombre)
    '''
    menu.withdraw()  # cierra la ventana principal
    gestionar_El = tk.Toplevel()
    gestionar_El.title("Gestionar Elementos Quimicos")
    gestionar_El.geometry("500x300")
    gestionar_El.configure(bg="lightgreen")
    gestionar_El.resizable(False, False)

    def regresarGestionarEaMenu():
            gestionar_El.withdraw()
            menu.iconify()
            menu.deiconify()

    tk.Button(gestionar_El, text="Regresar", width=15, anchor="c", bg="orange", fg="black", font=(
            "Arial Black", 10), command=lambda: regresarGestionarEaMenu()).place(x=300, y=200)
    gestionar_El.mainloop()

def gestionarCompuesto():
    ''' 
    a. Ver listado de compuestos y sus fórmulas
    b. Analizar compuesto
        i. Seleccionar un compuesto
        ii. Ver listado de máquinas y tiempos necesarios para producir el
            compuesto
        iii. Ver gráficamente (utilizando Graphiz) el listado de instrucciones con
                que una máquina puede producir el compuesto'''
    menu.withdraw()  # cierra la ventana principal
    gestionar_Comp = tk.Toplevel()
    gestionar_Comp.title("Gestionar Compuestos")
    gestionar_Comp.geometry("500x300")
    gestionar_Comp.configure(bg="lightgreen")
    gestionar_Comp.resizable(False, False)

    def regresarGestionarCaMenu():
            gestionar_Comp.withdraw()
            menu.iconify()
            menu.deiconify()

    tk.Button(gestionar_Comp, text="Regresar", width=15, anchor="c", bg="orange", fg="black", font=(
            "Arial Black", 10), command=lambda: regresarGestionarCaMenu()).place(x=300, y=200)
    gestionar_Comp.mainloop()

def gestionarMaquinas():
    #a. Listado de máquinas
    menu.withdraw()  # cierra la ventana principal
    gestionar_Maq = tk.Toplevel()
    gestionar_Maq.title("Gestionar Maquinas")
    gestionar_Maq.geometry("500x300")
    gestionar_Maq.configure(bg="lightgreen")
    gestionar_Maq.resizable(False, False)

    def regresarGestionarMaMenu():
            gestionar_Maq.withdraw()
            menu.iconify()
            menu.deiconify()

    tk.Button(gestionar_Maq, text="Regresar", width=15, anchor="c", bg="orange", fg="black", font=(
            "Arial Black", 10), command=lambda: regresarGestionarMaMenu()).place(x=300, y=200)
    gestionar_Maq.mainloop()

def documentacion():
    #cambiar la direccion del archivo para que se abra la documentacion de este proyecto
    pathTecnico = "Proyecto1\Documentacion\Manual Tecnico.pdf" 
    webbrowser.open_new(pathTecnico)

def info():
    showinfo(title="Información del desarrollador", message="Josué Daniel Rojché García\nCarnet: 201901103")

def salir():
    # menu.destroy()
    sys.exit()
    
if __name__ == '__main__':
    menu = tk.Tk()
    menu.title("PROYECTO NO.1")
    menu.geometry("607x400")
    menu.configure(bg="#212F3C")
    menu.resizable(False, False)

    tk.Label(menu, text="Menu", bg="#000000", fg="#FFFFFF",width= 33, font=("Arial", 13)).grid(row=0,column=0)
    tk.Label(menu, text="Ayuda", bg="#000000", fg="#FFFFFF",width= 33, font=("Arial", 13)).grid(row=0,column=1)

    tk.Button(menu, text="Abrir", width=20, anchor="c", bg="#895C09", fg="Black", font=("Arial Black", 10), command=lambda: cargarArchivo()).place(x=70, y=60)
    tk.Button(menu, text="Guardar", width=20, anchor="c", bg="#895C09", fg="Black", font=("Arial Black", 10), command=lambda: guardarArchivo()).place(x=70, y=105)
    tk.Button(menu, text="Gestionar Elementos", width=20, anchor="c", bg="#895C09", fg="Black", font=("Arial Black", 10), command=lambda: gestionarElemento()).place(x=70, y=150)
    tk.Button(menu, text="Gestionar Compuestos", width=20, anchor="c", bg="#895C09", fg="Black", font=("Arial Black", 10), command=lambda: gestionarCompuesto()).place(x=70, y=195)
    tk.Button(menu, text="Gestionar Maquinas", width=20, anchor="c", bg="#895C09", fg="Black", font=("Arial Black", 10), command=lambda: gestionarMaquinas()).place(x=70, y=240)
    tk.Button(menu, text="Inicialización", width=20, anchor="c", bg="#895C09", fg="Black", font=("Arial Black", 10), command=lambda: inicializacion()).place(x=70, y=285)
    tk.Button(menu, text="Salir", width=20, anchor="c", bg="#895C09", fg="Black", font=("Arial Black", 10), command=lambda: salir()).place(x=70, y=330)
    
    tk.Button(menu, text="Documentación", width=20, anchor="c", bg="#895C09", fg="Black", font=("Arial Black", 10), command=lambda: documentacion()).place(x=370, y=60)
    tk.Button(menu, text="Desarrollador", width=20, anchor="c", bg="#895C09", fg="Black", font=("Arial Black", 10), command=lambda: info()).place(x=370, y=105)

    menu.mainloop() # Permite mostrar la ventana 