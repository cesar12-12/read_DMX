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
        #print('Abri el archivo: '+Archivo)
        Archivo_Nuevo=open(Archivos[4]+"\\"+Archivo.replace(Cambio_palabra, Nueva_palabra),'w')
        #print('Cree el archivo: '+Archivo.replace(Cambio_palabra, Nueva_palabra))
        try:
            for linea in Archivo_original: #para cada linea de Archivo
                if Cambio_palabra in linea: #si esta la palabra que se desea cambiar dentro de la variable "linea"
                    nueva_linea=linea.replace(Cambio_palabra, Nueva_palabra)
                    Archivo_Nuevo.write(nueva_linea)
                else:
                    Archivo_Nuevo.write(linea)
            Archivo_Nuevo.close()
        except:
            Archivo_Nuevo.close()
            os.remove(Archivo.replace(Cambio_palabra, Nueva_palabra))
            Archivo_Lista=open(Archivos[4]+"\\"+'ArchivosNoCopiados.txt', 'w')
            Archivo_Lista.write('No pude abrir los siguientes archivos:')
            for linea in Archivo_Lista:
                Archivo_Lista.write(Archivo) 
            Archivo_Lista.close()
            #print('No pude abrir el archivo: %s' % Archivo)
        #print('Cerre el archivo ' +Archivo.replace(Cambio_palabra, Nueva_palabra))
        Archivo_original.close()
        #print('Cerre el archivo original '+Archivo)