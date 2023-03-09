import os
import random
from tkinter import filedialog
import sys
from tkinter.messagebox import showerror, showinfo, showwarning
from xml.dom import minidom
import xml.etree.cElementTree as ET
import graphviz

def cargarArchivo():
    # contadores para saber las cantidades
    contadorCantidad_MaxOrganismo = 0
    contadorMuestra = 0
    contadorCeldaV = 0
    # abre ventana para seleccionar archivo
    urlarchivo = filedialog.askopenfilename(initialdir="./", title="Seleccione un Archivo", filetypes=(("xml", "*.xml"), ("all files", "*.*")))
    # urlarchivo = input()
    if urlarchivo != "":
        documento = minidom.parse(urlarchivo)

        # Se obtienen los datos de la lista organismos
        organismosdoc = documento.getElementsByTagName("organismo")
        for organismodoc in organismosdoc:
            contadorCantidad_MaxOrganismo += 1
            organismo_codigo = organismodoc.getElementsByTagName("codigo")[0]
            organismo_nombre = organismodoc.getElementsByTagName("nombre")[0]
            # print(organismo_codigo.firstChild.data)
            # print(organismo_nombre.firstChild.data)
            if contadorCantidad_MaxOrganismo <= 1000:
                # enviando los parametros al objeto y enviando el objeto a la lista
                objetoOrganismo = Organismo(str(organismo_codigo.firstChild.data).strip(), str(organismo_nombre.firstChild.data).strip())
                colorS = "#"+''.join(random.choice('0123456789ABCDEF')for j in range(6))
                objetoColor = Color(str(organismo_codigo.firstChild.data).strip(), str(colorS).strip(), str(organismo_nombre.firstChild.data).strip())
                # Agregando organismo a la lista de organismos y agregando color al organismo
                lista_Organismos.addFinalNode(objetoOrganismo)
                lista_Colores.addFinalNode(objetoColor)
            else:
                showerror(
                    title="Error", message="El tamaño maximo de organismos es: 1000 \nPorfavor ingrese menos organismos")
                break

        # Se obtienen los datos de listado muestras
        muestrasdoc1 = documento.getElementsByTagName("muestra")
        for muestradoc in muestrasdoc1:
            muestra_codigo = muestradoc.getElementsByTagName("codigo")[0]
            muestra_descripcion = muestradoc.getElementsByTagName("descripcion")[0]
            muestra_filas = muestradoc.getElementsByTagName("filas")[0]
            muestra_columnas = muestradoc.getElementsByTagName("columnas")[0]
            # recorriendo la listaa de celdas vivas
            celdasvivasdoc = muestradoc.getElementsByTagName("celdaViva")
            lista_CeldasVivas = Lista()
            for celdavivadoc in celdasvivasdoc:
                celdaViva_fila = celdavivadoc.getElementsByTagName("fila")[0]
                celdaViva_columna = celdavivadoc.getElementsByTagName("columna")[0]
                celdaViva_codigoOrganismo = celdavivadoc.getElementsByTagName("codigoOrganismo")[
                    0]
                # .......enviando los parametros al objeto y enviando el objeto a la lista
                objetoCeldaViva = CeldaViva(str(celdaViva_fila.firstChild.data).strip(), str(celdaViva_columna.firstChild.data).strip(), str(celdaViva_codigoOrganismo.firstChild.data).strip())
                # Agregando celda viva a la lista de celdas vivas
                if ((int(celdaViva_fila.firstChild.data) <= int(muestra_filas.firstChild.data)) and (int(celdaViva_fila.firstChild.data) > 0) and (int(celdaViva_columna.firstChild.data) <= int(muestra_columnas.firstChild.data)) and (int(celdaViva_columna.firstChild.data) > 0 )):
                    lista_CeldasVivas.addFinalNode(objetoCeldaViva)
                    contadorCeldaV = contadorCeldaV + 1
                else:
                    showerror(title="Error", message="La celda Viva debe estar dentro del valor máximo de:\nfilas: 10000\ncolumnas: 10000 \n El codigo del organismo de la celda viva con el dato de la fila o columna que supera el máximo es:\n" + str(celdaViva_codigoOrganismo.firstChild.data))
                    break

            if ((int(muestra_filas.firstChild.data) <= 10000) and (int(muestra_columnas.firstChild.data) <= 10000)):
                # enviando los parametros al objeto y enviando el objeto a la lista
                objetoMuestra = Muestra(str(muestra_codigo.firstChild.data).strip(), str(muestra_descripcion.firstChild.data).strip(), str(
                    muestra_filas.firstChild.data).strip(), str(muestra_columnas.firstChild.data).strip(), lista_CeldasVivas)
                # Agregando muestra a la lista de muestras
                lista_Muestras.addFinalNode(objetoMuestra)
                contadorMuestra += 1
            else:
                showerror(title="Error", message="La muestra solo puede tener como máximo:\nfilas: 10000\ncolumnas: 10000\nEl codigo de la muestra con el dato de la fila o columna que supera el máximo es:\n" + str(muestra_codigo.firstChild.data))
                break

        showinfo(title="Guardado", message="Archivo leído exitosamente")
        # imprimiendo datos
        # lista_Organismos.printList()
        # crear otro metodo imprimir para la lista de muestras
        # lista_Muestras.printList()
    else :
        print("canceló la opción\n")


if __name__ == '__main__':
    print("Iniciando")