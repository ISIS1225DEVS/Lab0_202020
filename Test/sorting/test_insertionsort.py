"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
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
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import pytest
import config
from Sorting import insertionsort as sort
from DataStructures import listiterator as it
from ADT import list as slt

# list_type = 'ARRAY_LIST'
list_type = 'SINGLE_LINKED'

book1 = {'book_id': '1', 'book_title': 'Title 1', 'author': 'author 1'}
book2 = {'book_id': '2', 'book_title': 'Title 2', 'author': 'author 2'}
book3 = {'book_id': '3', 'book_title': 'Title 3', 'author': 'author 3'}
book4 = {'book_id': '4', 'book_title': 'Title 4', 'author': 'author 4'}
book5 = {'book_id': '5', 'book_title': 'Title 5', 'author': 'author 5'}
book6 = {'book_id': '6', 'book_title': 'Title 6', 'author': 'author 6'}
book7 = {'book_id': '7', 'book_title': 'Title 7', 'author': 'author 7'}
book8 = {'book_id': '8', 'book_title': 'Title 8', 'author': 'author 8'}
book9 = {'book_id': '9', 'book_title': 'Title 9', 'author': 'author 9'}
book10 = {'book_id': '10', 'book_title': 'Title 10', 'author': 'author 10'}
book11 = {'book_id': '7', 'book_title': 'Title 11', 'author': 'author 11'}
book12 = {'book_id': '8', 'book_title': 'Title 12', 'author': 'author 12'}
book13 = {'book_id': '9', 'book_title': 'Title 13', 'author': 'author 13'}
book14 = {'book_id': '10', 'book_title': 'Title 14', 'author': 'author 14'}

lista_ordenada_correcta = [
    book1, book2, book3, book4, book5, book6, book7, book8, book9, book10
]


def less(element1, element2):
    if int(element1['book_id']) < int(element2['book_id']):
        return True
    return False


def probarOrden(lst):
    """
    Revisa que la lista que se pasa por parametro esté en el orden correcto en el cual los libros deberian estar
    """
    iterator = it.newIterator(lst)
    indice = 0
    while it.hasNext(iterator):
        element = it.next(iterator)
        assert element == lista_ordenada_correcta[indice]
        indice += 1
        result = "".join(str(key) + ": " + str(value) +
                         ",  " for key, value in element.items())
        print(result)


def test_randomElements():
    """
    Lista con elementos en orden aleatorio, prueba que se ordene correctamente cuando no hay orden alguno
    """
    lst = slt.newList(list_type)
    slt.addFirst(lst, book5)
    slt.addFirst(lst, book6)
    slt.addFirst(lst, book3)
    slt.addFirst(lst, book10)
    slt.addFirst(lst, book1)
    slt.addFirst(lst, book2)
    slt.addFirst(lst, book8)
    slt.addFirst(lst, book4)
    slt.addFirst(lst, book7)
    slt.addFirst(lst, book9)

    print("Random list:----------------------------------------------------")
    iterator = it.newIterator(lst)
    while it.hasNext(iterator):
        element = it.next(iterator)
        result = "".join(str(key) + ": " + str(value) +
                         ",  " for key, value in element.items())
        print(result)
    print("sorting ....")
    sort.insertionSort(lst, less)
    probarOrden(lst)


def test_invertedElements():
    """
    Lista ordenada inversamente, sale correcta si el orden final es el inverso a la forma en la cual se
    agregan
    """
    lst = slt.newList(list_type)
    slt.addFirst(lst, book1)
    slt.addFirst(lst, book2)
    slt.addFirst(lst, book3)
    slt.addFirst(lst, book4)
    slt.addFirst(lst, book5)
    slt.addFirst(lst, book6)
    slt.addFirst(lst, book7)
    slt.addFirst(lst, book8)
    slt.addFirst(lst, book9)
    slt.addFirst(lst, book10)

    print("Inverted list:----------------------------------------------------")
    iterator = it.newIterator(lst)
    while it.hasNext(iterator):
        element = it.next(iterator)
        result = "".join(str(key) + ": " + str(value) +
                         ",  " for key, value in element.items())
        print(result)
    print("sorting ....")
    sort.insertionSort(lst, less)
    iterator = it.newIterator(lst)
    probarOrden(lst)


