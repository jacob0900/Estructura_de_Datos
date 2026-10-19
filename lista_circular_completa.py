import random
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
    
    # 1. initialize() - Inicializar una lista circular vacía
    def initialize(self):
        self.head = None
        return self
    
    # 2. is_empty() - Verificar si la lista está vacía
    def is_empty(self):
        return self.head is None
    
    # 3. length() - Obtener el número de elementos en la lista
    def length(self):
        if self.is_empty():
            return 0
        
        count = 1
        current = self.head
        while current.next != self.head:
            count += 1
            current = current.next
        
        return count
    
    # 4. clear() - Eliminar todos los elementos de la lista
    def clear(self):
        self.head = None
        return self
    
    # 5. add_first(data) - Insertar un elemento al inicio
    def add_first(self, data):
        new_node = Node(data)
        
        if self.is_empty():
            self.head = new_node
            new_node.next = new_node  # Apunta a sí mismo
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            
            new_node.next = self.head
            current.next = new_node
            self.head = new_node
        
        return self
    
    # 6. add_last(data) - Insertar un elemento al final
    def add_last(self, data):
        new_node = Node(data)
        
        if self.is_empty():
            self.head = new_node
            new_node.next = new_node  # Apunta a sí mismo
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            
            current.next = new_node
            new_node.next = self.head
        
        return self
    
    # 7. insert_at(index, data) - Insertar en una posición específica
    def insert_at(self, index, data):
        if index < 0:
            raise IndexError("Índice negativo no permitido")
        
        if index == 0:
            return self.add_first(data)
        
        new_node = Node(data)
        current = self.head
        position = 0
        
        while position < index - 1:
            current = current.next
            position += 1
            
            # Si damos la vuelta completa, el índice es mayor que el tamaño
            if current == self.head:
                raise IndexError("Índice fuera de rango")
        
        new_node.next = current.next
        current.next = new_node
        
        return self
    
    # 8. insert_after(node, data) - Insertar después de un nodo específico
    def insert_after(self, node, data):
        if node is None:
            raise ValueError("El nodo no puede ser None")
        
        new_node = Node(data)
        new_node.next = node.next
        node.next = new_node
        
        return self
    
    # 9. insert_before(node, data) - Insertar antes de un nodo específico
    def insert_before(self, node, data):
        if node is None or self.is_empty():
            raise ValueError("El nodo no puede ser None y la lista no puede estar vacía")
        
        # Si el nodo es la cabeza
        if node == self.head:
            return self.add_first(data)
        
        current = self.head
        while current.next != self.head and current.next != node:
            current = current.next
        
        if current.next == self.head:
            raise ValueError("El nodo no está en la lista")
        
        new_node = Node(data)
        new_node.next = node
        current.next = new_node
        
        return self
    
    # 10. insert_sorted(data) - Insertar en orden (lista ordenada)
    def insert_sorted(self, data):
        if self.is_empty() or data <= self.head.data:
            return self.add_first(data)
        
        current = self.head
        
        # Encontrar el lugar para insertar
        while current.next != self.head and current.next.data < data:
            current = current.next
        
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node
        
        return self
    
    # 11. remove_first() - Eliminar el primer elemento
    def remove_first(self):
        if self.is_empty():
            raise ValueError("No se puede eliminar de una lista vacía")
        
        if self.head.next == self.head:  # Solo hay un elemento
            removed_data = self.head.data
            self.head = None
            return removed_data
        
        removed_data = self.head.data
        current = self.head
        
        # Encontrar el último nodo
        while current.next != self.head:
            current = current.next
        
        # Ajustar la cabeza y el último nodo
        current.next = self.head.next
        self.head = self.head.next
        
        return removed_data
    
    # 12. remove_last() - Eliminar el último elemento
    def remove_last(self):
        if self.is_empty():
            raise ValueError("No se puede eliminar de una lista vacía")
        
        if self.head.next == self.head:  # Solo hay un elemento
            removed_data = self.head.data
            self.head = None
            return removed_data
        
        current = self.head
        previous = None
        
        # Encontrar el último y penúltimo nodo
        while current.next != self.head:
            previous = current
            current = current.next
        
        # Eliminar el último nodo
        previous.next = self.head
        removed_data = current.data
        
        return removed_data
    
    # 13. remove_at(index) - Eliminar en una posición específica
    def remove_at(self, index):
        if self.is_empty():
            raise ValueError("No se puede eliminar de una lista vacía")
        
        if index < 0:
            raise IndexError("Índice negativo no permitido")
        
        if index == 0:
            return self.remove_first()
        
        current = self.head
        previous = None
        position = 0
        
        while position < index:
            previous = current
            current = current.next
            position += 1
            
            # Si damos la vuelta completa, el índice es mayor que el tamaño
            if current == self.head:
                raise IndexError("Índice fuera de rango")
        
        # Eliminar el nodo
        previous.next = current.next
        removed_data = current.data
        
        return removed_data
    
    # 14. remove_node(node) - Eliminar un nodo específico
    def remove_node(self, node):
        if self.is_empty() or node is None:
            raise ValueError("La lista está vacía o el nodo es None")
        
        if node == self.head:
            return self.remove_first()
        
        current = self.head
        
        # Buscar el nodo anterior al que queremos eliminar
        while current.next != self.head and current.next != node:
            current = current.next
        
        if current.next == self.head:
            raise ValueError("El nodo no está en la lista")
        
        # Eliminar el nodo
        current.next = node.next
        removed_data = node.data
        
        return removed_data
    
    # 15. remove_by_value(data) - Eliminar por valor
    def remove_by_value(self, data):
        if self.is_empty():
            raise ValueError("No se puede eliminar de una lista vacía")
        
        if self.head.data == data:
            return self.remove_first()
        
        current = self.head
        
        # Buscar el nodo con el valor
        while current.next != self.head and current.next.data != data:
            current = current.next
        
        if current.next == self.head:
            raise ValueError(f"El valor {data} no está en la lista")
        
        # Eliminar el nodo
        removed_node = current.next
        current.next = removed_node.next
        
        return data
    
    # 16. remove_duplicates() - Eliminar elementos duplicados
    def remove_duplicates(self):
        if self.is_empty() or self.head.next == self.head:
            return self  # Lista vacía o con un solo elemento
        
        values = set()
        current = self.head
        values.add(current.data)
        
        while current.next != self.head:
            if current.next.data in values:
                # Duplicado encontrado, eliminarlo
                current.next = current.next.next
            else:
                # Nuevo valor, agregarlo al conjunto
                values.add(current.next.data)
                current = current.next
        
        return self
    
    # 17. search(data) - Buscar un elemento y retornar el nodo
    def search(self, data):
        if self.is_empty():
            return None
        
        if self.head.data == data:
            return self.head
        
        current = self.head.next
        
        while current != self.head:
            if current.data == data:
                return current
            current = current.next
        
        return None  # No encontrado
    
    # 18. contains(data) - Verificar si un elemento existe
    def contains(self, data):
        return self.search(data) is not None
    
    # 19. index_of(data) - Obtener la posición de un elemento
    def index_of(self, data):
        if self.is_empty():
            return -1
        
        if self.head.data == data:
            return 0
        
        current = self.head.next
        index = 1
        
        while current != self.head:
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
        
        while current != self.head:
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
        
        while current != self.head:
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
        
        # Fast avanza dos veces más rápido que slow
        while fast.next != self.head and fast.next.next != self.head:
            slow = slow.next
            fast = fast.next.next
        
        # Si hay un número par de elementos, devolver el segundo del medio
        if fast.next.next == self.head:
            return slow.next
        
        return slow
    
    # 23. get_first() - Obtener el primer elemento
    def get_first(self):
        if self.is_empty():
            raise ValueError("La lista está vacía")
        
        return self.head.data
    
    # 24. get_last() - Obtener el último elemento
    def get_last(self):
        if self.is_empty():
            raise ValueError("La lista está vacía")
        
        current = self.head
        
        while current.next != self.head:
            current = current.next
        
        return current.data
    
    # 25. get_at(index) - Obtener elemento en una posición específica
    def get_at(self, index):
        if self.is_empty():
            raise ValueError("La lista está vacía")
        
        if index < 0:
            raise IndexError("Índice negativo no permitido")
        
        if index == 0:
            return self.get_first()
        
        current = self.head
        position = 0
        
        while position < index:
            current = current.next
            position += 1
            
            if current == self.head:
                raise IndexError("Índice fuera de rango")
        
        return current.data
    
    # 26. get_node_at(index) - Obtener el nodo en una posición específica
    def get_node_at(self, index):
        if self.is_empty():
            raise ValueError("La lista está vacía")
        
        if index < 0:
            raise IndexError("Índice negativo no permitido")
        
        if index == 0:
            return self.head
        
        current = self.head
        position = 0
        
        while position < index:
            current = current.next
            position += 1
            
            if current == self.head:
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
        return CircularListIterator(self)
    
    # 30. for_each(func) - Aplicar una función a cada elemento
    def for_each(self, func):
        if self.is_empty():
            return self
        
        current = self.head
        func(current.data)
        current = current.next
        
        while current != self.head:
            func(current.data)
            current = current.next
        
        return self
    
    # 31. traverse() - Recorrer la lista e imprimir elementos
    def traverse(self):
        if self.is_empty():
            print("Lista vacía")
            return
        
        current = self.head
        print(current.data, end="")
        current = current.next
        
        while current != self.head:
            print(" -> ", end="")
            print(current.data, end="")
            current = current.next
        
        print()  # Nueva línea al final
    
    # 32. traverse_n_times(n) - Recorrer la lista n veces
    def traverse_n_times(self, n):
        if self.is_empty() or n <= 0:
            return
        
        current = self.head
        count = 0
        
        while count < n * self.length():
            print(current.data, end=" -> ")
            current = current.next
            count += 1
        
        print("...")  # Indicar que podría continuar
    
    # 33. iterate_from(start_node, steps) - Iterar desde un nodo específico
    def iterate_from(self, start_node, steps):
        if self.is_empty() or start_node is None:
            return None
        
        current = start_node
        
        for _ in range(steps):
            current = current.next
        
        return current
    
    # 34. map(func) - Aplicar una función y devolver nueva lista
    def map(self, func):
        if self.is_empty():
            return CircularLinkedList()
        
        result = CircularLinkedList()
        current = self.head
        
        # Agregar el primer elemento
        result.add_last(func(current.data))
        current = current.next
        
        # Agregar el resto de elementos
        while current != self.head:
            result.add_last(func(current.data))
            current = current.next
        
        return result
    
    # 35. filter(predicate) - Filtrar elementos según una condición
    def filter(self, predicate):
        if self.is_empty():
            return CircularLinkedList()
        
        result = CircularLinkedList()
        current = self.head
        
        # Verificar el primer elemento
        if predicate(current.data):
            result.add_last(current.data)
        
        current = current.next
        
        # Verificar el resto de elementos
        while current != self.head:
            if predicate(current.data):
                result.add_last(current.data)
            current = current.next
        
        return result
    
    # 36. reduce(func, initial) - Reducir la lista a un solo valor
    def reduce(self, func, initial):
        if self.is_empty():
            return initial
        
        result = initial
        current = self.head
        
        # Acumular el primer elemento
        result = func(result, current.data)
        current = current.next
        
        # Acumular el resto de elementos
        while current != self.head:
            result = func(result, current.data)
            current = current.next
        
        return result
    
    # 37. sort() - Ordenar la lista (utilizando bubble sort como ejemplo)
    def sort(self):
        if self.is_empty() or self.head.next == self.head:
            return self  # Lista vacía o con un solo elemento
        
        n = self.length()
        
        for i in range(n):
            current = self.head
            for j in range(n - i - 1):
                if current.data > current.next.data:
                    # Intercambiar datos
                    current.data, current.next.data = current.next.data, current.data
                current = current.next
        
        return self
    
    # 38. reverse() - Invertir el orden de los elementos
    def reverse(self):
        if self.is_empty() or self.head.next == self.head:
            return self  # Lista vacía o con un solo elemento
        
        prev = None
        current = self.head
        next_node = None
        
        # Guardar el primer nodo para actualizar después
        first = self.head
        
        while True:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            
            if current == self.head:
                break
        
        # Actualizar el enlace del último nodo al nuevo head
        first.next = prev
        self.head = prev
        
        return self
    
    # 39. shuffle() - Mezclar aleatoriamente los elementos
    def shuffle(self):
        import random
        
        if self.is_empty() or self.head.next == self.head:
            return self  # Lista vacía o con un solo elemento
        
        # Convertir a lista
        elements = []
        current = self.head
        elements.append(current.data)
        current = current.next
        
        while current != self.head:
            elements.append(current.data)
            current = current.next
        
        # Mezclar
        random.shuffle(elements)
        
        # Reconstruir la lista
        self.clear()
        for element in elements:
            self.add_last(element)
        
        return self
    
    # 40. merge(other_list) - Combinar con otra lista
    def merge(self, other_list):
        if other_list.is_empty():
            return self
        
        if self.is_empty():
            self.head = other_list.head
            return self
        
        # Obtener el último nodo de esta lista
        last = self.head
        while last.next != self.head:
            last = last.next
        
        # Obtener el último nodo de la otra lista
        other_last = other_list.head
        while other_last.next != other_list.head:
            other_last = other_last.next
        
        # Conectar las listas
        last.next = other_list.head
        other_last.next = self.head
        
        return self
    
    # 41. concat(other_list) - Concatenar con otra lista (copia los elementos)
    def concat(self, other_list):
        result = CircularLinkedList()
        
        # Copiar esta lista
        if not self.is_empty():
            current = self.head
            result.add_last(current.data)
            current = current.next
            
            while current != self.head:
                result.add_last(current.data)
                current = current.next
        
        # Copiar la otra lista
        if not other_list.is_empty():
            current = other_list.head
            result.add_last(current.data)
            current = current.next
            
            while current != other_list.head:
                result.add_last(current.data)
                current = current.next
        
        return result
    
    # 42. intersect(other_list) - Elementos comunes con otra lista
    def intersect(self, other_list):
        result = CircularLinkedList()
        
        if self.is_empty() or other_list.is_empty():
            return result
        
        # Conjunto para almacenar elementos de la otra lista
        other_elements = set()
        current = other_list.head
        other_elements.add(current.data)
        current = current.next
        
        while current != other_list.head:
            other_elements.add(current.data)
            current = current.next
        
        # Verificar elementos comunes
        current = self.head
        if current.data in other_elements and not result.contains(current.data):
            result.add_last(current.data)
        current = current.next
        
        while current != self.head:
            if current.data in other_elements and not result.contains(current.data):
                result.add_last(current.data)
            current = current.next
        
        return result
    
    # 43. difference(other_list) - Elementos que están en una pero no en otra
    def difference(self, other_list):
        result = CircularLinkedList()
        
        if self.is_empty():
            return result
        
        if other_list.is_empty():
            return self.concat(CircularLinkedList())  # Crear una copia
        
        # Conjunto para almacenar elementos de la otra lista
        other_elements = set()
        current = other_list.head
        other_elements.add(current.data)
        current = current.next
        
        while current != other_list.head:
            other_elements.add(current.data)
            current = current.next
        
        # Agregar elementos que no están en la otra lista
        current = self.head
        if current.data not in other_elements:
            result.add_last(current.data)
        current = current.next
        
        while current != self.head:
            if current.data not in other_elements:
                result.add_last(current.data)
            current = current.next
        
        return result
    
    # 44. is_subset(other_list) - Verificar si una lista es subconjunto de otra
    def is_subset(self, other_list):
        if other_list.is_empty():
            return True  # Una lista vacía es subconjunto de cualquier lista
        
        if self.is_empty():
            return False  # Esta lista vacía no contiene elementos de la otra
        
        # Conjunto para almacenar los elementos de esta lista
        elements = set()
        current = self.head
        elements.add(current.data)
        current = current.next
        
        while current != self.head:
            elements.add(current.data)
            current = current.next
        
        # Verificar si todos los elementos de la otra lista están en esta lista
        current = other_list.head
        if current.data not in elements:
            return False
        current = current.next
        
        while current != other_list.head:
            if current.data not in elements:
                return False
            current = current.next
        
        return True
    
    # 45. split_at(index) - Dividir la lista en dos en una posición
    def split_at(self, index):
        if self.is_empty():
            return CircularLinkedList(), CircularLinkedList()
        
        if index <= 0:
            return CircularLinkedList(), self.concat(CircularLinkedList())
        
        length = self.length()
        if index >= length:
            return self.concat(CircularLinkedList()), CircularLinkedList()
        
        # Primera parte
        first_part = CircularLinkedList()
        current = self.head
        for i in range(index):
            first_part.add_last(current.data)
            current = current.next
        
        # Segunda parte
        second_part = CircularLinkedList()
        for i in range(index, length):
            second_part.add_last(current.data)
            current = current.next
        
        return first_part, second_part
    
    # 46. rotate_right(k) - Rotar k posiciones a la derecha
    def rotate_right(self, k):
        if self.is_empty() or self.head.next == self.head or k <= 0:
            return self
        
        length = self.length()
        k = k % length  # Normalizar k
        
        if k == 0:
            return self
        
        # Encontrar nuevo nodo cabeza
        steps = length - k
        new_head = self.head
        
        for _ in range(steps):
            new_head = new_head.next
        
        # Actualizar la cabeza
        self.head = new_head
        
        return self
    
    # 47. rotate_left(k) - Rotar k posiciones a la izquierda
    def rotate_left(self, k):
        if self.is_empty() or self.head.next == self.head or k <= 0:
            return self
        
        length = self.length()
        k = k % length  # Normalizar k
        
        if k == 0:
            return self
        
        # Rotar a la izquierda k posiciones es lo mismo que
        # rotar a la derecha (length - k) posiciones
        return self.rotate_right(length - k)
    
    # 48. rotate_to_front(node) - Rotar para que un nodo quede al frente
    def rotate_to_front(self, node):
        if self.is_empty() or node is None or node == self.head:
            return self
        
        # Verificar si el nodo está en la lista
        current = self.head
        found = False
        
        while current.next != self.head:
            if current.next == node:
                found = True
                break
            current = current.next
        
        if not found and current.next != node:
            raise ValueError("El nodo no está en la lista")
        
        # Actualizar la cabeza
        self.head = node
        
        return self
    
    # 49. rotate_till_sorted() - Rotar hasta encontrar una secuencia ordenada
    def rotate_till_sorted(self):
        if self.is_empty() or self.head.next == self.head:
            return self  # Lista vacía o con un solo elemento
        
        length = self.length()
        min_value = self.find_min()
        
        # Rotar hasta que el valor mínimo esté al frente
        current = self.head
        for _ in range(length):
            if current.data == min_value:
                self.head = current
                break
            current = current.next
        
        return self
    
    # 50. rotate_random() - Rotar aleatoriamente
    def rotate_random(self):
        import random
        
        if self.is_empty() or self.head.next == self.head:
            return self  # Lista vacía o con un solo elemento
        
        length = self.length()
        steps = random.randint(0, length - 1)
        
        return self.rotate_right(steps)
    
    # 51. is_sorted() - Verificar si la lista está ordenada
    def is_sorted(self):
        if self.is_empty() or self.head.next == self.head:
            return True  # Lista vacía o con un solo elemento está ordenada
        
        current = self.head
        while current.next != self.head:
            if current.data > current.next.data:
                return False
            current = current.next
        
        return True
    
    # 52. is_palindrome() - Verificar si la lista es un palíndromo
    def is_palindrome(self):
        if self.is_empty() or self.head.next == self.head:
            return True  # Lista vacía o con un solo elemento es palíndromo
        
        # Convertir la lista a una lista normal para comparar
        values = []
        current = self.head
        values.append(current.data)
        current = current.next
        
        while current != self.head:
            values.append(current.data)
            current = current.next
        
        # Verificar si es palíndromo
        return values == values[::-1]
    def tirardado(self,posact):
        newpos=posact+random.randint(1, 6)
        return self.get_at(newpos)
        
        

