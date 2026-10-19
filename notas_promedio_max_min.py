


notas = []  
contador = 1  

while len(notas) < 5:  
    try:
        
        entrada = input(f"Ingresa la nota {contador} (0-10): ")
        nota = float(entrada)
        
        if 0 <= nota <= 10:
            notas.append(nota)
            contador += 1
        else:
            print("¡La nota debe estar entre 0 y 10!")
            
    except ValueError:  # Si no se puede convertir a número
        print("¡Error! Debes ingresar un número\n")



print("Tus notas:", ", ".join(map(str, notas)))

# Calcular estadísticas
media = sum(notas) / 5
maxima = max(notas)
minima = min(notas)

# Mostrar resultados con formato
print(f"\nNota media: {media:.2f}")  # :.2f para mostrar 2 decimales
print(f"Nota más alta: {maxima}")
print(f"Nota más baja: {minima}")