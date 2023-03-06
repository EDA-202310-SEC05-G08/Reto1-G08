"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def newCatalog():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    catalog = {
        "data": None,
        "actividad_economica":None,
        "sector_economico":None,
        "subsector_economico":None
    }

    catalog["data"] = lt.newList(datastructure="ARRAY_LIST",
                                     cmpfunction=sort)

    return catalog


def addcontenidoN(catalog,data):
    #Se separa cada linea del csv en una lista con la info
    info=dicc_array(data)
    lt.addLast(catalog["data"],info)


    return catalog

def dicc_array(info):
    array=lt.newList("ARRAY_LIST")
    lt.addFirst(array,int(info["Año"]))#1
    lt.addLast(array,info["Código actividad económica"])#2
    lt.addLast(array,info["Nombre actividad económica"])#3
    lt.addLast(array,info["Código sector económico"])#4
    lt.addLast(array,info["Nombre sector económico"])#5
    lt.addLast(array,info["Código subsector económico"])#6
    lt.addLast(array,info["Nombre subsector económico"])#7
    lt.addLast(array,info["Total ingresos netos"])#8
    lt.addLast(array,info["Total costos y gastos"])#9
    lt.addLast(array,int(info["Total saldo a pagar"]))#10
    lt.addLast(array,info["Total saldo a favor"])#11
    return array

# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    data = {'id': 0, "info": ""}
    data["id"] = id
    data["info"] = info

    return data


# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    pos_data = lt.isPresent(data_structs["data"], id)
    if pos_data > 0:
        data = lt.getElement(data_structs["data"], pos_data)
        return data
    return None


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    return lt.size(data_structs["data"])


def req_1(info):
    """
    Función que soluciona el requerimiento 1 O(N)
    """
    lista=lt.newList("ARRAY_LIST") #Por convencion, la posicion 1 sera 2012, 2 sera 2013 y asi sucesivamente
    anio_base=2011
    lt.addFirst(lista,0)
    lt.addLast(lista,0)
    lt.addLast(lista,0)
    lt.addLast(lista,0)
    lt.addLast(lista,0)
    lt.addLast(lista,0)
    lt.addLast(lista,0)
    lt.addLast(lista,0)
    lt.addLast(lista,0)
    lt.addLast(lista,0)
    # TODO: Realizar el requerimiento 1
    for i in lt.iterator(info):
        anio=lt.getElement(i,1)-anio_base  #Anio es la posicion para la lista
        saldo=lt.getElement(i,10)  
        if lt.getElement(lista,anio)==0 or saldo > lt.getElement(lt.getElement(lista,anio),10):
            lt.changeInfo(lista,anio,i)
    return lista

def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    if data_1["id"] > data_2["id"]:
        return 1
    elif data_1["id"] < data_2["id"]:
        return -1
    else:
        return 0

# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    return data_1["Año"] > data_2["Año"]


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    sa.sort(data_structs["data"], sort_criteria)
