import sys
import tkinter as tk
from tkinter import CENTER, RIGHT, Y, Scrollbar, filedialog, Tk, ttk, Frame, END
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
                        objetoElemento = Elemento(int(elemento_numeroAtomico), str(elemento_simbolo).strip(),str(elemento_nombreElemento).strip())
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
                                            ObjetoelementoPin = ElementoPin(str(pin_simboloElemento).strip())
                                            listaelementoPin.insertarFinal(ObjetoelementoPin)
                                ObjetoPinMaquina = Pin(listaelementoPin)
                                liPinMaquina.insertarFinal(ObjetoPinMaquina)
                        #aca se guarda la lista maquinas 
                        objetoMaquina = Maquina(str(maquinaDatos_nombre).strip(),int(maquinaDatos_numeroPines), int(maquinaDatos_numeroElementos), liPinMaquina)  
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
                                    objetoElementoCompuesto = ElementoCompuesto(str(compuesto_elemento).strip())
                                    liElementosCompuesto.insertarFinal(objetoElementoCompuesto)
                        #objeto
                        objetoCompuesto = Compuesto(str(compuesto_nombre).strip(),liElementosCompuesto)
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
        listaElementos.ordenamientoBurbuja()
        listaCompuestos.ordenamientoBurbujaCompuesto()
    else :
        print("canceló la opción\n")

def guardarArchivo():
    if listaCompuestos.estaVacia() == True:
        pass
    elif listaCompuestos.estaVacia() == False:
        showwarning(title="Advertencia", message="Porfavor primero cargue un archivo.")

def inicializacion():
    listaElementos.inicializarLista()
    listaMaquinas.inicializarLista()
    listaCompuestos.inicializarLista()

