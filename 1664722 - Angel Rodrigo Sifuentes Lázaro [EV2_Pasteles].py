class Pastel:
    def __init__(self, sabor, precio, tamaño):
        self.sabor = sabor
        self.precio = precio
        self.tamaño = tamaño

    def imprimir_precio(self):
        print(f"El pastel de {self.sabor} de tamaño {self.tamaño} cuesta ${self.precio}")

def mostrar_menu():
    print("----------R O D R I  C A K E S----------")
    print("----------------------------------------")
    print("Opciones de pasteles:")
    print("1. Tortuga")
    print("2. Alemán")
    print("3. Cheesecake")
    print("4. Tiramisú")
    print("5. Imposible")
    print("----------------------------------------")

def main():
    while True:
        mostrar_menu()
        
        opcion_pastel = input("Elija el número del pastel que desea (1-5): ")

        if opcion_pastel in ["1", "2", "3", "4", "5"]:
            sabor_pastel = ""
            if opcion_pastel == "1":
                sabor_pastel = "Tortuga"
            elif opcion_pastel == "2":
                sabor_pastel = "Alemán"
            elif opcion_pastel == "3":
                sabor_pastel = "Cheesecake"
            elif opcion_pastel == "4":
                sabor_pastel = "Tiramisú"
            elif opcion_pastel == "5":
                sabor_pastel = "Imposible"

            size = input("Introduzca (en minúsculas) el tamaño del pastel (grande/mediano/chico): ")

            pastel = Pastel(sabor_pastel, "300", "grande")
            if size == "mediano":
                pastel.precio = "160"
                pastel.tamaño = "mediano"
            elif size == "chico":
                pastel.precio = "80"
                pastel.tamaño = "chico"

            pastel.imprimir_precio()

            opcion = input("¿Desea imprimir su ticket? (si/no): ")
            if opcion == "si":
                print("----------------------------------------")
                print("----------R O D R I  C A K E S----------")
                print("----------------------------------------")
                print(f"PASTEL SABOR {pastel.sabor} DE TAMAÑO {pastel.tamaño}")
                print("----------------------------------------")
                print(f"TOTAL: ${pastel.precio}")
                print("----MUCHAS GRACIAS POR SU PREFERENCIA---")
                print("----------------------------------------")
                print("-----------VUELVA PRONTO!--------------")
            elif opcion == "no":
                print("¡Muchas gracias, vuelva pronto!")

        else:
            print("Opción no válida. Por favor, elija un número del 1 al 5.")

        continuar = input("¿Desea hacer otro pedido? (si/no): ")
        if continuar.lower() != "si":
            print("¡Gracias por visitarnos! Hasta luego.")

if __name__ == "__main__":
    main()
