def ver_bicicletas(bicicletas):
    bicicletas = []
    with open("bicicletas.csv", "r") as f:
        next(f) 
        for linea in f:
            datos = linea.strip().split(",")
            datos[2] = float(datos[2]) 
            datos[3] = int(datos[3])   
            bicicletas.append(datos)
    
    ordenadas = ordenar_lista(bicicletas, 2, ascendente=True)
    
    print("\nmodello / precio/ disponible")
    for b in ordenadas:
        print(f"{b[1]} | ${b[2]} | {b[3]}")


def Agregar_cliente ():
    nombre = input("Nombre: ")
    email = input("Email: ")
    
    max_id = 0
    with open("clientes.csv", "r") as f:
        next(f)
        for linea in f:
            datos = linea.strip().split(",")
            current_id = int(datos[0])
            if current_id > max_id:
                max_id = current_id
    
    nuevo_id = max_id + 1
    nueva_linea = f"{nuevo_id},{nombre},{email}\n"
    
    with open("clientes.csv", "a") as f:
        f.write(nueva_linea)
    print("Cliente guardado.")



def Calcular_total(bicicletas,alquiler):
    precios = []
    with open("bicicletas.csv", "r") as f:
            next(f)
            for linea in f:
                precios.append(linea.strip().split(","))

    
    totales = [] 
    with open("alquiler.csv", "r") as f:
        next(f)
        for linea in f:
            id_a, id_b_alq, id_cli, horas = linea.strip().split(",")
            horas = int(horas)
            
            
            for b in precios:
                if b[0] == id_b_alq:
                    precio = float(b[2])
                    modelo = b[1]
                    subtotal = horas * precio
                    
                    
                    encontrado = False
                    for t in totales:
                        if t[0] == id_b_alq:
                            t[2] += subtotal
                            encontrado = True
                    if not encontrado:
                        totales.append([id_b_alq, modelo, subtotal])

   
    ranking = ordenar_lista(totales, 2, ascendente=False)
    
    
    with open("total_ingresos.csv", "w") as f:
        f.write("bicicleta_id,modelo,total\n")
        for r in ranking:
            f.write(f"{r[0]},{r[1]},{r[2]}\n")

def ver_clientes_alquilado(clientes,alquiler):
    clientes_que_alquilaron = []
    
    with open("alquiler.csv", "r") as f:
        lineas = f.readlines()
        for i in range(1, len(lineas)):
            id_cli = lineas[i].strip().split(",")[2]
            if id_cli not in clientes_que_alquilaron:
                clientes_que_alquilaron.append(id_cli)
    
    
    lista_final = []
    with open("clientes.csv", "r") as f:
        lineas = f.readlines()
        for i in range(1, len(lineas)):
            datos = lineas[i].strip().split(",")
            if datos[0] in clientes_que_alquilaron:
                lista_final.append(datos)
    
    
    ordenados = ordenar_lista(lista_final, 1, True)
    
    print("\n--- CLIENTES CON ALQUILERES (A-Z) ---")
    for c in ordenados:
        print(f"ID: {c[0]} | Nombre: {c[1]:<15} | Email: {c[2]}")