def gestionarElemento():
    if listaElementos.estaVacia() == True:
        menu.withdraw()  # cierra la ventana principal
        gestionar_El = tk.Toplevel()
        gestionar_El.title("Gestionar Elementos Quimicos")
        gestionar_El.config(bg= "lightgreen")
        gestionar_El.geometry("600x545")
        gestionar_El.resizable(False, False)

        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview", background="silver",foreground="black", rowheight=25, fieldbackground="silver")
        style.map("Treeview", background=[("selected", "green")])

        scroll_bar = Scrollbar(gestionar_El)
        scroll_bar.pack(side=RIGHT, fill=Y)

        tablaDinamica = ttk.Treeview(gestionar_El, yscrollcommand=scroll_bar.set, columns=("col1", "col2", "col3"))
        scroll_bar.config(command=tablaDinamica.yview)
        tablaDinamica.column("#0", width=20)
        tablaDinamica.column("col1", width=120, anchor=CENTER)
        tablaDinamica.column("col2", width=80, anchor=CENTER)
        tablaDinamica.column("col3", width=120, anchor=CENTER)

        tablaDinamica.heading("#0", text="No.", anchor=CENTER)
        tablaDinamica.heading("col1", text="Número Atómico", anchor=CENTER)
        tablaDinamica.heading("col2", text="Simbolo", anchor=CENTER)
        tablaDinamica.heading("col3", text="Nombre Elemento", anchor=CENTER)
        # agregando estilo a las filas
        tablaDinamica.tag_configure("oddrow", background="white")
        tablaDinamica.tag_configure("evenrow", background="lightblue")

        # AGREGANDO LISTA DE OBJETOS A LA TABLA DE ACUERDO AL TAMAÑO DE LA LISTA.
        iterador = 1
        while iterador <= listaElementos.obtenerSize():
            auxiliarListaElementos =listaElementos.ObtenerElementos(iterador)
            numAtomEl = auxiliarListaElementos.getElementoNumAtomico()
            simboloEl = auxiliarListaElementos.getElementoSimbolo()
            nomEl = auxiliarListaElementos.getElementoNombreElemento()
            if iterador % 2 == 0:
                tablaDinamica.insert("", tk.END, text= str(iterador), values=(str(numAtomEl), simboloEl, nomEl), tags=("evenrow",))
            else:
                tablaDinamica.insert("", tk.END, text = str(iterador), values=(str(numAtomEl), simboloEl, nomEl), tags=("oddrow",))

            iterador +=1

        tablaDinamica.place(x = 20 , y = 20 , width= 545, height= 310 )

        tk.Label(gestionar_El, text="Nuevo elemento quimico", bg="#000000", fg="#FFFFFF",width= 40, font=("Arial", 13)).place(x= 0, y= 350)
        tk.Label(gestionar_El, text="", bg="#000000", fg="#FFFFFF",width= 40, font=("Arial", 13)).place(x= 0, y= 520)
        tk.Label(gestionar_El, text="", bg="#000000", fg="#FFFFFF",height= 10,width= 2, font=("Arial", 13)).place(x= 360, y= 350)
        tk.Label(gestionar_El, text="", bg="#000000", fg="#FFFFFF",height= 10,width= 2, font=("Arial", 13)).place(x= 0, y= 350)
        tk.Label(gestionar_El, text="Número Atómico:", bg="lightgreen", fg="black", font=("Calibri", 13)).place(x=30, y=385)
        tk.Label(gestionar_El, text="Símbolo:", bg="lightgreen", fg="black", font=("Calibri", 13)).place(x=30, y=415)
        tk.Label(gestionar_El, text="Nombre:", bg="lightgreen", fg="black", font=("Calibri", 13)).place(x=30, y=445)

        #CUADROS DE ENTRADA DE TEXTO
        entradaNumAtomico = tk.StringVar()
        entrada_NumAtomico = ttk.Entry(gestionar_El, textvariable = entradaNumAtomico, width=30).place(x=160, y=390)
        entradaSimbolo= tk.StringVar()
        entrada_Simbolo = ttk.Entry(gestionar_El, textvariable = entradaSimbolo, width=30).place(x=160, y=420)
        entradaNombre = tk.StringVar()
        entrada_Nombre = ttk.Entry(gestionar_El, textvariable = entradaNombre, width=30).place(x=160, y=450)

        def regresarGestionarEaMenu():
                gestionar_El.withdraw()
                menu.iconify()
                menu.deiconify()

        def agregarElementoQ():
            numeroAtomico_1 = str(entradaNumAtomico.get())
            simbolo_1 = str(entradaSimbolo.get())
            nombre_1 = str(entradaNombre.get())

            #obteniendo datos y compararlos con los datos ingresados por el usuario 

            bolleanoElementosRepetidos = listaElementos.validarRepetidos(int(numeroAtomico_1), simbolo_1.strip(), nombre_1.strip())

            #si los datos ingresados son iguales a los que existen en la tabla entonces indicar un mensaje de no ingresar datos repetidos
            if bolleanoElementosRepetidos == True:
                showerror(title="No es aceptado", message="Por favor no introduzca datos que ya existan en la tabla.")
            elif bolleanoElementosRepetidos == False:
                auxObjetoElemento = Elemento(int(numeroAtomico_1), simbolo_1 , nombre_1 )
                listaElementos.insertarFinal(auxObjetoElemento)
                showinfo(title="Guardado", message="Datos almacenados correctamente")
                listaElementos.ordenamientoBurbuja()
        tk.Button(gestionar_El, text="Agregar", width=15, anchor="c", bg="orange", fg="black", font=("Arial Black", 10), command=lambda:    agregarElementoQ()).place(x=160, y=485)
        tk.Button(gestionar_El, text="Regresar", width=15, anchor="c", bg="red", fg="black", font=("Arial Black", 10), command=lambda:  regresarGestionarEaMenu()).place(x=430, y=450)

        gestionar_El.mainloop()
    elif listaElementos.estaVacia() == False:
        showwarning(title="Advertencia", message="Porfavor primero cargue un archivo.")

