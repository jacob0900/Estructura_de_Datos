
import itertools

def cargar_correlaciones(archivo='correlaciones.txt'):
    """
    Carga y valida las correlaciones entre acciones desde un archivo.
    
    El formato esperado del archivo es:
    - Primera línea: Número entero 'n' que representa la cantidad de acciones
    - Siguientes n(n-1)/2 líneas: ACCION1 ACCION2 correlacion
    
    Args:
        archivo (str): Ruta al archivo de correlaciones (default: 'correlaciones.txt')
        
    Returns:
        tuple: (número de acciones, diccionario de correlaciones)
        
    Raises:
        FileNotFoundError: Si el archivo no existe
        ValueError: Si el formato o los valores en el archivo son incorrectos
        Exception: Para otros errores durante la carga
    """
    try:
        with open(archivo, 'r') as file:
            lineas = file.readlines()

        # Validar que el archivo no esté vacío
        if not lineas:
            raise ValueError("El archivo de correlaciones está vacío")

        # Obtener y validar el número de acciones
        num_acciones = int(lineas[0].strip())
        if num_acciones <= 0:
            raise ValueError("El número de acciones debe ser positivo")

        # Validar que el número de líneas sea consistente con el número de acciones
        lineas_esperadas = (num_acciones * (num_acciones - 1)) // 2
        if len(lineas) - 1 != lineas_esperadas:
            raise ValueError(f"El archivo debe contener {lineas_esperadas} correlaciones para {num_acciones} acciones")

        correlaciones = {}
        acciones_vistas = set()  # Para detectar correlaciones duplicadas

        # Procesar cada línea de correlación
        for i, linea in enumerate(lineas[1:], start=1):
            partes = linea.strip().split()
            if len(partes) != 3:
                raise ValueError(f"Error en formato en línea {i+1}: debe contener ACCION1 ACCION2 correlacion")

            accion1, accion2, correlacion = partes
            if accion1 == accion2:
                raise ValueError(f"Error en línea {i+1}: una acción no puede correlacionarse consigo misma")

            # Verificar que no haya correlaciones duplicadas
            par_acciones = frozenset([accion1, accion2])
            if par_acciones in acciones_vistas:
                raise ValueError(f"Error: Correlación duplicada entre {accion1} y {accion2}")
            acciones_vistas.add(par_acciones)

            # Validar y convertir el valor de correlación
            try:
                correlacion = float(correlacion)
                if not -1 <= correlacion <= 1:
                    raise ValueError(f"Error en línea {i+1}: correlación debe estar entre -1 y 1")
            except ValueError:
                raise ValueError(f"Error en línea {i+1}: correlación debe ser un número real")

            # Almacenar correlación en ambos sentidos (matriz simétrica)
            correlaciones[(accion1, accion2)] = correlacion
            correlaciones[(accion2, accion1)] = correlacion

        return num_acciones, correlaciones

    except FileNotFoundError:
        raise FileNotFoundError(f"El archivo {archivo} no fue encontrado")
    except Exception as e:
        raise Exception(f"Error al cargar correlaciones: {str(e)}")

