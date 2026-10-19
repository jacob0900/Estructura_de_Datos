
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
      
"""
Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo
"""
import random 

def solucion_1():
    Mi_lista = Lista_enlazada()
    Mi_lista2 = Lista_enlazada()
    Mi_lista3 = Lista_enlazada()
    cont = 0
    while cont < 10 :
        a = random.randint(0, 10)
        Mi_lista.agregar_al_final(a)
        Mi_lista2.agregar_al_final(a**2)
        Mi_lista3.agregar_al_final(a**3)
        cont += 1

    Mi_lista.print_list()
    print("\n")
    Mi_lista2.print_list()
    print("\n")
    Mi_lista3.print_list()
    print("\n")

solucion_1()    