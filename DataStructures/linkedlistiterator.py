"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Desarrollado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
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

import DataStructures.listnode as node

"""
  Este módulo implementa un iterador para recorrer los elementos de una lista encadenada
"""


def newIterator(lst):
    """
    Inicializa un iterador para la lista lst
    Args:
        lst: La lista sobre la que se quiere iterar
    Returns:
        Un iterador para la lista
    """
    iterator = {'iterable_lst': lst, 'current_node': None, 'type': 'LINKED_ITERATOR'}
    return iterator


def hasNext(iterator):
    """
    Informa si se puede seguir iterando.
    Informa si existe un nodo en la siguiente posicion de la lista, a partir de la posicion actual del iterador.
    Args:
        iterator: El iterador creado sobre la lista
    Returns:
        True si existe un siguiente elemento, False de lo contrario
    """
    if iterator['iterable_lst']['first'] == None:
        return False
    elif (iterator['iterable_lst']['first'] != None) and (iterator['current_node']) == None:
        return True
    elif iterator['current_node']['next'] == None:
        return False
    elif iterator['current_node']['next'] != None:
        return True


def next(iterator):
    """
    Retorna el elemento en la posición siguiente a la indicada por el iterador
    Args:
        iterator: El iterador de la lista
    Returns:
        El siguiente elemento al último retornado por el iterador
    """
    if (iterator['iterable_lst']['first'] != None) and (iterator['current_node'] == None):
        iterator['current_node'] = iterator['iterable_lst']['first']
    elif iterator['current_node']['next'] != None:
        iterator['current_node'] = iterator['current_node']['next']

    return iterator['current_node']['info']
