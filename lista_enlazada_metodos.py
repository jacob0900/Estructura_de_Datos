#Crnt+f para buscar cosas
class Nodo:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Lista_enlazada:
    def __init__(self):
        self.head = None

    # Método para verificar si la estructura de datos está vacía
    def is_empty(self):
        return self.head == None

    # Método para agregar elementos en el frente de la linked list
    def agregar_al_inicio(self, data):
        self.head = Nodo(data=data, next=self.head)

    # Método para agregar elementos al final de la lista enlazada
    def agregar_al_final(self, data):
        # Si la lista no existe, entonces se crea
        if not self.head:
            self.head = Nodo(data=data)
            return
        # Recorre toda la lista hasta llegar al final,
        # cuando temporal.next=None
        temporal = self.head
        while temporal.next:
            temporal = temporal.next
        # Cuando llega al final de la lista, enlaza el último nodo con
        # el nuevo nodo que se crea
        temporal.next = Nodo(data=data)

    # Método para eliminar nodos
    def delete_node(self, key):
        actual = self.head
        previo = None
        # Se busca el dato a eliminar en la lista
        while actual and actual.data != key:
            previo = actual
            actual = actual.next
        # Si el dato a eliminar es el primero,
        # entonces se reasigna la cabeza de la lista
        if previo is None:
            self.head = actual.next
        elif actual:
            previo.next = actual.next
            actual.next = None

    # Método para obtener el último nodo
    def get_last_node(self):
        temp = self.head
        while(temp.next is not None):
            temp = temp.next
        return temp.data

    # Método para imprimir la lista de nodos
    def print_list(self):
        node = self.head
        while node != None:
            print(node.data, end=" --> ")
            node = node.next
        print("None")  # Para mostrar el final de la lista

    # Método para encontrar el máximo de una lista 
    def encontrar_maximo(self):
        if self.is_empty():
            return None
        
        maximo = self.head.data
        actual = self.head
        
        while actual:
            if actual.data > maximo:
                maximo = actual.data
            actual = actual.next
        
        return maximo

    # Método para encontrar el mínimo de una lista
    def encontrar_minimo(self):
        if self.is_empty():
            return None
        
        minimo = self.head.data
        actual = self.head
        
        while actual:
            if actual.data < minimo:
                minimo = actual.data
            actual = actual.next
        
        return minimo
    
    # Método para calcular el promedio
    def calcular_promedio(self):
        if self.is_empty():
            return None

        suma = 0
        contador = 0
        actual = self.head

        while actual:
            suma += actual.data
            contador += 1
            actual = actual.next

        if contador == 0:
            return 0
            
        return suma / contador

    # Método flexible para buscar nodos por valor o posición
    def buscar_nodo(self, valor=None, indice=None, obtener_solo_valor=False):
        # Verificar que se proporcione al menos un criterio de búsqueda
        if valor is None and indice is None:
            return None
        
        # Verificar si la lista está vacía
        if self.is_empty():
            return None
        
        actual = self.head
        posicion = 0
        
        # Búsqueda por valor
        if valor is not None:
            while actual:
                if actual.data == valor:
                    return actual.data if obtener_solo_valor else (actual, posicion)
                actual = actual.next
                posicion += 1
            return None  # No se encontró el valor
        
        # Búsqueda por índice/posición
        elif indice is not None:
            if indice < 0:
                return None  # Índice inválido
            
            while actual and posicion < indice:
                actual = actual.next
                posicion += 1
            
            if actual and posicion == indice:
                return actual.data if obtener_solo_valor else actual
            else:
                return None  # Posición fuera de rango
    
    # Método para agregar en el medio - corregido la indentación
    def agregar_en_medio(self, data):
        # Si la lista está vacía, simplemente agregamos al inicio
        if self.is_empty():
            self.agregar_al_inicio(data)
            return
        
        # Calcular la longitud de la lista
        longitud = 0
        temp = self.head
        while temp:
            longitud += 1
            temp = temp.next
        
        # Encontrar la posición media
        posicion_media = longitud // 2
        
        # Si la posición media es 0 (lista de un solo elemento), insertamos al inicio
        if posicion_media == 0:
            self.agregar_al_inicio(data)
            return
        
        # Navegar hasta la posición anterior al punto medio
        temp = self.head
        for i in range(posicion_media - 1):
            temp = temp.next
        
        # Insertar el nuevo nodo después de temp
        nuevo_nodo = Nodo(data)
        nuevo_nodo.next = temp.next
        temp.next = nuevo_nodo
    
    #verificar que un numero sea entero o decimal
    def ValidarQueEsUn_numero(self, valor):
        if isinstance(valor, (int, float)):
            return valor
        else:
            print("ERROR: El valor debe ser numérico")
            return False
    
    #Metodo para poner el cero en la mitad positivos a la derecha y negativos a la izquierda
    def poner_numerosListaSegunOrdenAscendente(self, input):
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
            # Buscar el punto de inserción para el 0
            if self.head.data >= 0:  # Si el primer elemento es positivo o cero, insertar al inicio
                self.agregar_al_inicio(0)
                return True

            actual = self.head
            while actual.next and actual.next.data < 0:
                actual = actual.next

            # Insertar el 0 después del último negativo
            nuevo_nodo = Nodo(0)
            nuevo_nodo.next = actual.next
            actual.next = nuevo_nodo
            return True

    def Verificacion_NoRepetidos(self, valor):
        if self.is_empty():
            return True

        actual = self.head
        while actual:
            if actual.data == valor:
                print("ERROR: El valor ya existe en la lista")
                return False  # El valor ya existe en la lista
            actual = actual.next
        return True  # El valor no existe en la lista 