def cargar_rendimientos(archivo='rendimientos.txt'):
    """
    Carga y valida los rendimientos y factores de riesgo de las acciones desde un archivo.
    
    El formato esperado del archivo es:
    - Cada línea: ACCION rendimiento_anual factor_riesgo
    
    Args:
        archivo (str): Ruta al archivo de rendimientos (default: 'rendimientos.txt')
        
    Returns:
        tuple: (diccionario de rendimientos, diccionario de factores de riesgo)
        
    Raises:
        FileNotFoundError: Si el archivo no existe
        ValueError: Si el formato o los valores en el archivo son incorrectos
        Exception: Para otros errores durante la carga
    """
    try:
        with open(archivo, 'r') as file:
            lineas = file.readlines()

        # Validar que el archivo no esté vacío
        if not lineas:
            raise ValueError("El archivo de rendimientos está vacío")

        rendimientos = {}
        riesgos = {}
        acciones_vistas = set()  # Para detectar acciones duplicadas

        # Procesar cada línea
        for i, linea in enumerate(lineas):
            partes = linea.strip().split()
            if len(partes) != 3:
                raise ValueError(f"Error en formato en línea {i+1}: debe contener ACCION rendimiento_anual factor_riesgo")

            accion, rendimiento, riesgo = partes
            
            # Verificar que no haya acciones duplicadas
            if accion in acciones_vistas:
                raise ValueError(f"Error: La acción {accion} aparece más de una vez en el archivo")
            acciones_vistas.add(accion)

            # Validar y convertir el rendimiento
            try:
                rendimiento = float(rendimiento)
                if rendimiento < 0:
                    raise ValueError(f"Error en línea {i+1}: el rendimiento debe ser un valor positivo")
            except ValueError:
                raise ValueError(f"Error en línea {i+1}: el rendimiento debe ser un número real")

            # Validar y convertir el factor de riesgo
            try:
                riesgo = int(riesgo)
                if not 1 <= riesgo <= 10:
                    raise ValueError(f"Error en línea {i+1}: el factor de riesgo debe estar entre 1 y 10")
            except ValueError:
                raise ValueError(f"Error en línea {i+1}: el factor de riesgo debe ser un número entero")

            # Almacenar los valores
            rendimientos[accion] = rendimiento
            riesgos[accion] = riesgo

        return rendimientos, riesgos

    except FileNotFoundError:
        raise FileNotFoundError(f"El archivo {archivo} no fue encontrado")
    except Exception as e:
        raise Exception(f"Error al cargar rendimientos: {str(e)}")

def validar_consistencia_datos(correlaciones, rendimientos, riesgos):
    """
    Valida que exista consistencia entre los datos de correlaciones, rendimientos y riesgos.
    
    Verifica que todas las acciones que aparecen en el archivo de correlaciones
    tengan sus correspondientes rendimientos y factores de riesgo, y viceversa.
    
    Args:
        correlaciones (dict): Diccionario de correlaciones entre pares de acciones
        rendimientos (dict): Diccionario de rendimientos por acción
        riesgos (dict): Diccionario de factores de riesgo por acción
        
    Raises:
        ValueError: Si hay inconsistencias entre los conjuntos de acciones
    """
    # Extraer todos los nombres de acciones de las correlaciones
    acciones_correlaciones = set(itertools.chain(*correlaciones.keys()))
    
    # Obtener los nombres de acciones de rendimientos y riesgos
    acciones_rendimientos = set(rendimientos.keys())
    acciones_riesgos = set(riesgos.keys())

    # Verificar que todas las acciones en correlaciones tengan rendimientos
    acciones_faltantes_rendimientos = acciones_correlaciones - acciones_rendimientos
    if acciones_faltantes_rendimientos:
        raise ValueError(f"Las siguientes acciones aparecen en correlaciones pero no tienen rendimientos: {acciones_faltantes_rendimientos}")

    # Verificar que todas las acciones en correlaciones tengan factores de riesgo
    acciones_faltantes_riesgos = acciones_correlaciones - acciones_riesgos
    if acciones_faltantes_riesgos:
        raise ValueError(f"Las siguientes acciones aparecen en correlaciones pero no tienen factores de riesgo: {acciones_faltantes_riesgos}")

    # Verificar que todas las acciones con rendimientos aparezcan en correlaciones
    acciones_sin_correlacion = acciones_rendimientos - acciones_correlaciones
    if acciones_sin_correlacion:
        raise ValueError(f"Las siguientes acciones tienen rendimientos pero no aparecen en correlaciones: {acciones_sin_correlacion}")

def obtener_limite_correlacion():
    """
    Solicita al usuario el límite máximo de correlación permitido.
    
    Returns:
        float: El límite de correlación (entre -1 y 1)
    """
    while True:
        try:
            limite_correlacion = float(input("Ingrese el límite de correlación permitido (-1 a 1): "))
            if -1 <= limite_correlacion <= 1:
                return limite_correlacion
            else:
                print("El límite de correlación debe estar entre -1 y 1.")
        except ValueError:
            print("El límite de correlación debe ser un número real.")

