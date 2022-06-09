import sys
import os 
from tkinter import N


#python3 prog.py /path Cambio NewWord New_dir_name

Archivos=sys.argv #Lista con los argumentos (archivos)

path=os.listdir(Archivos[1])
Cambio_palabra=Archivos[2]
Nueva_palabra=Archivos[3]

if os.path.exists(Archivos[4]) is False:
    Dir_name=os.mkdir(Archivos[4])
else:
    pass

for Archivo in path: #para cada dentro del directorio
    if os.path.isfile(Archivos[1]+"\\"+Archivo) is True:
        Archivo_original=open(Archivos[1]+"\\"+Archivo,'r')
        Archivo_Nuevo=open(Archivos[4]+"\\"+Archivo.replace(Cambio_palabra, Nueva_palabra),'w')
        for linea in Archivo_original: #para cada linea de Archivo
            if Cambio_palabra in linea: #si esta la palabra que se desea cambiar dentro de la variable "linea"
                nueva_linea=linea.replace(Cambio_palabra, Nueva_palabra)
                Archivo_Nuevo.write(nueva_linea)
            else:
                Archivo_Nuevo.write(linea)
        Archivo_Nuevo.close()
        Archivo_original.close()