from lector import leer_csv
from funciones import * 
from menu import mostrar_menu

alquiler = leer_csv("alquiler.csv")
bicicletas = leer_csv("bicicletas.csv")
clientes = leer_csv("clientes.csv")
total_ingresos = leer_csv("total_ingresos.csv")

while True:
    opcion = mostrar_menu()

    if opcion == "1":
        ver_bicicletas(bicicletas)

    elif opcion == "2":
        Agregar_cliente(clientes)

    elif opcion == "3":
            Calcular_total(bicicletas,alquiler)

    elif opcion == "4":
        ver_clientes_alquilado(clientes,alquiler)

    
    elif opcion == "5":
        print("Saliendo...")
        break

    else:
        print("Opción inválida")