def obtener_min_acciones(acciones_disponibles):
    """
    Solicita al usuario el número mínimo de acciones deseadas en el portafolio.
    
    Args:
        acciones_disponibles (list): Lista de acciones disponibles
        
    Returns:
        int: El número mínimo de acciones (entre 1 y el total disponible)
    """
    while True:
        try:
            min_acciones = int(input(f"Ingrese el mínimo de acciones (1 a {len(acciones_disponibles)}): "))
            if 1 <= min_acciones <= len(acciones_disponibles):
                return min_acciones
            else:
                print(f"El mínimo de acciones debe estar entre 1 y {len(acciones_disponibles)}.")
        except ValueError:
            print("El mínimo de acciones debe ser un número entero.")

def obtener_riesgo_maximo():
    """
    Solicita al usuario el riesgo promedio máximo permitido para el portafolio.
    
    Returns:
        float: El riesgo promedio máximo permitido (número no negativo)
    """
    while True:
        try:
            riesgo_maximo = float(input("Ingrese el riesgo promedio máximo permitido: "))
            if riesgo_maximo >= 0:
                return riesgo_maximo
            else:
                print("El riesgo promedio máximo permitido debe ser un número no negativo.")
        except ValueError:
            print("El riesgo promedio máximo permitido debe ser un número real.")

def buscar_portafolio_maximo_beneficio(correlaciones, rendimientos):
    """
    Busca el portafolio con máximo rendimiento promedio respetando las restricciones
    de correlación y número mínimo de acciones.
    
    Esta función implementa el siguiente algoritmo:
    1. Solicita al usuario los parámetros de búsqueda
    2. Genera todas las posibles combinaciones de acciones (desde min_acciones hasta todas)
    3. Filtra las combinaciones que cumplen con la restricción de correlación
    4. Identifica el portafolio con máximo rendimiento promedio entre los válidos
    
    Args:
        correlaciones (dict): Diccionario de correlaciones entre pares de acciones
        rendimientos (dict): Diccionario de rendimientos por acción
    """
    # Solicitar parámetros al usuario
    limite_correlacion = obtener_limite_correlacion()
    min_acciones = obtener_min_acciones(list(rendimientos.keys()))

    acciones_disponibles = list(rendimientos.keys())
    if min_acciones > len(acciones_disponibles):
        print(f"Error: No es posible crear un portafolio con {min_acciones} acciones cuando solo hay {len(acciones_disponibles)} disponibles")
        return

    # Generar todas las combinaciones posibles desde min_acciones hasta todas las acciones
    # Usamos itertools.chain para obtener una sola lista con todas las combinaciones de diferentes tamaños
    combinaciones_posibles = list(itertools.chain(*[itertools.combinations(acciones_disponibles, tamano) 
                                                  for tamano in range(min_acciones, len(acciones_disponibles) + 1)]))

    # Filtrar las combinaciones que cumplen con la restricción de correlación
    # Una combinación es válida si ningún par de acciones en ella supera el límite de correlación
    portafolios_validos = [combinacion for combinacion in combinaciones_posibles 
                          if all(correlaciones.get((accion1, accion2), 0) <= limite_correlacion 
                               for i, accion1 in enumerate(combinacion) 
                               for accion2 in combinacion[i+1:])]

    if not portafolios_validos:
        print("No se encontraron portafolios que cumplan con las restricciones dadas.")
        return

    # Encontrar el portafolio con el máximo rendimiento promedio
    mejor_portafolio = max(portafolios_validos, 
                          key=lambda portafolio: sum(rendimientos[accion] for accion in portafolio) / len(portafolio))

    # Calcular el rendimiento promedio del mejor portafolio
    rendimiento_promedio = sum(rendimientos[accion] for accion in mejor_portafolio) / len(mejor_portafolio)

    # Mostrar resultados
    print("Portafolio de máximo beneficio:", mejor_portafolio)
    print("Rendimiento promedio:", rendimiento_promedio)
    print("Cantidad de portafolios posibles:", len(portafolios_validos))

