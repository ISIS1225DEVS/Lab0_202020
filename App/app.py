"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Cristian Camilo Castellanos
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
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

"""
  Este módulo es una aplicación básica con un menú de opciones para
   cargar datos, contar elementos, y hacer búsquedas sobre una lista.
"""

import config as cf
import sys
import csv
from time import process_time


def loadCSVFile(file_d, file_c, lst_d, lst_c, sep=";"):
    """
    Carga un archivo csv a una lista
    Args:
        file_d
            Archivo de texto del cual se cargaran los detalles de las películas.
        file_c
            Archivo de texto del cual se cargaran los castings de las películas.
        lst_d :: []
            Lista a la cual quedaran cargados los detalles despues de la lectura del archivo.
        lst_c :: []
            Lista a la cual quedaran cargados los castings despues de la lectura del archivo.
        sep :: str
            Separadores código para diferenciar a los distintos elementos dentro del archivo.
    Try:
        Intenta cargar el archivo CSV a la lista que se le pasa por parametro, si encuentra algun error
        Borra la lista e informa al usuario
    Returns: None   
    """
    del lst_d[:]
    del lst_c[:]
    print("Cargando archivos...")
    t1_start = process_time()  # tiempo inicial
    dialect = csv.excel()
    dialect.delimiter = sep
    try:
        with open(file_d, encoding="utf-8-sig") as csvfile_d, open(file_c, encoding="utf-8-sig") as csvfile_c:
            spamreader_d = csv.DictReader(csvfile_d, dialect=dialect)
            spamreader_c = csv.DictReader(csvfile_c, dialect=dialect)
            for row in spamreader_d:
                lst_d.append(row)
            for row in spamreader_c:
                lst_c.append(row)
    except:
        del lst_d[:]
        del lst_c[:]
        print("Se presento un error en la carga de los archivos")
    t1_stop = process_time()  # tiempo final
    print("Tiempo de ejecución ", t1_stop - t1_start, " segundos")


def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Contar los elementos de la Lista")
    print("3- Contar elementos filtrados por palabra clave")
    print("4- Consultar elementos a partir de dos listas")
    print("0- Salir")


def countElementsFilteredByColumn(criteria, column, lst):
    """
    Retorna cuantos elementos coinciden con un criterio para una columna dada  
    Args:
        criteria:: str
            Critero sobre el cual se va a contar la cantidad de apariciones
        column
            Columna del arreglo sobre la cual se debe realizar el conteo
        lst
            Lista en la cual se realizará el conteo, debe estar inicializada
    Return:
        counter :: int
            la cantidad de veces ue aparece un elemento con el criterio definido
    """
    if len(lst) == 0:
        print("La lista esta vacía")
        return 0
    else:
        t1_start = process_time()  # tiempo inicial
        counter = 0  # Cantidad de repeticiones
        for element in lst:
            if criteria.lower() in element[column].lower():  # filtrar por palabra clave
                counter += 1
        t1_stop = process_time()  # tiempo final
        print("Tiempo de ejecución ", t1_stop - t1_start, " segundos")
    return counter


def countElementsByCriteria(criteria, column, lst):
    """
    Retorna la cantidad de elementos que cumplen con un criterio para una columna dada
    """
    return 0


def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """
    details_list = []  # instanciar una lista vacia
    casting_list = []  # instanciar una lista vacia
    while True:
        printMenu()  # imprimir el menu de opciones en consola
        inputs = input('Seleccione una opción para continuar\n')  # leer opción ingresada
        if len(inputs) > 0:
            if int(inputs[0]) == 1:  # opcion 1
                loadCSVFile("../Data/MoviesDetailsCleaned-small.csv", "../Data/MoviesCastingRaw-small.csv",
                            details_list, casting_list)  # llamar funcion cargar datos
                if len(details_list) == len(casting_list):
                    print("Datos cargados, " + str(len(details_list)) + " elementos cargados en listas")
                else:
                    print("Datos cargados, aunque inconsistentes")
            elif int(inputs[0]) == 2:  # opcion 2
                if len(details_list) == 0:  # obtener la longitud de la lista
                    print("La lista esta vacía")
                else:
                    print("La lista tiene " + str(len(details_list)) + " elementos")
            elif int(inputs[0]) == 3:  # opcion 3
                criteria = input('Ingrese el criterio de búsqueda\n')
                counter = countElementsFilteredByColumn(criteria, "nombre", lista)  # filtrar una columna por criterio
                print("Coinciden ", counter, " elementos con el crtierio: ", criteria)
            elif int(inputs[0]) == 4:  # opcion 4
                criteria = input('Ingrese el criterio de búsqueda\n')
                counter = countElementsByCriteria(criteria, 0, details_list)
                print("Coinciden", counter, "elementos con el crtierio: '", criteria, "' (en construcción ...)")
            elif int(inputs[0]) == 0:  # opcion 0, salir
                sys.exit(0)


if __name__ == "__main__":
    main()
