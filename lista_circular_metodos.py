class Nodo:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class ListaCircular:
    def __init__(self):
        """Inicializa una lista circular vacía."""
        self.head = None

    def is_empty(self):
        """Verifica si la lista está vacía."""
        return self.head is None

    def agregar_al_inicio(self, data):
        """Agrega un elemento al inicio de la lista."""
        new_node = Nodo(data=data, next=self.head)
        if self.is_empty():
            new_node.next = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
        self.head = new_node

    def agregar_al_final(self, data):
        """Agrega un elemento al final de la lista."""
        if self.is_empty():
            self.head = Nodo(data=data, next=self.head)
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = Nodo(data=data, next=self.head)

    def delete_node(self, key):
        """Elimina un nodo con el valor especificado."""
        if self.is_empty():
            return

        if self.head.data == key:
            if self.head.next == self.head:
                self.head = None
            else:
                current = self.head
                while current.next != self.head:
                    current = current.next
                self.head = self.head.next
                current.next = self.head
            return

        current = self.head
        while current.next != self.head and current.next.data != key:
            current = current.next

        if current.next == self.head:
            return

        current.next = current.next.next

    def get_last_node(self):
        """Obtiene el último nodo de la lista."""
        if self.is_empty():
            return None

        current = self.head
        while current.next != self.head:
            current = current.next
        return current.data

    def print_list(self):
        """Imprime los elementos de la lista."""
        if self.is_empty():
            print("La lista está vacía.")
            return

        current = self.head
        while True:
            print(current.data, end=" --> ")
            current = current.next
            if current == self.head:
                break
        print("None")

    def encontrar_maximo(self):
        """Encuentra el valor máximo en la lista."""
        if self.is_empty():
            return None

        maximo = self.head.data
        current = self.head

        while True:
            if current.data > maximo:
                maximo = current.data
            current = current.next
            if current == self.head:
                break

        return maximo

    def encontrar_minimo(self):
        """Encuentra el valor mínimo en la lista."""
        if self.is_empty():
            return None

        minimo = self.head.data
        current = self.head

        while True:
            if current.data < minimo:
                minimo = current.data
            current = current.next
            if current == self.head:
                break

        return minimo

    def calcular_promedio(self):
        """Calcula el promedio de los valores en la lista."""
        if self.is_empty():
            return None

        suma = 0
        contador = 0
        current = self.head

        while True:
            suma += current.data
            contador += 1
            current = current.next
            if current == self.head:
                break

        return suma / contador if contador != 0 else 0

    def buscar_nodo(self, valor=None, indice=None, obtener_solo_valor=False):
        """Busca un nodo por valor o índice."""
        if valor is None and indice is None:
            return None

        if self.is_empty():
            return None

        current = self.head
        posicion = 0

        if valor is not None:
            while True:
                if current.data == valor:
                    return current.data if obtener_solo_valor else (current, posicion)
                current = current.next
                posicion += 1
                if current == self.head:
                    break
            return None

        if indice is not None:
            if indice < 0:
                return None

            while posicion < indice:
                current = current.next
                posicion += 1
                if current == self.head:
                    return None

            return current.data if obtener_solo_valor else current

    def agregar_en_medio(self, data):
        """Agrega un elemento en la posición media de la lista."""
        if self.is_empty():
            self.agregar_al_inicio(data)
            return

        longitud = 0
        current = self.head
        while True:
            longitud += 1
            current = current.next
            if current == self.head:
                break

        posicion_media = longitud // 2

        if posicion_media == 0:
            self.agregar_al_inicio(data)
            return

        current = self.head
        for _ in range(posicion_media - 1):
            current = current.next

        nuevo_nodo = Nodo(data)
        nuevo_nodo.next = current.next
        current.next = nuevo_nodo

    def validar_que_es_numero(self, valor):
        """Valida que un valor sea un número entero o decimal."""
        if isinstance(valor, (int, float)):
            return valor
        else:
            print("ERROR: El valor debe ser numérico")
            return False

    def poner_numeros_lista_segun_orden_ascendente(self, input):
        """Pone los números en la lista según el orden ascendente."""
        if self.is_empty():
            self.agregar_al_inicio(input)
            return True

        if input < 0:
            self.agregar_al_inicio(input)
            return True

        if input > 0:
            self.agregar_al_final(input)
            return True

        if input == 0:
            if self.head.data >= 0:
                self.agregar_al_inicio(0)
                return True

            current = self.head
            while current.next != self.head and current.next.data < 0:
                current = current.next

            nuevo_nodo = Nodo(0)
            nuevo_nodo.next = current.next
            current.next = nuevo_nodo
            return True

    def verificacion_no_repetidos(self, valor):
        """Verifica que un valor no esté repetido en la lista."""
        if self.is_empty():
            return True

        current = self.head
        while True:
            if current.data == valor:
                print("ERROR: El valor ya existe en la lista")
                return False
            current = current.next
            if current == self.head:
                break
        return True