def gestionarCompuesto():
    if listaCompuestos.estaVacia() == True:
        menu.withdraw()  # cierra la ventana principal
        gestionar_Comp = tk.Toplevel()
        gestionar_Comp.title("Gestionar Compuestos")
        gestionar_Comp.geometry("800x545")
        gestionar_Comp.configure(bg="lightgreen")
        gestionar_Comp.resizable(True, False)

        style1 = ttk.Style()
        style1.theme_use("default")
        style1.configure("Treeview", background="silver",foreground="black", rowheight=25, fieldbackground="silver")
        style1.map("Treeview", background=[("selected", "green")])

        scroll_bar1 = Scrollbar(gestionar_Comp)
        scroll_bar1.pack(side=RIGHT, fill=Y)
        #hacer que la tabla tenga la cantidad de columnas de acuerdo al compuesto con mas elementos en la lista
        #Agregar cada columna con un elemento y la primer columna tendra solo el nombre del compuesto

        tama = listaCompuestos.obtenerTamañoPrimero()
        i = 1
        listaauxiliar = []
        while i <= int(tama):
            cadenaCOlumna = "col" + str(i)
            listaauxiliar.append(cadenaCOlumna)
            i +=1

        columnas = tuple(listaauxiliar)
        tablaDinamica1 = ttk.Treeview(gestionar_Comp, yscrollcommand=scroll_bar1.set, columns= columnas)
        scroll_bar1.config(command=tablaDinamica1.yview)

        tablaDinamica1.column("#0", width=100)
        tablaDinamica1.heading("#0", text="Compuesto", anchor=CENTER)
        aumenta = 1
        for ii in columnas:
            tablaDinamica1.column(ii, width=80, anchor=CENTER)
            tablaDinamica1.heading(ii, text="elemento "+ str(aumenta), anchor=CENTER)
            aumenta +=1

        # agregando estilo a las filas
        tablaDinamica1.tag_configure("oddrow", background="white")
        tablaDinamica1.tag_configure("evenrow", background="lightblue")

        # AGREGANDO LISTA DE OBJETOS A LA TABLA DE ACUERDO AL TAMAÑO DE LA LISTA.
        iterador1 = 1
        while iterador1 <= listaCompuestos.obtenerSize():
            #se almacena en un dato auxiliar la l
            auxiliarListadatosCompuesto = listaCompuestos.ObtenerCompuestos(iterador1)
            auxiliarListadatosCompuesto.nombreCompuesto
            auxiLista = auxiliarListadatosCompuesto.listaElementosCompuesto
            iterador11 = 1
            listaauxiliar1 = []
            while iterador11 <= auxiLista.obtenerSize():
                elementoObtenido = auxiLista.ObtenerCompuestos(iterador11)
                listaauxiliar1.append(str(elementoObtenido.compuestoSimboloElemento))
                iterador11 += 1
            auxiliarColumna = tuple(listaauxiliar1)
            if iterador1 % 2 == 0:
                tablaDinamica1.insert("", tk.END, text= str(auxiliarListadatosCompuesto.nombreCompuesto), values=auxiliarColumna, tags=("evenrow",))
            else:
                tablaDinamica1.insert("", tk.END, text = str(auxiliarListadatosCompuesto.nombreCompuesto), values=auxiliarColumna, tags=("oddrow",))
            iterador1 += 1
        #tablaDinamica1.pack()
        tablaDinamica1.place(x = 20 , y = 20 , height= 310 )

        ''' 
        
        b. Analizar compuesto
            i. Seleccionar un compuesto
            ii. Ver listado de máquinas y tiempos necesarios para producir el
                compuesto
            iii. Ver gráficamente (utilizando Graphiz) el listado de instrucciones con
                    que una máquina puede producir el compuesto'''

        tk.Label(gestionar_Comp, text="Analizar Compuesto", bg="#000000", fg="#FFFFFF",width= 40, font=("Arial", 13)).place(x= 0, y= 350)
        tk.Label(gestionar_Comp, text="", bg="#000000", fg="#FFFFFF",width= 40, font=("Arial", 13)).place(x= 0, y= 520)
        tk.Label(gestionar_Comp, text="", bg="#000000", fg="#FFFFFF",height= 10,width= 2, font=("Arial", 13)).place(x= 350, y= 350)
        tk.Label(gestionar_Comp, text="", bg="#000000", fg="#FFFFFF",height= 10,width= 2, font=("Arial", 13)).place(x= 0, y= 350)
        tk.Label(gestionar_Comp, text="Seleccionar Compuesto", bg="lightgreen", fg="black", font=("Arial Black", 13)).place(x=75, y=385)
        tk.Label(gestionar_Comp, text="Nombre Compuesto:", bg="lightgreen", fg="black", font=("Calibri", 13)).place(x=30, y=415)

        #CUADROS DE ENTRADA DE TEXTO
        entradaNombreCompu= tk.StringVar()
        entrada_NombreCompu = ttk.Entry(gestionar_Comp, textvariable = entradaNombreCompu, width=25).place(x=190, y=420)

        def obteniendoSeleccion():
            try:
                nameCompuesto = str(entradaNombreCompu.get())
                realizarInstruccion(nameCompuesto.lower())
            except Exception as e:
                showwarning(title="Advertencia", message="No ha seleccionado ningún compuesto.")
        def verListadoMaquinasTiempos():
            "crear tabla "
            
        def verInstruccionesGraficas():
            "usar graphviz"

        def regresarGestionarCaMenu():
                gestionar_Comp.withdraw()
                menu.iconify()
                menu.deiconify()

        tk.Button(gestionar_Comp, text="Seleccionar", width=15, anchor="c", bg="orange", fg="black", font=("Arial Black", 10), command=lambda: obteniendoSeleccion()).place(x=110, y=460)
        tk.Button(gestionar_Comp, text="Ver listado maquinas y tiempos", width=35, anchor="c", bg="orange", fg="black", font=("Arial Black", 10), command=lambda: verListadoMaquinasTiempos()).place(x=415, y=400)
        tk.Button(gestionar_Comp, text="Ver instrucciones graficas", width=35, anchor="c", bg="orange", fg="black", font=("Arial Black", 10), command=lambda: verInstruccionesGraficas()).place(x=415, y=450)
        tk.Button(gestionar_Comp, text="Regresar", width=15, anchor="c", bg="red", fg="black", font=("Arial Black", 10), command=lambda: regresarGestionarCaMenu()).place(x=600, y=500)
        gestionar_Comp.mainloop()
    elif listaCompuestos.estaVacia() == False:
        showwarning(title="Advertencia", message="Porfavor primero cargue un archivo.")

