class Nodo:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
     
class Lista_enlazada:
    def __init__(self):
        self.head = None

    # Método para agregar elementos en el frente de la linked list
    def agregar_al_inicio(self, data):
        self.head = Nodo(data=data, next=self.head)
        #nuevo_nodo = Nodo(data)
        #nuevo_nodo.next = self.head
        #return nuevo_nodo

    # Método para verificar si la estructura de datos esta vacia
    def is_empty(self):
        return self.head == None

    # Método para agregar elementos al final de la lista enlazada
    def agregar_al_final(self, data):
      #Si la lista no existe, entonces se crea
        if not self.head:
            self.head = Nodo(data=data)
            return
        #recorre toda la lista hasta llegar al final,
        #cuando temporal.next=None
        temporal = self.head
        while temporal.next:
            temporal = temporal.next
        #Cuando llega al final de la lista, enlaza el último nodo con
        #el nuevo nodo que se crea
        temporal.next = Nodo(data=data)

    # Método para eleminar nodos
    def delete_node(self, key):
        actual = self.head
        previo = None
        #Se busca el dato a eliminar en la lista
        while actual and actual.data != key:
            previo = actual
            actual = actual.next
        #Si el dato a eliminar es el primero,
        #entonces se reasigna la cabeza de la lista
        if previo is None:
            self.head = actual.next
        elif actual:
            previo.next = actual.next
            actual.next = None

    # Método para obtener el ultimo nodo
    def get_last_node(self):
        temp = self.head
        while(temp.next is not None):
            temp = temp.next
        return temp.data

    # Método para imprimir la lista de nodos
    def print_list( self ):
        node = self.head
        while node != None:
            print(node.data, end =" --> ")
            node = node.next
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
    
    # Método para encontrar el mínimo de una lista - CORREGIDO: INDENTACIÓN
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
    
    # Método para calcular el promedio - CORREGIDO: INDENTACIÓN Y RETURN
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
"""
Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10). A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor.
"""
def solucion3():
    Mi_ListaNotas = Lista_enlazada()
    for i in range(5):
        while True:
            try:
                nota = float(input(f"ingrese la nota {i+1}:"))
                if 0 <= nota <= 10:
                    Mi_ListaNotas.agregar_al_inicio(nota)
                    break
                else:
                    print("Tu nota no es valida titan")
            except ValueError:
                print("Usa valores numericos")
    Mi_ListaNotas.print_list()
    maximo = Mi_ListaNotas.encontrar_maximo()
    minimo = Mi_ListaNotas.encontrar_minimo()
    promedio = Mi_ListaNotas.calcular_promedio()
    
    print(f"el maximo de la lista es: {maximo}")
    print(f"el minimo de la lista es: {minimo}")
    print(f"el promedio de la lista es: {promedio}")
    

solucion3()

    





    