# Iterador para lista circular
class CircularListIterator:
    def __init__(self, circular_list):
        self.circular_list = circular_list
        self.current = circular_list.head
        self.started = False
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.circular_list.is_empty():
            raise StopIteration
        
        if not self.started:
            self.started = True
            return self.current.data
        
        self.current = self.current.next
        
        if self.current == self.circular_list.head:
            raise StopIteration
        
        return self.current.data


#monopolio
mapa= CircularLinkedList()
mapa.add_first("prop1")
mapa.add_first("prop2")
mapa.add_first("prop3")
mapa.add_first("prop4")
mapa.add_first("prop5")
mapa.add_first("prop6")
mapa.add_first("prop7")
mapa.add_first("prop8")
mapa.add_first("prop9")
mapa.add_first("salida")
jugador1=CircularLinkedList()

jugador2=CircularLinkedList()


status = "playing"
p = input("jugador 1 o 2")
d = input("escribe l para lanzar el dado")
posact=0
while status !="over" :
    #parcial 2 quitar lasiguiente linea para reutlizar
    break
    if p == "1" and d =="l" :
        newpos=(posact+random.randint(1, 6)) % mapa.length()
        cayoen=mapa.get_at(newpos)   
        print("caiste en",cayoen)
        if cayoen=="salida":
               print("")
        else:
            if jugador1.contains(cayoen) is True :
                   print("ya eres el dueño de la propiedad ")
            elif jugador2.contains(cayoen) is True:
                   print("la propiedad ya tiene dueño")  
            elif jugador2.contains(cayoen) is False:
                   jugador1.add_first(cayoen)
                   print ("propiedad adquirida")
            
            
       
    if p =="2" and d =="l":
        newpos=(posact+random.randint(1, 6)) % mapa.length()
        cayoen=mapa.get_at(newpos)   
        print("caiste en",cayoen)
        if cayoen=="salida":
               print("caiste en ")
        else:
            if jugador2.contains(cayoen) is True :
                   print("ya eres el dueño de la propiedad ")
            elif jugador1.contains(cayoen) is True:
                   print("la propiedad ya tiene dueño")  
            elif jugador1.contains(cayoen) is False:
                   jugador2.add_first(cayoen)
                   print ("propiedad adquirida")
               
    posact =newpos    
    p = input("jugador 1 o 2")
    d = input("escribe l para lanzar el dado")
    if jugador1.length()+jugador2.length() >8:
        status="over"
        