def realizarInstruccion(nameCompuesto):
    contadorSegundos = 0
    compuestoBuscar = nameCompuesto
    auxiliarListaElemento =listaCompuestos.buscarCompuesto(compuestoBuscar)
    iterador = 1
    while iterador <= auxiliarListaElemento.obtenerSize():
        cElemento = auxiliarListaElemento.ObtenerCompuestos(iterador)

        print(str(cElemento.compuestoSimboloElemento))
        iterador1 = 1
        print("cantidad maquinas:"+ str(listaMaquinas.obtenerSize()))
        while iterador1 <= listaMaquinas.obtenerSize():
            auxiliarM = listaMaquinas.ObtenerMaquinas(iterador1)
            auxiliarPines = auxiliarM.listaPinMaquina
            iterador2 =1
            print("Cantidad Pines:"+str(auxiliarPines.obtenerSize()))
            while iterador2 <= auxiliarPines.obtenerSize():
                auxiliarElementos = auxiliarPines.ObtenerMaquinas(iterador2)
                elementosAux =auxiliarElementos.listaelementoPin
                #print("Pin")
                iterador3 =1
                print("cantidad elementos:"+str(elementosAux.obtenerSize()))
                while iterador3 <= elementosAux.obtenerSize():
                    el = elementosAux.ObtenerMaquinas(iterador3)
                    #print(el.elementoSimbolo)
                    if str(cElemento.compuestoSimboloElemento) == el.elementoSimbolo:
                        print("Fusionar")
                        print(el.elementoSimbolo)
                    else: 
                        print("mover")
                    iterador3 +=1
                iterador2 +=1
            iterador1 +=1
        #quitar los whiles y obtener la cantidad de pines de la maquina para recorrer el primer pin y segundo pin como primera iteracion
        contadorSegundos +=1
        iterador +=1
    '''
            cada pin de la maquina puede realizar las siguientes funciones
            moverse hacia adelante
            moverse hacia atras
            esperar
            fusionar elemento quimico

            restricciones de la maquina para crear compuestos
            Solo puede fusionar un elemento quimico a la vez
            solo debe contener una vez cada elemento quimico

            ii. Ver listado de máquinas y tiempos necesarios para 
                producir el compuesto
            iii. Ver gráficamente (utilizando Graphiz) el listado 
                de instrucciones conm que una máquina puede producir
                el compuesto
            Algoritmo
            1. Seleccionar el compuesto de la tabla.
            2. Obtener el primer elemento del compuesto.
            3. Buscar el elemento en los pines de la maquina
                3.0 validar si es estado inicial entonces mover hacia adelante
                en todos los pines.
                    3.0.1 aumentar en una unidad el segundo.
                    3.0.2 verificar si existe coincidencia del elemento entre los
                    pines.
                        3.0.2.1 Si no coincide mover hacia adelante en todos los 
                        pines al mismo tiempo y volver a validar coincidencia
                        3.0.2.2 Si coincide en uno de los pines, entonces
                        Esperar en los otros pines, y al mismo tiempo que Espera
                        fusionar elemento.
                3.1 si no es igual a estado inicial entonces buscar hacia atras y adelante
                    si existe coincidencia de elementos en los pines.
                    3.1.1 si existe coincidencia entonces aumentar un segundo, fusionar elemento
                    y que los demas elementos esperen 
            3.3 Eliminar el primer elemento de la lista de compuesto.
            4. repetir el paso 3

            '''
