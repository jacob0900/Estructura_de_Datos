import csv
import datetime

# TAD 
class SistemaPago:
    def __init__(self):
        self.precio_boleta = 9000  # Precio fijo de la boleta
        self.ingresos_por_sala = {}  # Diccionario para registrar ingresos por sala
    
    def inicializar_sala(self, nro_sala):
        """Inicializa el contador de ingresos para una sala si no existe"""
        if nro_sala not in self.ingresos_por_sala:
            self.ingresos_por_sala[nro_sala] = 0
    
    def procesar_pago(self, nro_sala):
        """Procesa el pago de una boleta y retorna True si el pago es exitoso"""
        print(f"\n=== PAGO DE BOLETA ===")
        print(f"El precio de la boleta es: ${self.precio_boleta} pesos")
        
        try:
            monto_pagado = int(input("Ingrese el monto a pagar: "))
            
            if monto_pagado >= self.precio_boleta:
                
                self.registrar_ingreso(nro_sala)
                
                # Calcular cambio si es necesario
                if monto_pagado > self.precio_boleta:
                    cambio = monto_pagado - self.precio_boleta
                    print(f"Su cambio es: ${cambio} pesos")
                
                print("¡Pago exitoso! Puede seleccionar su asiento.")
                return True
            else:
                print(f"El monto ingresado (${monto_pagado}) es insuficiente.")
                return False
                
        except ValueError:
            print("Por favor ingrese un monto válido.")
            return False
    
    def registrar_ingreso(self, nro_sala):
        """Registra un ingreso para la sala especificada"""
        self.inicializar_sala(nro_sala)
        self.ingresos_por_sala[nro_sala] += self.precio_boleta
    
    def mostrar_ingresos(self):
        """Muestra un reporte de los ingresos por sala"""
        print("\n=== REPORTE DE INGRESOS POR SALA ===")
        total = 0
        for sala, ingreso in self.ingresos_por_sala.items():
            print(f"Sala {sala}: ${ingreso} pesos")
            total += ingreso
        print(f"Total de ingresos: ${total} pesos")

# Crear una instancia global del sistema de pago
sistema_pago = SistemaPago()

class room:
    
    def __init__(self,nombre,sc,nro,sala):
        self.pelicula=nombre
        self.schedule=sc
        self.nrosala=nro
        self.sala = sala
        
        
        
    def showingcartelera(self,k):
        print(f"id:{k+1}")  # Ajustado para mostrar ids desde 1 para el usuario
        print(f"Película: {self.pelicula}")
        print(f"Horario: {self.schedule}")
        print(f"Sala: {self.nrosala}")
        
    
        print()
            
    def showingchair(self):
        print("\n Distribución de asientos:")
        print("    " + "   ".join(str(i + 1) for i in range(10)))  # Encabezado de columnas (1-10)
        for idx, fila in enumerate(self.sala, start=1):
           print(f"{idx:2} | {fila}")  # Índice de fila + datos
           print()    
            
def crearmatrizsala(nume):
    filas= 8
    columnas = 10
    num = str(nume)
    matriz =[]
    for i in range(filas):
        fila =[]
        for j in range(columnas):
            indice = i*columnas+j
            if indice < len(num):
                fila.append(int(num[indice]))
            else:
                fila.append(0)  # Asegurarse de que todas las posiciones estén inicializadas
        matriz.append(fila)            
    return matriz


with open("peliculaslab2.csv", "r", encoding="utf-8") as file:
    contenido = csv.reader(file)
    funciones =[]
    next(contenido)
    for i in range(6):
        try:
            line = next(contenido)
            nombre = line[0]
            horario = line[1]
            nrosala = line[2]
            sla =line[3]
            sala = crearmatrizsala(sla)
            x = room(nombre,horario,nrosala,sala)
            funciones.append(x)
        except StopIteration:
            break  # Si hay menos de 6 líneas en el archivo
        
        
def mostrarcartelera(funciones):
    print("==========CARTELERA==========")
    for i in range(len(funciones)):
        y=funciones[i]
        k=i
        y.showingcartelera(k)

def es_hora_mayor(hora_objetivo):
    formato = "%H:%M"
    ahora = datetime.datetime.now().strftime(formato)
    hora_actual = datetime.datetime.strptime(ahora, formato)
    hora_objetivo = datetime.datetime.strptime(hora_objetivo, formato)
    
    return hora_actual > hora_objetivo




def validationtime(funciones, sel):
    for i in range(len(funciones)):
        y = funciones[i]
        if i == sel-1:
            hora_funcion = y.schedule
            
            # Calculamos la hora límite (30 minutos después del inicio)
            formato = "%H:%M"
            hora_inicio = datetime.datetime.strptime(hora_funcion, formato)
            hora_limite = hora_inicio + datetime.timedelta(minutes=30)
            hora_limite_str = hora_limite.strftime(formato)
            
            # Verificamos si la hora actual es mayor que la hora límite
            if es_hora_mayor(hora_limite_str):
                print("La función lleva más de 30 minutos de iniciada, no se puede ingresar")
                return False
            elif es_hora_mayor(hora_funcion):
                print("La función ya comenzó pero todavía puedes ingresar")
                return True
            else:
                print("La función aún no comienza, puedes ingresar")
                return True
    return False  # Si no encuentra la función



def versala(funciones,sel):     
        for i in range(len(funciones)):
            y=funciones[i]
            if i==sel-1:
                y.showingchair()
                return y.nrosala  # Retorna el número de sala para usarlo en el sistema de pago
        return None
                
# Función de reservar puestos

def reservar_asiento(funciones, sel):
    for i in range(len(funciones)):
        y = funciones[i]
        if i == sel - 1:  
            print("\n=== SELECCIÓN DE ASIENTO ===")
            #y.showingchair()  
            
            try:
                fila = int(input("Ingrese el número de fila: ")) - 1  
                columna = int(input("Ingrese el número de columna: ")) - 1
                    
                if 0 <= fila < 8 and 0 <= columna < 10:
                    if y.sala[fila][columna] == 0:
                            y.sala[fila][columna] = 1  
                            print("\n¡Se ha reservado su asiento!")
                            y.showingchair()  
                    else:
                            print("El asiento ya está ocupado.")
                else:
                        print("Fila o columna no existen.")
            except ValueError:
                print("Por favor ingrese números válidos.")
            
            return
 
            
#MENUUUUUU                
                
interruptor = "stay"
while interruptor != "salir":
    seleccion = input("\nPresione 1 para conocer la cartelera, 2 para ver ingresos, 'salir' para terminar: ")
    
    if seleccion.lower() == "salir":
        interruptor = "salir"
        print("¡Gracias por usar el sistema de cine!")
    elif seleccion == "1":
        mostrarcartelera(funciones)
        sel = input("¿A cuál función desea ingresar? (número): ")
        try:
            sel_num = int(sel)
            if 1 <= sel_num <= len(funciones):  # Verificar que el número esté en rango
                if validationtime(funciones, sel_num):
                    # Obtener el número de sala
                    sala_actual = versala(funciones, sel_num)
                    
                    # Procesar el pago antes de permitir la reserva
                    if sistema_pago.procesar_pago(sala_actual):
                        reservar_asiento(funciones, sel_num)
                else:
                    # No hacer nada si la validación de tiempo falló
                    pass
            else:
                print("Número de función inválido.")
        except ValueError:
            print("Por favor ingrese un número válido.")
    elif seleccion == "2":
        sistema_pago.mostrar_ingresos()
    else:
        print("Opción no válida.")







        
        
        
                
    







    