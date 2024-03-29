﻿"""
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
def cargadatos(lista): 
    list_aux=[]
    list_aux_=[]
    size=lt.size(lista)
    if size<6:
        for i in lt.iterator(lista):
            list_aux.append(i)
    else:
        list_aux.append(lt.getElement(lista,1))
        list_aux.append(lt.getElement(lista,2))
        list_aux.append(lt.getElement(lista,3))
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
    cabecero=["Año","Cod Actividad Economico","Nombre Act Economico","Codigo Sector Economico","Nombre sector economico","Cod subsector economico","Nom subsector economico","Total ingresos netos","Total costos y gastos","Total saldo a pagar","Total saldo a favor"]
    print(tabulate(list_aux_,headers=cabecero,tablefmt="grid",maxcolwidths=[3,5,10,3,3,3,3,3,3,3,3]))

def requerimiento1(lista): 
   
    list_aux=[]
    list_aux_=[]
    size=lt.size(lista)
    if size<6:
        for i in lt.iterator(lista):
            list_aux.append(i)
    else:
        list_aux.append(lt.getElement(lista,1))
        list_aux.append(lt.getElement(lista,2))
        list_aux.append(lt.getElement(lista,3))
        list_aux.append(lt.getElement(lista,4))
        list_aux.append(lt.getElement(lista,5))
        list_aux.append(lt.getElement(lista,6))
        list_aux.append(lt.getElement(lista,7))
        list_aux.append(lt.getElement(lista,8))
        list_aux.append(lt.getElement(lista,9))
        list_aux.append(lt.getElement(lista,10))
    for info in list_aux:
        list_aux2=["","","","","","","","","",""]
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
        
        



        list_aux_.append(list_aux2)
    cabecero=["Año","Codigo Actividad Economico","Nombre Actividad Economico","Codigo Sector Economico","Nombre sector economico","Codigo subsector economico","Total ingresos netos","Total costos y gastos", "Total saldo a pagar", "Total saldo a favor"]
    print(tabulate(list_aux_,headers=cabecero,tablefmt="grid",maxcolwidths=[5,10,20,10,20,10,20,10,10,10,10]))

def requerimiento2(lista): 
   
    list_aux=[]
    list_aux_=[]
    size=lt.size(lista)
    if size<6:
        for i in lt.iterator(lista):
            list_aux.append(i)
    else:
        list_aux.append(lt.getElement(lista,1))
        list_aux.append(lt.getElement(lista,2))
        list_aux.append(lt.getElement(lista,3))
        list_aux.append(lt.getElement(lista,4))
        list_aux.append(lt.getElement(lista,5))
        list_aux.append(lt.getElement(lista,6))
        list_aux.append(lt.getElement(lista,7))
        list_aux.append(lt.getElement(lista,8))
        list_aux.append(lt.getElement(lista,9))
        list_aux.append(lt.getElement(lista,10))
    for info in list_aux:
        list_aux2=["","","","","","","","","",""]
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
        
        
        list_aux_.append(list_aux2)
    cabecero=["Año","Codigo Actividad Economico","Nombre Actividad Economico","Codigo Sector Economico","Nombre sector economico","Codigo subsector economico","Total ingresos netos","Total costos y gastos", "Total saldo a pagar", "Total saldo a favor"]
    print(tabulate(list_aux_,headers=cabecero,tablefmt="grid",maxcolwidths=[5,10,10,10,10,10,10,10,5,5,5]))        

def requerimiento3(lista): 
   
    list_aux=[]
    list_aux_=[]
    size=lt.size(lista)
    if size<6:
        for i in lt.iterator(lista):
            list_aux.append(i)
    else:
        list_aux.append(lt.getElement(lista,1))
        list_aux.append(lt.getElement(lista,2))
        list_aux.append(lt.getElement(lista,3))
        list_aux.append(lt.getElement(lista,4))
        list_aux.append(lt.getElement(lista,5))
        list_aux.append(lt.getElement(lista,6))
        list_aux.append(lt.getElement(lista,7))
        list_aux.append(lt.getElement(lista,8))
        list_aux.append(lt.getElement(lista,9))
        list_aux.append(lt.getElement(lista,10))
    for info in list_aux:
        list_aux2=["","","","","","","","","",""]
        list_aux2[0]=lt.getElement(info,1)
        list_aux2[1]=lt.getElement(info,4)
        list_aux2[2]=lt.getElement(info,5)
        list_aux2[3]=lt.getElement(info,6)
        list_aux2[4]=lt.getElement(info,7)
        list_aux2[5]=lt.getElement(info,12)
        list_aux2[6]=lt.getElement(info,8)
        list_aux2[7]=lt.getElement(info,9)
        list_aux2[8]=lt.getElement(info,10)
        list_aux2[9]=lt.getElement(info,11)
        
        



        list_aux_.append(list_aux2)
    cabecero=["Año","Cod Sec Economico","Nom Sect Economico","Cod Subsect","Nom subsect","Total de retencion","Total ingresos netos","Total costos y gastos del subsector economico", "Total saldo a pagar del subsect economico", "Total saldo a favor del subsect economico"]
    print(tabulate(list_aux_,headers=cabecero,tablefmt="grid",maxcolwidths=[3,5,10,3,10,3,3,3,3,3]))   
    
    
    
    
    
    
    
    
    
    
def requerimiento5(lista): 
   
    list_aux=[]
    list_aux_=[]
    size=lt.size(lista)
    if size<6:
        for i in lt.iterator(lista):
            list_aux.append(i)
    else:
        list_aux.append(lt.getElement(lista,1))
        list_aux.append(lt.getElement(lista,2))
        list_aux.append(lt.getElement(lista,3))
        list_aux.append(lt.getElement(lista,4))
        list_aux.append(lt.getElement(lista,5))
        list_aux.append(lt.getElement(lista,6))
        list_aux.append(lt.getElement(lista,7))
        list_aux.append(lt.getElement(lista,8))
        list_aux.append(lt.getElement(lista,9))
        list_aux.append(lt.getElement(lista,10))
    for info in list_aux:
        list_aux2=["","","","","","","","","",""]
        list_aux2[0]=lt.getElement(info,1)
        list_aux2[1]=lt.getElement(info,4)
        list_aux2[2]=lt.getElement(info,5)
        list_aux2[3]=lt.getElement(info,6)
        list_aux2[4]=lt.getElement(info,7)
        list_aux2[5]=lt.getElement(info,13)
        list_aux2[6]=lt.getElement(info,8)
        list_aux2[7]=lt.getElement(info,9)
        list_aux2[8]=lt.getElement(info,10)
        list_aux2[9]=lt.getElement(info,11)
        
 
        list_aux_.append(list_aux2)
    cabecero=["Año","Cod Sec Economico","Nom Sect Economico","Cod Subsect","Nom subsect","Total de descuentos tributarios","Total ingresos netos","Total costos y gastos del subsector economico", "Total saldo a pagar del subsect economico", "Total saldo a favor del subsect economico"]
    print(tabulate(list_aux_,headers=cabecero,tablefmt="grid",maxcolwidths=[3,5,10,3,10,3,3,3,3,3]))      
    
    
    
    

def requerimiento4(lista): 
   
    list_aux=[]
    list_aux_=[]
    size=lt.size(lista)
    if size<6:
        for i in lt.iterator(lista):
            list_aux.append(i)
    else:
        list_aux.append(lt.getElement(lista,1))
        list_aux.append(lt.getElement(lista,2))
        list_aux.append(lt.getElement(lista,3))
        list_aux.append(lt.getElement(lista,4))
        list_aux.append(lt.getElement(lista,5))
        list_aux.append(lt.getElement(lista,6))
        list_aux.append(lt.getElement(lista,7))
        list_aux.append(lt.getElement(lista,8))
        list_aux.append(lt.getElement(lista,9))
        list_aux.append(lt.getElement(lista,10))
    for info in list_aux:
        list_aux2=["","","","","","","","","",""]
        list_aux2[0]=lt.getElement(info,1)
        list_aux2[1]=lt.getElement(info,4)
        list_aux2[2]=lt.getElement(info,5)
        list_aux2[3]=lt.getElement(info,6)
        list_aux2[4]=lt.getElement(info,7)
        list_aux2[5]=lt.getElement(info,12)
        list_aux2[6]=lt.getElement(info,8)
        list_aux2[7]=lt.getElement(info,9)
        list_aux2[8]=lt.getElement(info,10)
        list_aux2[9]=lt.getElement(info,11)
        
        



        list_aux_.append(list_aux2)
    cabecero=["Año","Cod Sec Economico","Nom Sect Economico","Cod Subsect","Nom subsect","Total de retencion","Total ingresos netos","Total costos y gastos del subsector economico", "Total saldo a pagar del subsect economico", "Total saldo a favor del subsect economico"]
    print(tabulate(list_aux_,headers=cabecero,tablefmt="grid",maxcolwidths=[3,5,10,3,10,3,3,3,3,3]))

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar la actividad económica con mayor total saldo a pagar para todos los años disponibles")
    print("3- Listar la actividad económica con mayor total saldo a favor para todos los años disponibles")
    print("4- Encontrar el subsector económico con el menor total de retenciones para todos los años disponibles")
    print("5- Encontrar el subsector económico con los mayores costos y gastos de nómina para todos los años disponibles ")
    print("6- Encontrar el subsector económico con los mayores descuentos tributarios para todos los años disponibles")
    print("7- Encontrar la actividad económica con el mayor total de ingresos netos para cada sector económico en un año específico")
    print("8- Listar el TOP (N) de las actividades económicas con el menor total de costos y gastos para un periodo de tiempo ")
    print("9- Listar el TOP (N) de actividades económicas de cada subsector con los mayores totales de impuestos a cargo para un periodo de tiempo. ")

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
        cargadatos((catalog["data"]))
          
 

             
        

    elif int(inputs[0]) == 2:
        inicio=controller.getTime()
        answer=controller.req_1(catalog)
        requerimiento1(answer)
        fin=controller.getTime()
        print("Ha tardado {0}".format(controller.deltaTime(inicio,fin)))
        
    elif int(inputs[0])==3:
        inicio=controller.getTime()
        answer=controller.req_2(catalog)
        requerimiento2(answer)
        fin=controller.getTime()
        print("Ha tardado {0}".format(controller.deltaTime(inicio,fin)))
    elif int(inputs[0])==4:
        inicio=controller.getTime()
        answer=controller.req_3(catalog)
        requerimiento3(answer)
        fin=controller.getTime()
        print("Ha tardado {0}".format(controller.deltaTime(inicio,fin)))
    elif int(inputs[0])==5:
        inicio=controller.getTime()
        answer=controller.req_4(catalog)
        requerimiento4(answer)
        fin=controller.getTime()
        print("Ha tardado {0}".format(controller.deltaTime(inicio,fin)))        

    elif int(inputs[0])==6:
        inicio=controller.getTime()
        answer=controller.req_5(catalog)
        requerimiento3(answer)
        fin=controller.getTime()
        print("Ha tardado {0}".format(controller.deltaTime(inicio,fin)))

    elif int(inputs[0])==7:
        inicio=controller.getTime()
        answer=controller.req_7(catalog)
        requerimiento5(answer)
        fin=controller.getTime()
        print("Ha tardado {0}".format(controller.deltaTime(inicio,fin)))    
    else:
        sys.exit(0)
sys.exit(0)

