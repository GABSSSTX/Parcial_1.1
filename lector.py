def leer_csv(nombre_archivo):
    datos = []
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
       
        linea_cabecera = archivo.readline().strip()
        encabezado = linea_cabecera.split(",")
        
        
        for i in range(len(encabezado)):
            encabezado[i] = encabezado[i].strip()

        for linea in archivo:
            valores = linea.strip().split(",")
            if len(valores) == len(encabezado):
                fila = {}
                for i in range(len(encabezado)):
                    fila[encabezado[i]] = valores[i].strip() # También limpiamos el valor
                datos.append(fila)
    return datos

