# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 14:54:33 2025

@author: DEYVYS MARIA VALDES
"""

class Nodo:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class Lista_enlazada:
    def __init__(self):
        self.head = None
        
    # 1. initialize() - Inicializar una lista enlazada vacía
    def initialize(self):
        self.head = None
        return self
    
    # 2. is_empty() - Verificar si la lista está vacía
    def is_empty(self):
        return self.head == None
    
    # 3. length() - Obtener el número de elementos en la lista
    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    
    # 4. clear() - Eliminar todos los elementos de la lista
    def clear(self):
        self.head = None
        return self
    
    # 5. add_first() - Insertar un elemento al inicio (mismo que agregar_al_inicio)
    def add_first(self, data):
        self.head = Nodo(data=data, next=self.head)
        return self
        
    # Método ya implementado en el código original
    def agregar_al_inicio(self, data):
        self.head = Nodo(data=data, next=self.head)
    
    # 6. add_last() - Insertar un elemento al final (mismo que agregar_al_final)
    def add_last(self, data):
        if not self.head:
            self.head = Nodo(data=data)
            return self
            
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Nodo(data=data)
        return self
        
    # Método ya implementado en el código original
    def agregar_al_final(self, data):
        if not self.head:
            self.head = Nodo(data=data)
            return
            
        temporal = self.head
        while temporal.next:
            temporal = temporal.next
        temporal.next = Nodo(data=data)
    
    # 7. insert_at() - Insertar en una posición específica
    def insert_at(self, index, data):
        if index < 0:
            raise IndexError("Índice negativo no permitido")
            
        if index == 0:
            return self.add_first(data)
            
        current = self.head
        position = 0
        
        while current and position < index - 1:
            current = current.next
            position += 1
            
        if current is None:
            raise IndexError("Índice fuera de rango")
            
        new_node = Nodo(data=data, next=current.next)
        current.next = new_node
        return self
    
    # 8. insert_after() - Insertar después de un nodo específico
    def insert_after(self, target_node, data):
        if target_node is None:
            raise ValueError("El nodo no puede ser None")
            
        new_node = Nodo(data=data, next=target_node.next)
        target_node.next = new_node
        return self
    
    # 9. insert_before() - Insertar antes de un nodo específico
    def insert_before(self, target_node, data):
        if target_node is None:
            raise ValueError("El nodo no puede ser None")
            
        if self.head is None:
            raise ValueError("La lista está vacía")
            
        if self.head == target_node:
            return self.add_first(data)
            
        current = self.head
        while current and current.next != target_node:
            current = current.next
            
        if current is None:
            raise ValueError("El nodo objetivo no está en la lista")
            
        new_node = Nodo(data=data, next=target_node)
        current.next = new_node
        return self
    
    # 10. insert_sorted() - Insertar en orden (lista ordenada)
    def insert_sorted(self, data):
        if self.is_empty() or data <= self.head.data:
            return self.add_first(data)
            
        current = self.head
        while current.next and current.next.data < data:
            current = current.next
            
        new_node = Nodo(data=data, next=current.next)
        current.next = new_node
        return self
    
    # 11. remove_first() - Eliminar el primer elemento
    def remove_first(self):
        if self.is_empty():
            raise ValueError("No se puede eliminar de una lista vacía")
            
        removed_data = self.head.data
        self.head = self.head.next
        return removed_data
    
    # 12. remove_last() - Eliminar el último elemento
    def remove_last(self):
        if self.is_empty():
            raise ValueError("No se puede eliminar de una lista vacía")
            
        if self.head.next is None:
            removed_data = self.head.data
            self.head = None
            return removed_data
            
        current = self.head
        while current.next.next:
            current = current.next
            
        removed_data = current.next.data
        current.next = None
        return removed_data
    
    # 13. remove_at() - Eliminar en una posición específica
    def remove_at(self, index):
        if self.is_empty():
            raise ValueError("No se puede eliminar de una lista vacía")
            
        if index < 0:
            raise IndexError("Índice negativo no permitido")
            
        if index == 0:
            return self.remove_first()
            
        current = self.head
        position = 0
        
        while current.next and position < index - 1:
            current = current.next
            position += 1
            
        if current.next is None:
            raise IndexError("Índice fuera de rango")
            
        removed_data = current.next.data
        current.next = current.next.next
        return removed_data
    
    # 14. remove_node() - Eliminar un nodo específico
    def remove_node(self, node):
        if self.is_empty() or node is None:
            raise ValueError("La lista está vacía o el nodo es None")
            
        if self.head == node:
            removed_data = self.head.data
            self.head = self.head.next
            return removed_data
            
        current = self.head
        while current.next and current.next != node:
            current = current.next
            
        if current.next is None:
            raise ValueError("El nodo no está en la lista")
            
        removed_data = current.next.data
        current.next = current.next.next
        return removed_data
    
    # 15. remove_by_value() - Eliminar por valor (similar a delete_node ya implementado)
    def remove_by_value(self, data):
        if self.is_empty():
            raise ValueError("No se puede eliminar de una lista vacía")
            
        if self.head.data == data:
            self.head = self.head.next
            return data
            
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
            
        if current.next is None:
            raise ValueError(f"El valor {data} no está en la lista")
            
        current.next = current.next.next
        return data
    
    # Método ya implementado en el código original
    def delete_node(self, key):
        actual = self.head
        previo = None
        
        while actual and actual.data != key:
            previo = actual
            actual = actual.next
        
        if previo is None:
            self.head = actual.next
        elif actual:
            previo.next = actual.next
            actual.next = None
    
    # 16. remove_duplicates() - Eliminar elementos duplicados
    def remove_duplicates(self):
        if self.is_empty() or self.head.next is None:
            return self  # Lista vacía o con un solo elemento
            
        values = set([self.head.data])
        current = self.head
        
        while current.next:
            if current.next.data in values:
                # Duplicado encontrado, eliminarlo
                current.next = current.next.next
            else:
                # Nuevo valor, agregarlo al conjunto
                values.add(current.next.data)
                current = current.next
                
        return self
    
    # 17. search() - Buscar un elemento y retornar el nodo
    def search(self, data):
        current = self.head
        
        while current:
            if current.data == data:
                return current
            current = current.next
            
        return None  # No encontrado
    
    # 18. contains() - Verificar si un elemento existe
    def contains(self, data):
        return self.search(data) is not None
    
    # 19. index_of() - Obtener la posición de un elemento
    def index_of(self, data):
        current = self.head
        index = 0
        
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
            
        return -1  # No encontrado
    
    # 20. find_min() - Encontrar el valor mínimo
    def find_min(self):
        if self.is_empty():
            raise ValueError("La lista está vacía")
            
        min_value = self.head.data
        current = self.head.next
        
        while current:
            if current.data < min_value:
                min_value = current.data
            current = current.next
            
        return min_value
    
    # 21. find_max() - Encontrar el valor máximo
    def find_max(self):
        if self.is_empty():
            raise ValueError("La lista está vacía")
            
        max_value = self.head.data
        current = self.head.next
        
        while current:
            if current.data > max_value:
                max_value = current.data
            current = current.next
            
        return max_value
    
    # 22. find_middle() - Encontrar el nodo del medio
    def find_middle(self):
        if self.is_empty():
            return None
            
        slow = self.head
        fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow
    
    # 23. get_first() - Obtener el primer elemento
    def get_first(self):
        if self.is_empty():
            raise ValueError("La lista está vacía")
            
        return self.head.data
    
    # 24. get_last() - Obtener el último elemento (similar a get_last_node ya implementado)
    def get_last(self):
        if self.is_empty():
            raise ValueError("La lista está vacía")
            
        current = self.head
        while current.next:
            current = current.next
            
        return current.data
    
    # Método ya implementado en el código original
    def get_last_node(self):
        temp = self.head
        while(temp.next is not None):
            temp = temp.next
        return temp.data
    
    # 25. get_at() - Obtener elemento en una posición específica
    def get_at(self, index):
        if self.is_empty():
            raise ValueError("La lista está vacía")
            
        if index < 0:
            raise IndexError("Índice negativo no permitido")
            
        current = self.head
        position = 0
        
        while current and position < index:
            current = current.next
            position += 1
            
        if current is None:
            raise IndexError("Índice fuera de rango")
            
        return current.data
    
    # 26. get_node_at() - Obtener el nodo en una posición específica
    def get_node_at(self, index):
        if self.is_empty():
            raise ValueError("La lista está vacía")
            
        if index < 0:
            raise IndexError("Índice negativo no permitido")
            
        current = self.head
        position = 0
        
        while current and position < index:
            current = current.next
            position += 1
            
        if current is None:
            raise IndexError("Índice fuera de rango")
            
        return current
    
    # 27. peek_first() - Ver el primer elemento sin eliminarlo
    def peek_first(self):
        return self.get_first()
    
    # 28. peek_last() - Ver el último elemento sin eliminarlo
    def peek_last(self):
        return self.get_last()
    
    # 29. get_iterator() - Obtener un iterador para la lista
    def get_iterator(self):
        return LinkedListIterator(self)
    
    # 30. for_each() - Aplicar una función a cada elemento
    def for_each(self, func):
        current = self.head
        
        while current:
            func(current.data)
            current = current.next
            
        return self
    
    # 31. traverse() - Recorrer la lista e imprimir elementos (similar a print_list ya implementado)
    def traverse(self):
        if self.is_empty():
            print("Lista vacía")
            return
            
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
            
        print("None")
    
    # Método ya implementado en el código original
    def print_list(self):
        node = self.head
        while node != None:
            print(node.data, end =" --> ")
            node = node.next
    
    # 32. traverse_n_times() - Recorrer la lista n veces
    def traverse_n_times(self, n):
        if self.is_empty() or n <= 0:
            return
            
        for _ in range(n):
            current = self.head
            while current:
                print(current.data, end=" -> ")
                current = current.next
            print("None")
    
    # 33. iterate_from() - Iterar desde un nodo específico
    def iterate_from(self, start_node, steps):
        if self.is_empty() or start_node is None:
            return None
            
        current = start_node
        
        for _ in range(steps):
            if current is None:
                return None
            current = current.next
            
        return current
    
    # 34. map() - Aplicar una función y devolver nueva lista
    def map(self, func):
        result = Lista_enlazada()
        current = self.head
        
        while current:
            result.add_last(func(current.data))
            current = current.next
            
        return result
    
    # 35. filter() - Filtrar elementos según una condición
    def filter(self, predicate):
        result = Lista_enlazada()
        current = self.head
        
        while current:
            if predicate(current.data):
                result.add_last(current.data)
            current = current.next
            
        return result
    
    # 36. reduce() - Reducir la lista a un solo valor
    def reduce(self, func, initial):
        if self.is_empty():
            return initial
            
        result = initial
        current = self.head
        
        while current:
            result = func(result, current.data)
            current = current.next
            
        return result
    
    # 37. sort() - Ordenar la lista (utilizando bubble sort como ejemplo)
    def sort(self):
        if self.is_empty() or self.head.next is None:
            return self  # Lista vacía o con un solo elemento
            
        swapped = True
        
        while swapped:
            swapped = False
            current = self.head
            
            while current.next:
                if current.data > current.next.data:
                    # Intercambiar datos
                    current.data, current.next.data = current.next.data, current.data
                    swapped = True
                current = current.next
                
        return self
    
    # 38. reverse() - Invertir el orden de los elementos
    def reverse(self):
        if self.is_empty() or self.head.next is None:
            return self  # Lista vacía o con un solo elemento
            
        prev = None
        current = self.head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            
        self.head = prev
        return self
    
    # 39. shuffle() - Mezclar aleatoriamente los elementos
    def shuffle(self):
        import random
        
        if self.is_empty() or self.head.next is None:
            return self  # Lista vacía o con un solo elemento
            
        # Convertir a lista
        elements = []
        current = self.head
        
        while current:
            elements.append(current.data)
            current = current.next
            
        # Mezclar
        random.shuffle(elements)
        
        # Reconstruir la lista
        self.clear()
        for element in elements:
            self.add_last(element)
            
        return self
    
    # 40. merge() - Combinar con otra lista
    def merge(self, other_list):
        if other_list.is_empty():
            return self
            
        if self.is_empty():
            self.head = other_list.head
            return self
            
        # Obtener el último nodo de esta lista
        current = self.head
        while current.next:
            current = current.next
            
        # Conectar con la otra lista
        current.next = other_list.head
        return self
    
    # 41. concat() - Concatenar con otra lista (copia los elementos)
    def concat(self, other_list):
        result = Lista_enlazada()
        
        # Copiar esta lista
        current = self.head
        while current:
            result.add_last(current.data)
            current = current.next
            
        # Copiar la otra lista
        current = other_list.head
        while current:
            result.add_last(current.data)
            current = current.next
            
        return result
    
    # 42. intersect() - Elementos comunes con otra lista
    def intersect(self, other_list):
        result = Lista_enlazada()
        
        if self.is_empty() or other_list.is_empty():
            return result
            
        # Conjunto para almacenar elementos de la otra lista
        other_elements = set()
        current = other_list.head
        
        while current:
            other_elements.add(current.data)
            current = current.next
            
        # Verificar elementos comunes
        current = self.head
        seen = set()  # Para evitar duplicados en la lista resultante
        
        while current:
            if current.data in other_elements and current.data not in seen:
                result.add_last(current.data)
                seen.add(current.data)
            current = current.next
            
        return result
    
    # 43. difference() - Elementos que están en una pero no en otra
    def difference(self, other_list):
        result = Lista_enlazada()
        
        if self.is_empty():
            return result
            
        if other_list.is_empty():
            # Crear una copia de esta lista
            current = self.head
            while current:
                result.add_last(current.data)
                current = current.next
            return result
            
        # Conjunto para almacenar elementos de la otra lista
        other_elements = set()
        current = other_list.head
        
        while current:
            other_elements.add(current.data)
            current = current.next
            
        # Agregar elementos que no están en la otra lista
        current = self.head
        seen = set()  # Para evitar duplicados en la lista resultante
        
        while current:
            if current.data not in other_elements and current.data not in seen:
                result.add_last(current.data)
                seen.add(current.data)
            current = current.next
            
        return result
    
    # 44. is_subset() - Verificar si una lista es subconjunto de otra
    def is_subset(self, other_list):
        if other_list.is_empty():
            return True  # Una lista vacía es subconjunto de cualquier lista
            
        if self.is_empty():
            return False  # Esta lista vacía no contiene elementos de la otra
            
        # Conjunto para almacenar los elementos de esta lista
        elements = set()
        current = self.head
        
        while current:
            elements.add(current.data)
            current = current.next
            
        # Verificar si todos los elementos de la otra lista están en esta lista
        current = other_list.head
        
        while current:
            if current.data not in elements:
                return False
            current = current.next
            
        return True
    
    # 45. split_at() - Dividir la lista en dos en una posición
    def split_at(self, index):
        if self.is_empty():
            return Lista_enlazada(), Lista_enlazada()
            
        if index <= 0:
            return Lista_enlazada(), self.concat(Lista_enlazada())
            
        # Primera parte
        first_part = Lista_enlazada()
        current = self.head
        position = 0
        
        while current and position < index:
            first_part.add_last(current.data)
            current = current.next
            position += 1
            
        # Segunda parte
        second_part = Lista_enlazada()
        
        while current:
            second_part.add_last(current.data)
            current = current.next
            
        return first_part, second_part
    
    # 46. count_if() - Contar elementos que cumplen una condición
    def count_if(self, predicate):
        count = 0
        current = self.head
        
        while current:
            if predicate(current.data):
                count += 1
            current = current.next
            
        return count
    
    # 47. transform_in_place() - Transformar elementos en el lugar
    def transform_in_place(self, func):
        current = self.head
        
        while current:
            current.data = func(current.data)
            current = current.next
            
        return self
    
    # 48. rotate_right() - Mover el último elemento al principio
    def rotate_right(self):
        if self.is_empty() or self.head.next is None:
            return self  # Lista vacía o con un solo elemento
            
        # Encontrar el penúltimo y último nodo
        current = self.head
        while current.next.next:
            current = current.next
            
        # Mover el último nodo al principio
        last_node = current.next
        current.next = None
        last_node.next = self.head
        self.head = last_node
        
        return self
    
    # 49. rotate_left() - Mover el primer elemento al final
    def rotate_left(self):
        if self.is_empty() or self.head.next is None:
            return self  # Lista vacía o con un solo elemento
            
        # Guardar el primer nodo
        first_node = self.head
        self.head = first_node.next
        
        # Encontrar el último nodo
        current = self.head
        while current.next:
            current = current.next
            
        # Mover el primer nodo al final
        current.next = first_node
        first_node.next = None
        
        return self
    
    # 50. is_sorted() - Verificar si la lista está ordenada
    def is_sorted(self):
        if self.is_empty() or self.head.next is None:
            return True  # Lista vacía o con un solo elemento está ordenada
            
        current = self.head
        
        while current.next:
            if current.data > current.next.data:
                return False
            current = current.next
            
        return True
    
    # 51. is_palindrome() - Verificar si la lista es un palíndromo
    def is_palindrome(self):
        if self.is_empty() or self.head.next is None:
            return True  # Lista vacía o con un solo elemento es palíndromo
            
        # Convertir la lista a una lista normal para comparar
        values = []
        current = self.head
        
        while current:
            values.append(current.data)
            current = current.next
            
        # Verificar si es palíndromo
        return values == values[::-1]
    
    # 52. swap_pairs() - Intercambiar elementos adyacentes
    def swap_pairs(self):
        if self.is_empty() or self.head.next is None:
            return self  # Lista vacía o con un solo elemento
            
        dummy = Nodo(None, self.head)
        prev = dummy
        current = self.head
        
        while current and current.next:
            # Nodos a intercambiar
            first = current
            second = current.next
            
            # Intercambiar
            prev.next = second
            first.next = second.next
            second.next = first
            
            # Mover al siguiente par
            prev = first
            current = first.next
            
        self.head = dummy.next
        return self
    def Mover_Dato(self,nombre,move,where):
        if self.contains(nombre) is None:
            print("no existe")
            return
        posact =self.index_of(nombre)
        print(posact)
        
        if where =="adelante":
            self.remove_at(posact)
            posnew=(posact+move) %self.length()
            self.insert_at(posnew, nombre)
        if where =="atras":
            posnew=(posact-move)%self.length()
            print(posnew)
            self.remove_at(posact)
            self.insert_at(posnew, nombre)
    def metodo(self,dato):
        if type(dato) == str:
            print("el dato es un string")
            return
        if self.contains(dato) is True:
            print("ya el elemento esta contenido en la lista")
            
        if dato >0:
            self.add_last(dato)
        elif dato <0:
            self.add_first(dato)
        elif dato == 0:
            self.insert_sorted(dato)
        if type(dato) == str:
            print("el dato es un string")
        self.traverse()
            
            
            
            
            

# Iterador para lista enlazada
class LinkedListIterator:
    def __init__(self, linked_list):
        self.current = linked_list.head
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current is None:
            raise StopIteration
            
        data = self.current.data
        self.current = self.current.next
        return data

#parcial 1

pr =Lista_enlazada()
pr.metodo(1)
pr.metodo(2)
pr.metodo(-1)
pr.metodo(-2)
pr.metodo(0)
pr.metodo("alo")
 
#    # parcial2
# lista = Lista_enlazada()
# lista.add_first("jesus")
# lista.add_first("sebas")
# lista.add_first("juna")
# lista.add_first("camilo")
# lista.print_list()
# lista.Mover_Dato("sebas", 3, "atras")
# lista.print_list()






    
    