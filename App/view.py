"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
from DISClib.DataStructures import arraylist as ar
from tabulate import tabulate

default_limit = 1000
sys.setrecursionlimit(default_limit*10)
from DISClib.ADT import map as mp

def castBoolean(value):
    """
    Convierte un valor a booleano
    """
    if value in ('True', 'true', 'TRUE', 'T', 't', '1', 1, True):
        return True
    else:
        return False
    
def printAnswer(answer):
    """
    Imprime los datos de tiempo y memoria de la carga de datos
    """
    
    if answer[2]==0:
        print("Tiempo [ms]: ", f"{answer[1]:.3f}")
    else:
        print("Tiempo [ms]: ", f"{answer[1]:.3f}", "||",
              "Memoria [kB]: ", f"{answer[2]:.3f}")
"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
def cargadatosgames(lista): 
   
    list_aux=[]
    list_aux_=[]
    size=lt.size(lista)
    if size<6:
        for i in lt.iterator(lista):
            list_aux.append(i)
    else:
        list_aux.append(lt.getElement(lista,2))
        list_aux.append(lt.getElement(lista,3))
        list_aux.append(lt.getElement(lista,4))
        list_aux.append(lt.getElement(lista,size-2))
        list_aux.append(lt.getElement(lista,size-1))
        list_aux.append(lt.getElement(lista,size))
    for info in list_aux:
        list_aux2=["","","","","","","","","","",""]
        list_aux2[0]=lt.getElement(info,1)
        list_aux2[1]=lt.getElement(info,2)
        list_aux2[2]=lt.getElement(info,3)
        list_aux2[3]=lt.getElement(info,4)
        list_aux2[4]=lt.getElement(info,5)
        list_aux2[5]=lt.getElement(info,6)
        list_aux2[6]=lt.getElement(info,7)
        list_aux2[7]=lt.getElement(info,8)
        list_aux2[8]=lt.getElement(info,9)
        list_aux2[9]=lt.getElement(info,10)
        list_aux2[10]=lt.getElement(info,11)



        list_aux_.append(list_aux2)
    cabecero=["Año","Codigo Actividad Economico","Nombre Actividad Economico","Codigo Sector Economico","Nombre sector economico","Codigo subsector economico","Nombre subsector economico","Total ingresos netos","Total costos y gastos", "Total saldo a pagar", "Total saldo a favor"]
    print(tabulate(list_aux_,headers=cabecero,tablefmt="grid",maxcolwidths=[5,10,20,10,20,10,20,10,10,10,10]))
    



def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- ")

catalog = controller.newController()
catalog=catalog["model"]

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Desea observar el uso de memoria? (True/False)")
        mem = input("Respuesta: ")
        mem = castBoolean(mem)
        print("Cargando información de los archivos ....")
        answer=controller.loadData(catalog,memflag=mem)
        catalog=answer[0]
        printAnswer(answer)

       
        cargadatosgames((catalog["data"]))
          
 

             
        

    elif int(inputs[0]) == 2:
        answer=controller.req_1(catalog)
        cargadatosgames(answer)

    else:
        sys.exit(0)
sys.exit(0)

