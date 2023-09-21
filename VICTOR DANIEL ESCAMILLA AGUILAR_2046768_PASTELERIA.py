# Inicializar variables para los precios de pasteles
precio_pastel_pequeño = 100
precio_pastel_grande = 300

# Crear una lista vacía para almacenar los pasteles seleccionados
pasteles_seleccionados = []

while True:
    # Solicitar al usuario el sabor del pastel
    sabor = input("Por favor, ingresa el sabor del pastel (chocolate, vainilla o tres leches): ")
    
    # Verificar que el sabor ingresado sea válido
    if sabor.lower() not in ["chocolate", "vainilla", "tres leches"]:
        print("Sabor no válido. Por favor, selecciona un sabor válido.")
        continue
    
    # Preguntar al usuario si desea agregar otro pastel
    agregar_otro = input("¿Deseas agregar otro pastel? (sí/no): ")
    
    # Calcular el precio del pastel y agregarlo a la lista de pasteles seleccionados
    if sabor.lower() == "chocolate":
        pasteles_seleccionados.append(precio_pastel_pequeño)
    else:
        pasteles_seleccionados.append(precio_pastel_grande)
    
    # Verificar si el usuario desea agregar otro pastel
    if agregar_otro.lower() != "sí":
        break

# Calcular el precio total de los pasteles seleccionados
precio_total = sum(pasteles_seleccionados)

# Mostrar el precio total al usuario
print(f"El precio total de los pasteles seleccionados es: {precio_total} pesos.")