def test_orderedElementss():
    """
    Lista ordenada normalmente, deberia ser igual a como se ingresan los libros
    """
    lst = slt.newList(list_type)
    slt.addFirst(lst, book10)
    slt.addFirst(lst, book9)
    slt.addFirst(lst, book8)
    slt.addFirst(lst, book7)
    slt.addFirst(lst, book6)
    slt.addFirst(lst, book5)
    slt.addFirst(lst, book4)
    slt.addFirst(lst, book3)
    slt.addFirst(lst, book2)
    slt.addFirst(lst, book1)

    print("Inverted list:----------------------------------------------------")
    iterator = it.newIterator(lst)
    while it.hasNext(iterator):
        element = it.next(iterator)
        result = "".join(str(key) + ": " + str(value) +
                         ",  " for key, value in element.items())
        print(result)
    print("sorting ....")
    sort.insertionSort(lst, less)
    probarOrden(lst)


def test_oneElement():
    """
    Se prueba el ordenamiento de un elemento, solo deberia haber un elemento en la lista
    """
    lst = slt.newList(list_type)
    slt.addFirst(lst, book1)

    print("one element:----------------------------------------------------")
    iterator = it.newIterator(lst)
    while it.hasNext(iterator):
        element = it.next(iterator)
        result = "".join(str(key) + ": " + str(value) +
                         ",  " for key, value in element.items())
        print(result)
    print("sorting ....")
    sort.insertionSort(lst, less)
    iterator = it.newIterator(lst)
    while it.hasNext(iterator):
        element = it.next(iterator)
        assert element == book1


def test_ManyElements():
    """
    Con muchos elementos en la lista, en donde identificadores se repiten
    Deben aparecer consecutivos aquellos con id igual
    """
    lst = slt.newList(list_type)
    slt.addFirst(lst, book5)
    slt.addFirst(lst, book6)
    slt.addFirst(lst, book14)
    slt.addFirst(lst, book3)
    slt.addFirst(lst, book13)
    slt.addFirst(lst, book10)
    slt.addFirst(lst, book1)
    slt.addFirst(lst, book12)
    slt.addFirst(lst, book2)
    slt.addFirst(lst, book8)
    slt.addFirst(lst, book4)
    slt.addFirst(lst, book11)
    slt.addFirst(lst, book7)
    slt.addFirst(lst, book9)

    print("Repeated elements:----------------------------------------------------")
    iterator = it.newIterator(lst)
    while it.hasNext(iterator):
        element = it.next(iterator)
        result = "".join(str(key) + ": " + str(value) +
                         ",  " for key, value in element.items())
        print(result)
    print("sorting ....")
    sort.insertionSort(lst, less)
    assert slt.removeFirst(lst) == book1
    assert slt.removeFirst(lst) == book2
    assert slt.removeFirst(lst) == book3
    assert slt.removeFirst(lst) == book4
    assert slt.removeFirst(lst) == book5
    assert slt.removeFirst(lst) == book6
    assert slt.removeFirst(lst) == book7
    assert slt.removeFirst(lst) == book11
    assert slt.removeFirst(lst) == book8
    assert slt.removeFirst(lst) == book12
    assert slt.removeFirst(lst) == book9
    assert slt.removeFirst(lst) == book13
    assert slt.removeFirst(lst) == book10
    assert slt.removeFirst(lst) == book14


def test_agregarYquitar():
    """
    Prueba que al hacer varios ordnamientos el orden debe mantenerse asi se cambien los elementos
    Se requiere tener la lista ordenada, luego desordenada y probar que genera excepcion
    """
    lst = slt.newList(list_type)
    slt.addFirst(lst, book10)
    slt.addFirst(lst, book9)
    slt.addFirst(lst, book8)
    slt.addFirst(lst, book7)
    slt.addFirst(lst, book6)
    slt.addFirst(lst, book5)
    slt.addFirst(lst, book4)
    slt.addFirst(lst, book3)
    slt.addFirst(lst, book2)
    slt.addFirst(lst, book1)
    probarOrden(lst)  # Prueba que al inicio la lista esté en orden
    slt.addFirst(lst, slt.removeLast(lst))
    slt.addLast(lst, slt.removeFirst(lst))
    slt.addFirst(lst, slt.removeLast(lst))
    with pytest.raises(Exception):
        probarOrden(lst)
    sort.insertionSort(lst, less)
    probarOrden(lst)