def gestionarMaquinas():
    if listaMaquinas.estaVacia() == True:
        menu.withdraw()  # cierra la ventana principal
        gestionar_Maq = tk.Toplevel()
        gestionar_Maq.title("Gestionar Maquinas")
        gestionar_Maq.geometry("600x500")
        gestionar_Maq.configure(bg="lightgreen")
        gestionar_Maq.resizable(False, False)

        #realizar una tabla donde se mostrará principalmente el nombre de la maquina, numero de pines, numero de elementos , pin1, pin2, etc
        #a cada pin agregarle el arbol mostrando los elementos de cada pin, ver video adjunto o indicar que selecciones la maquina para ver la lista de pines por aparte.
        # https://www.youtube.com/watch?v=gUHFasQBwO4
        #https://es.stackoverflow.com/questions/172226/mostrar-datos-de-una-tabla-de-access-en-tkinter/172386#172386


        style3 = ttk.Style()
        style3.theme_use("default")
        style3.configure("Treeview", background="silver",foreground="black", rowheight=25, fieldbackground="silver")
        style3.map("Treeview", background=[("selected", "green")])

        scroll_bar3 = Scrollbar(gestionar_Maq)
        scroll_bar3.pack(side=RIGHT, fill=Y)

        tablaDinamica3 = ttk.Treeview(gestionar_Maq, yscrollcommand=scroll_bar3.set, columns=("col1", "col2", "col3"))
        scroll_bar3.config(command=tablaDinamica3.yview)
        tablaDinamica3.column("#0", width=20)
        tablaDinamica3.column("col1", width=120, anchor=CENTER)
        tablaDinamica3.column("col2", width=80, anchor=CENTER)
        tablaDinamica3.column("col3", width=120, anchor=CENTER)

        tablaDinamica3.heading("#0", text="No.", anchor=CENTER)
        tablaDinamica3.heading("col1", text="Nombre", anchor=CENTER)
        tablaDinamica3.heading("col2", text="Número de Pines", anchor=CENTER)
        tablaDinamica3.heading("col3", text="Número de elementos", anchor=CENTER)
        # agregando estilo a las filas
        tablaDinamica3.tag_configure("oddrow", background="white")
        tablaDinamica3.tag_configure("evenrow", background="lightblue")

        # AGREGANDO LISTA DE OBJETOS A LA TABLA DE ACUERDO AL TAMAÑO DE LA LISTA.
        iterador = 1
        while iterador <= listaMaquinas.obtenerSize():
            auxiliarListaMaquina = listaMaquinas.ObtenerMaquinas(iterador)
            nombreMa = auxiliarListaMaquina.nombreMaquina
            numeroPinesMa = auxiliarListaMaquina.numeroPinesMaquina
            numeroElementosMa = auxiliarListaMaquina.numeroElementosMaquina
            if iterador % 2 == 0:
                tablaDinamica3.insert("", tk.END, text= str(iterador), values=(str(nombreMa), str(numeroPinesMa), str(numeroElementosMa)), tags=("evenrow",))
            else:
                tablaDinamica3.insert("", tk.END, text = str(iterador), values=(str(nombreMa), str(numeroPinesMa), str(numeroElementosMa)), tags=("oddrow",))
            iterador +=1
        tablaDinamica3.place(x = 20 , y = 20 , width= 545, height= 310 )

        def regresarGestionarMaMenu():
                gestionar_Maq.withdraw()
                menu.iconify()
                menu.deiconify()
        tk.Button(gestionar_Maq, text="Regresar", width=15, anchor="c", bg="red", fg="black", font=(
                "Arial Black", 10), command=lambda: regresarGestionarMaMenu()).place(x=430, y=450)
        gestionar_Maq.mainloop()
    elif listaMaquinas.estaVacia() == False:
        showwarning(title="Advertencia", message="Porfavor primero cargue un archivo.")

def documentacion():
    #cambiar la direccion del archivo para que se abra la documentacion de este proyecto
    pathTecnico = "Documentacion\FtoArticuloEnsayo-IPC2-lab.pdf" 
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