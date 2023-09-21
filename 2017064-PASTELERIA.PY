# Nombre de la pastelería
nombre_pasteleria = "La Atrevida"

# Inicializar la lista de pasteles
pasteles = []

# Sabores disponibles
sabores_disponibles = ["fresa", "chocolate"]

while True:
    print(f"Bienvenido a {nombre_pasteleria}")
    print("Menú:")
    print("1. Elegir pasteles")
    print("2. Seleccionar sabor de pastel")
    print("3. Comprar otro pastel")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("Pasteles disponibles:")
        for pastel in pasteles:
            print("- " + pastel)
    elif opcion == "2":
        print("Sabores disponibles:")
        for idx, sabor in enumerate(sabores_disponibles, start=1):
            print(f"{idx}. {sabor}")
        sabor_elegido = input("Seleccione el número del sabor deseado: ")
        if sabor_elegido.isdigit() and 1 <= int(sabor_elegido) <= len(sabores_disponibles):
            print(f"Ha elegido el sabor: {sabores_disponibles[int(sabor_elegido) - 1]}")
        else:
            print("Opción inválida. Por favor, seleccione un sabor válido.")
    elif opcion == "3":
        pasteles.append("Pastel")
        print("¡Ha comprado un pastel!")
    elif opcion == "4":
        print("Gracias por visitar", nombre_pasteleria)
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