def buscar_portafolio_riesgo_controlado(correlaciones, rendimientos, riesgos):
    """
    Busca el portafolio con máximo rendimiento promedio respetando las restricciones
    de correlación, número mínimo de acciones y riesgo promedio máximo.
    
    Esta función implementa el siguiente algoritmo:
    1. Solicita al usuario los parámetros de búsqueda
    2. Genera todas las posibles combinaciones de acciones (desde min_acciones hasta todas)
    3. Filtra las combinaciones que cumplen con la restricción de correlación y riesgo
    4. Identifica el portafolio con máximo rendimiento promedio entre los válidos
    
    Args:
        correlaciones (dict): Diccionario de correlaciones entre pares de acciones
        rendimientos (dict): Diccionario de rendimientos por acción
        riesgos (dict): Diccionario de factores de riesgo por acción
    """
    # Solicitar parámetros al usuario
    limite_correlacion = obtener_limite_correlacion()
    min_acciones = obtener_min_acciones(list(rendimientos.keys()))
    riesgo_maximo = obtener_riesgo_maximo()

    acciones_disponibles = list(rendimientos.keys())
    if min_acciones > len(acciones_disponibles):
        print(f"Error: No es posible crear un portafolio con {min_acciones} acciones cuando solo hay {len(acciones_disponibles)} disponibles")
        return

    # Generar todas las combinaciones posibles desde min_acciones hasta todas las acciones
    combinaciones_posibles = list(itertools.chain(*[itertools.combinations(acciones_disponibles, tamano) 
                                                  for tamano in range(min_acciones, len(acciones_disponibles) + 1)]))

    # Filtrar las combinaciones que cumplen con ambas restricciones:
    # 1. Restricción de correlación: ningún par de acciones supera el límite de correlación
    # 2. Restricción de riesgo: el riesgo promedio no supera el máximo permitido
    portafolios_validos = [combinacion for combinacion in combinaciones_posibles 
                          if all(correlaciones.get((accion1, accion2), 0) <= limite_correlacion 
                               for i, accion1 in enumerate(combinacion) 
                               for accion2 in combinacion[i+1:]) 
                          and sum(riesgos[accion] for accion in combinacion) / len(combinacion) <= riesgo_maximo]

    if not portafolios_validos:
        print("No se encontraron portafolios que cumplan con las restricciones dadas.")
        return

    # Encontrar el portafolio con el máximo rendimiento promedio
    mejor_portafolio = max(portafolios_validos, 
                          key=lambda portafolio: sum(rendimientos[accion] for accion in portafolio) / len(portafolio))

    # Calcular el rendimiento promedio del mejor portafolio
    rendimiento_promedio = sum(rendimientos[accion] for accion in mejor_portafolio) / len(mejor_portafolio)

    # Mostrar resultados
    print("Portafolio con riesgo controlado:")
    print("Acciones:", mejor_portafolio)
    print("Rendimiento promedio:", rendimiento_promedio)
    print("Cantidad de portafolios posibles:", len(portafolios_validos))

def main():
    """
    Función principal del programa.
    
    Coordina la carga de datos, validación y presentación del menú
    de opciones al usuario.
    """
    try:
        # Cargar los datos desde los archivos
        print("Cargando datos...")
        num_acciones, correlaciones = cargar_correlaciones()
        rendimientos, riesgos = cargar_rendimientos()

        # Validar consistencia de los datos
        print("Validando datos...")
        validar_consistencia_datos(correlaciones, rendimientos, riesgos)
        print("Datos cargados y validados correctamente.")

        # Menú principal
        while True:
            print("\nMenú")
            print("1. Portafolio de máximo beneficio")
            print("2. Portafolio con riesgo controlado")
            print("3. Salir")

            opcion = input("Elija opción: ")

            if opcion == "1":
                buscar_portafolio_maximo_beneficio(correlaciones, rendimientos)
            elif opcion == "2":
                buscar_portafolio_riesgo_controlado(correlaciones, rendimientos, riesgos)
            elif opcion == "3":
                print("Hasta luego.")
                break
            else:
                print("Opción no válida")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    # Punto de entrada del programa
    main()