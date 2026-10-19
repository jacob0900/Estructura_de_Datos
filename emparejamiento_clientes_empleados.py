# Función para leer el archivo de empleados y cargar la info en una lista
def leer_emp(f):
    lista = []
    with open(f, 'r') as a:
        for l in a:
            d = l.strip().split(';')  # Separar por ';'
            lista.append([d[0], d[1], int(d[2])])  # [nombre, ocupación, precio]
    return lista

# Función para leer el archivo de clientes y cargar la info en una lista
def leer_cli(f):
    lista = []
    with open(f, 'r') as a:
        for l in a:
            d = l.strip().split(';')  # Separar por ';'
            lista.append([d[0], d[1], int(d[2])])  # [nombre, ocupación requerida, presupuesto]
    return lista

# Función que intenta emparejar clientes con empleados
def emp(emps, clis):
    usados_e = []  # Índices de empleados ya emparejados
    usados_c = []  # Índices de clientes ya emparejados
    res = []       # Lista final con los emparejamientos

    # Recorremos cada cliente
    for i in range(len(clis)):
        # Recorremos cada empleado
        for j in range(len(emps)):
            # Si ya fueron usados, los saltamos
            if j in usados_e or i in usados_c:
                continue
            # Si la ocupación coincide y el presupuesto alcanza...
            if clis[i][1] == emps[j][1] and clis[i][2] >= emps[j][2]:
                # Guardamos el emparejamiento
                res.append(clis[i][0] + ' - ' + emps[j][0])
                # Marcamos como ya usados
                usados_e.append(j)
                usados_c.append(i)
                break  # Pasamos al siguiente cliente
    return res

# ---- MAIN ----

# Cargar empleados desde el archivo
e = leer_emp("empleados.txt")
# Cargar clientes desde el archivo
c = leer_cli("clientes.txt")
# Realizar emparejamientos
m = emp(e, c)

# Imprimir emparejamientos
for x in m:
    print(x)
# Imprimir total de emparejamientos
print("\nTotal:", len(m))

