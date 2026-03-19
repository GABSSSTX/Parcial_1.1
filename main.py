from lector import leer_csv
from funciones import * 
from menu import mostrar_menu

productos = leer_csv("productos.csv")
pedidos = leer_csv("pedidos.csv")
clientes = leer_csv("clientes.csv")
ventas = leer_csv("ventas.csv")

while True:
    opcion = mostrar_menu()

    if opcion == "1":
        bicicletas_ordenadas(productos,pedidos)

    elif opcion == "2":
        Agregar_cliente(productos, pedidos, vendedores)

    elif opcion == "3":
            Calcular_total(clientes, pedidos, productos)

    elif opcion == "4":
        ver_clienetes_alquilado(productos)

    
    elif opcion == "5":
        print("Saliendo...")
        break

    else:
        print("Opción inválida")