import random

# Usamos las clases Node y CircularLinkedList que ya has implementado

def crear_juego_ruleta():
    # Crear lista de jugadores
    jugadores = CircularLinkedList()
    jugadores.add_last("Jugador 1")
    jugadores.add_last("Jugador 2")
    jugadores.add_last("Jugador 3")
    
    # Crear lista de premios/pruebas
    ruleta = CircularLinkedList()
    ruleta.add_last("$100")
    ruleta.add_last("$200")
    ruleta.add_last("$300")
    ruleta.add_last("$400")
    ruleta.add_last("$500")
    ruleta.add_last("Lanza de nuevo")
    ruleta.add_last("$700")
    ruleta.add_last("$800")
    ruleta.add_last("$900")
    ruleta.add_last("Eliminado del juego")
    
    # Posiciones actuales en la ruleta para cada jugador
    posiciones = {"Jugador 1": 0, "Jugador 2": 0, "Jugador 3": 0}
    
    # Jugadores eliminados
    eliminados = []
    
    # Jugador actual
    jugador_actual = jugadores.head
    
    # Flag para controlar el juego
    seguir_jugando = True
    
    print("¡Bienvenido al juego de la ruleta!")
    print("La ruleta tiene 10 casillas, incluyendo 'Lanza de nuevo' y 'Eliminado del juego'")
    
    while seguir_jugando:
        # Mostrar menú
        print("\n" + "="*50)
        print(f"Turno de: {jugador_actual.data}")
        print("1. Lanzar la ruleta")
        print("2. Salir del juego")
        opcion = input("Elija una opción: ")
        
        if opcion == "2":
            print("¡Gracias por jugar!")
            seguir_jugando = False
            continue
        
        elif opcion == "1":
            # Verificar si el jugador ya fue eliminado
            if jugador_actual.data in eliminados:
                print(f"{jugador_actual.data} ya fue eliminado. Pasando al siguiente jugador...")
                jugador_actual = jugador_actual.next
                continue
            
            # Lanzar la ruleta
            valor_lanzamiento = random.randint(1, 6)  # Simulando un dado
            print(f"{jugador_actual.data} ha lanzado y obtuvo un {valor_lanzamiento}")
            
            # Calcular nueva posición
            ultima_posicion = posiciones[jugador_actual.data]
            nueva_posicion = (ultima_posicion + valor_lanzamiento) % ruleta.length()
            posiciones[jugador_actual.data] = nueva_posicion
            
            # Obtener el premio
            premio = ruleta.get_at(nueva_posicion)
            print(f"Ha caído en la casilla {nueva_posicion}: {premio}")
            
            # Manejar casillas especiales
            lanzar_de_nuevo = False
            
            if premio == "Lanza de nuevo":
                print(f"¡{jugador_actual.data} puede lanzar de nuevo!")
                lanzar_de_nuevo = True
            
            elif premio == "Eliminado del juego":
                print(f"¡{jugador_actual.data} ha sido eliminado del juego!")
                eliminados.append(jugador_actual.data)
                
                # Verificar si quedan jugadores
                if len(eliminados) == jugadores.length():
                    print("¡Todos los jugadores han sido eliminados! Fin del juego.")
                    seguir_jugando = False
                    continue
                elif len(eliminados) == jugadores.length() - 1:
                    # Solo queda un jugador
                    ganador = None
                    temp = jugadores.head
                    for _ in range(jugadores.length()):
                        if temp.data not in eliminados:
                            ganador = temp.data
                            break
                        temp = temp.next
                    
                    print(f"¡Solo queda un jugador! {ganador} es el ganador.")
                    seguir_jugando = False
                    continue
            
            # Mostrar estado actual
            print("\nEstado actual:")
            print(f"{'Jugador':<10} {'Posición':<10} {'Estado':<15}")
            temp = jugadores.head
            for _ in range(jugadores.length()):
                estado = "Eliminado" if temp.data in eliminados else "Activo"
                print(f"{temp.data:<10} {posiciones[temp.data]:<10} {estado:<15}")
                temp = temp.next
            
            # Pasar al siguiente jugador si no obtuvo "Lanza de nuevo"
            if not lanzar_de_nuevo:
                jugador_actual = jugador_actual.next
        
        else:
            print("Opción no válida. Intente de nuevo.")
    
    print("Fin del juego.")

# Ejecutar el juego
if __name__ == "__main__":
    crear_juego_ruleta()
    
        

    
    
      
        

              
        
     
        
     