# Ejercicio Comisión por Ventas - Felipe Cogorno

import json

def calcular_comision(ventas):
    if ventas >= 0 and ventas <= 4:
        comision = 0
    elif ventas >= 5 and ventas <= 9:
        comision = 120000
    elif ventas >= 10:
        comision = 120000 + ((ventas - 9) * 40000)
    return comision

    # si la cantidad de ventas realizadas en el mes estan entre 0 y 4 entonces la
    # comision va a ser de 0, si esta entre 5 y 9 de 120.000, y si es mayor o igual
    # a 10, por cada venta que pa

def cargar_constantes():
    constantes = {}
    with open("constantes.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo: # recorre cada linea del .txt
            nombre, valores = linea.strip().split("=") # separa el nombre de la constante de sus valores
            constantes[nombre] = valores.split(",") # separa los valores separados por coma y los convierte en una lista
    return constantes


def alta_vendedor(vendedores, meses, respuesta):
    try:
        legajo = int(input("Ingrese un legajo (-1 para cancelar): "))
        if legajo == -1: return vendedores

        while legajo < 1:
            legajo = int(input("Legajo inválido. Ingrese nuevamente: "))
            if legajo == -1: return vendedores

        legajo_existe = False 

        for vendedor in vendedores:
            if vendedor["legajo"] == legajo:
                legajo_existe = True

        while legajo_existe == True:
            print("Ese legajo ya existe.")
            legajo = int(input("Ingrese otro legajo (-1 para cancelar): "))

            if legajo == -1: return vendedores

            while legajo < 1:
                legajo = int(input("Legajo inválido. Ingrese nuevamente: "))
                if legajo == -1: return vendedores

            legajo_existe = False
            for vendedor in vendedores:
                if vendedor["legajo"] == legajo:
                    legajo_existe = True

        # en caso de que se repita un legajo, se busca con un for entre
        # los legajos guardados en la lista vendedores. si se repite un legajo
        # entonces la variable legajo_existe se convierte en True. despues de 
        # eso, se hace un bucle while (que se repite hasta que legajo_existe sea
        # False) para que se ingrese de nuevo un legajo correctamente

        sueldo_basico = float(input("Ingrese sueldo básico: "))
        while sueldo_basico <= 0:
            sueldo_basico = float(input("Sueldo inválido. Ingrese nuevamente: "))

        registros_ventas = [] # esta lista va a contener diccionarios de las ventas de cada mes
        recibio_comision = False # guarda si el vendedor recibio alguna comision durante los meses que cargo, como todavia no cargo empieza en falso

        otro_mes = "si" # esto para que empiece el bucle y despues vaya preguntando si quiere ingresar otro mes
        while otro_mes == "si":
            mes = input("Ingrese el mes: ").strip().lower()
            while mes not in meses:
                mes = input("Mes inválido. Ingrese nuevamente: ").strip().lower()

            mes_existe = False

            for registro in registros_ventas:
                if registro["mes"] == mes:
                    mes_existe = True

            while mes_existe == True:
                print("Ya existen ventas cargadas para ese mes.")
                mes = input("Ingrese otro mes: ").strip().lower()       
                while mes not in meses:
                    mes = input("Mes inválido. Ingrese nuevamente: ").strip().lower()

                mes_existe = False
                for registro in registros_ventas:
                    if registro["mes"] == mes:
                        mes_existe = True

        # se pregunta si se desea cargar otro mes y mientras la respuesta sea
        # "si" se repite el proceso de carga. se solicita un mes y se verifica
        # que sea valido y que no se encuentre registrado anteriormente en la
        # lista registros_ventas. para comprobarlo se utiliza un for que recorre
        # los registros ya cargados y compara el mes ingresado con los existentes.
        # si el mes ya existe, la variable mes_existe pasa a ser True y se ejecuta
        # un while que solicita ingresar otro mes. cada vez que se ingresa uno
        # nuevo, se vuelve a comprobar que sea valido y que no este repetido.
        # cuando se ingresa un mes que todavia no fue registrado, se puede
        # continuar con la carga de la cantidad de ventas

            ventas = int(input("Ingrese cantidad de ventas: "))
            while ventas < 0:
                ventas = int(input("Cantidad inválida. Ingrese nuevamente: "))

            comision = calcular_comision(ventas)
            sueldo_total = sueldo_basico + comision

            print("Mes:", mes)
            print("Cantidad de ventas:", ventas)
            print("Comisión:", comision)
            print("Sueldo total:", sueldo_total)

            if comision > 0:
                recibio_comision = True
            # si la comision es mayor a 0 entonces la variable recibio_comision se vuelve True, sino pasa de largo

            registro = {
                "mes": mes,
                "cantidad": ventas,
                "comision": comision
            }

            # mete los datos ingresados del mes en un diccionario y los agrega en la lista registros_ventas

            registros_ventas.append(registro)

            otro_mes = input("¿Desea cargar otro mes? (si/no): ").strip().lower()
            while otro_mes not in respuesta: # aca valida que lo que ingrese solo pueda ser un si o un no
                otro_mes = input("Ingrese si o no: ").strip().lower()

        vendedor = {
            "legajo": legajo,
            "sueldo_basico": sueldo_basico,
            "ventas": registros_ventas
        }

        # mete los datos de cada vendedor en un diccionario y los agrega en la lista vendedores

        vendedores.append(vendedor)

        print("Vendedor registrado correctamente.")

    except ValueError: # captura el error que se produce cuando se ingresa un dato que no se puede convertir al tipo de dato solicitado
        print("Error: ingresó un dato inválido. Intente nuevamente.")

    return vendedores

def baja_vendedor(vendedores):
    try:
        legajo = int(input("Ingrese el legajo del vendedor que desea eliminar (-1 para cancelar): "))

        if legajo == -1:
            return vendedores # si ingresa -1, se cancela la carga del vendedor y devuelve la lista sin modificar

        while legajo < 1:
            legajo = int(input("Legajo inválido. Ingrese nuevamente: "))
            if legajo == -1:
                return vendedores

        vendedor_encontrado = False

        for vendedor in vendedores:
            if vendedor["legajo"] == legajo:
                vendedores.remove(vendedor)
                vendedor_encontrado = True
                print("Vendedor eliminado correctamente.")
                break

        if vendedor_encontrado == False:
            print("No existe un vendedor con ese legajo.")

    # la funcion se encarga de borrar un legajo especifico. primero se
    # tiene que ingresar por consola un legajo valido. despues se recorre
    # con un for cada vendedor o elemento de la lista de vendedores y
    # compara el legajo del vendedor con el legajo ingresado. si encuentra
    # ese legajo entonces lo borra de la lista de vendedores, cambia el valor
    # de la variable vendedor_encontrado a True y hace un break para que deje
    # de comparar o buscar los legajos, porque ya se encontro

    except ValueError:
        print("Error: ingresó un dato inválido. Intente nuevamente.")

    return vendedores

# aca decidi hacer la modificacion segun el sueldo basico, siento que si lo 
# hacia con otra caracteristica o con todas iba a ser innecesario y mucho 
# mas complicado o largo. pero no queria no poner nada de modificar
def modificar_vendedor(vendedores):
    try:
        legajo = int(input("Ingrese el legajo del vendedor que desea modificar (-1 para cancelar): "))

        if legajo == -1:
            return vendedores

        while legajo < 1:
            legajo = int(input("Legajo inválido. Ingrese nuevamente: "))
            if legajo == -1:
                return vendedores

        vendedor_encontrado = False

        for vendedor in vendedores:
            if vendedor["legajo"] == legajo:
                vendedor_encontrado = True

                sueldo_basico = float(input("Ingrese el nuevo sueldo básico: "))
                while sueldo_basico <= 0:
                    sueldo_basico = float(input("Sueldo inválido. Ingrese nuevamente: "))

                vendedor["sueldo_basico"] = sueldo_basico

                print("Vendedor modificado correctamente.")
                break

        if vendedor_encontrado == False:
            print("No existe un vendedor con ese legajo.")

    # como dije, esta funcion se encarga de modificar el sueldo basico del vendedor.
    # primero se ingresa por consola un legajo valido. despues con un for se recorre
    # vendedor o elemento por elemento de la lista de vendedores y se compara el legajo
    # ingresado por consola con el legajo del vendedor. si la comparacion es verdadera
    # entonces se ingresa por consola otro sueldo_basico valido, despues se modifica
    # el sueldo_basico antiguo por el nuevo recien ingresado. al final se usa un break 
    # para que pare de recorrer cada legajo de la lista
    
    except ValueError:
        print("Error: ingresó un dato inválido. Intente nuevamente.")

    return vendedores

def alta_venta(vendedores, meses):
    try:
        legajo = int(input("Ingrese el legajo del vendedor (-1 para cancelar): "))

        if legajo == -1:
            return vendedores

        while legajo < 1:
            legajo = int(input("Legajo inválido. Ingrese nuevamente: "))
            if legajo == -1:
                return vendedores

        vendedor_encontrado = False

        for vendedor in vendedores:
            if vendedor["legajo"] == legajo:
                vendedor_encontrado = True

                mes = input("Ingrese el mes: ").strip().lower() # elimina espacios del principio y el final y lo convierte en minusculas
                while mes not in meses:
                    mes = input("Mes inválido. Ingrese nuevamente: ").strip().lower()

                mes_existe = False

                for registro in vendedor["ventas"]:
                    if registro["mes"] == mes:
                        mes_existe = True

                while mes_existe == True:
                    print("Ya existen ventas cargadas para ese mes.")
                    mes = input("Ingrese otro mes: ").strip().lower()

                    while mes not in meses:
                        mes = input("Mes inválido. Ingrese nuevamente: ").strip().lower()

                    mes_existe = False
                    for registro in vendedor["ventas"]:
                        if registro["mes"] == mes:
                            mes_existe = True

                ventas = int(input("Ingrese cantidad de ventas: "))
                while ventas < 0:
                    ventas = int(input("Cantidad inválida. Ingrese nuevamente: "))

                comision = calcular_comision(ventas)

                registro = {
                    "mes": mes,
                    "cantidad": ventas,
                    "comision": comision
                }

                vendedor["ventas"].append(registro)

                print("Venta registrada correctamente.")
                break

        if vendedor_encontrado == False:
            print("No existe un vendedor con ese legajo.")

    # la funcion carga nuevas ventas para un vendedor. primero solicita un legajo 
    # y busca si existe dentro de la lista de vendedores. si lo encuentra, solicita 
    # un mes valido y verifica que no haya ventas cargadas anteriormente para ese
    # mismo mes. despues solicita la cantidad de ventas, calcula la comision
    # correspondiente y guarda los datos en un diccionario. finalmente agrega ese 
    # diccionario a la lista de ventas del vendedor y utiliza un break para dejar
    # de recorrer la lista de vendedores.

    except ValueError:
        print("Error: ingresó un dato inválido. Intente nuevamente.")

    return vendedores

def baja_venta(vendedores, meses):
    try:
        legajo = int(input("Ingrese el legajo del vendedor que desea eliminar (-1 para cancelar): "))

        if legajo == -1:
            return vendedores

        while legajo < 1:
            legajo = int(input("Legajo inválido. Ingrese nuevamente: "))
            if legajo == -1:
                return vendedores

        vendedor_encontrado = False

        for vendedor in vendedores:
            if vendedor["legajo"] == legajo:
                vendedor_encontrado = True

                mes = input("Ingrese el mes de la venta que desea eliminar: ").strip().lower()
                while mes not in meses:
                    mes = input("Mes inválido. Ingrese nuevamente: ").strip().lower()

                venta_encontrada = False

                for registro in vendedor["ventas"]:
                    if registro["mes"] == mes:
                        vendedor["ventas"].remove(registro)
                        venta_encontrada = True
                        print("Venta eliminada correctamente.")
                        break

                if venta_encontrada == False:
                    print("No existen ventas cargadas para ese mes.")

                break

        if vendedor_encontrado == False:
            print("No existe un vendedor con ese legajo.")

        # primero se busca al vendedor mediante su legajo. si existe, se solicita
        # el mes de la venta que se desea eliminar y se recorren sus registros.
        # si se encuentra el mes, se elimina el diccionario correspondiente de la
        # lista de ventas. los break estan para que se deje de recorrer las listas
        # una vez que se encontro al vendedor y se elimino la venta.

    except ValueError:
        print("Error: ingresó un dato inválido. Intente nuevamente.")

    return vendedores

# en este caso, decidi modificar segun la cantidad de ventas
def modificar_venta(vendedores, meses):
    try:
        legajo = int(input("Ingrese el legajo del vendedor que desea modificar (-1 para cancelar): "))

        if legajo == -1:
            return vendedores

        while legajo < 1:
            legajo = int(input("Legajo inválido. Ingrese nuevamente: "))
            if legajo == -1:
                return vendedores

        vendedor_encontrado = False

        for vendedor in vendedores:
            if vendedor["legajo"] == legajo:
                vendedor_encontrado = True

                mes = input("Ingrese el mes de la venta que desea modificar: ").strip().lower()
                while mes not in meses:
                    mes = input("Mes inválido. Ingrese nuevamente: ").strip().lower()

                venta_encontrada = False

                for registro in vendedor["ventas"]:
                    if registro["mes"] == mes:
                        venta_encontrada = True

                        ventas = int(input("Ingrese la nueva cantidad de ventas: "))
                        while ventas < 0:
                            ventas = int(input("Cantidad inválida. Ingrese nuevamente: "))

                        registro["cantidad"] = ventas
                        registro["comision"] = calcular_comision(ventas)

                        print("Venta modificada correctamente.")
                        break

                if venta_encontrada == False:
                    print("No existen ventas cargadas para ese mes.")

                break

        if vendedor_encontrado == False:
            print("No existe un vendedor con ese legajo.")

    # primero se busca al vendedor mediante su legajo y despues se busca el
    # registro correspondiente al mes ingresado. si se encuentra, se solicita
    # una nueva cantidad de ventas y se actualizan tanto la cantidad como la
    # comision. 

    except ValueError:
        print("Error: ingresó un dato inválido. Intente nuevamente.")

    return vendedores

def consultar_vendedores_ventas(vendedores, meses, respuesta):
    try:
        if len(vendedores) == 0:
            print("No hay vendedores registrados.")
        else:
            legajo = int(input("Ingrese el legajo del vendedor que desea consultar (-1 para cancelar): "))

            if legajo == -1:
                return

            while legajo < 1:
                legajo = int(input("Legajo inválido. Ingrese nuevamente: "))
                if legajo == -1:
                    return

            vendedor_encontrado = False

            for vendedor in vendedores:
                if vendedor["legajo"] == legajo:
                    vendedor_encontrado = True

                    print("--------------------")
                    print("Legajo:", vendedor["legajo"])
                    print("Sueldo básico:", vendedor["sueldo_basico"])
                    print("--------------------")

                    consultar = input("¿Desea consultar las ventas de un mes específico? (si/no): ").strip().lower()
                    while consultar not in respuesta:
                        consultar = input("Ingrese si o no: ").strip().lower()

                    if consultar == "si":
                        mes = input("Ingrese el mes que desea consultar: ").strip().lower()
                        while mes not in meses:
                            mes = input("Mes inválido. Ingrese nuevamente: ").strip().lower()

                        venta_encontrada = False

                        for registro in vendedor["ventas"]:
                            if registro["mes"] == mes:
                                venta_encontrada = True

                                print("--------------------")
                                print("Mes:", registro["mes"])
                                print("Cantidad de ventas:", registro["cantidad"])
                                print("Comisión:", registro["comision"])
                                print("--------------------")
                                break

                        if venta_encontrada == False:
                            print("No hay ventas registradas para ese mes.")

                    break # para cortar el for

            if vendedor_encontrado == False:
                print("No existe un vendedor con ese legajo.")

    # primero se verifica si hay vendedores registrados y despues se solicita
    # un legajo valido para buscar al vendedor. si se encuentra, se muestran
    # sus datos y se pregunta si desea consultar las ventas de un mes especifico.
    # si responde que si, se solicita un mes valido y se recorren sus registros
    # de ventas para buscarlo. si se encuentra, se muestran la cantidad de ventas
    # y la comision correspondiente. se utilizan las variables vendedor_encontrado
    # y venta_encontrada para comprobar si existen los registros buscados.

    except ValueError:
        print("Error: ingresó un dato inválido. Intente nuevamente.")

def informar_estadisticas(vendedores):
    if len(vendedores) > 0:
        total_ventas = 0
        vendedores_sin_comision = 0

        for vendedor in vendedores:
            recibio_comision = False

            for registro in vendedor["ventas"]:
                total_ventas += registro["cantidad"]

                if registro["comision"] > 0:
                    recibio_comision = True

            if recibio_comision == False:
                vendedores_sin_comision += 1

        promedio = total_ventas / len(vendedores)

        print("\n========== ESTADISTICAS ==========")
        print("Promedio de ventas realizadas por vendedor:", promedio)

        maximo_ventas = -1
        meses_maximos = []

        for vendedor in vendedores:
            for registro in vendedor["ventas"]:
                if registro["cantidad"] > maximo_ventas:
                    maximo_ventas = registro["cantidad"]
                    meses_maximos = [registro["mes"]]

                elif registro["cantidad"] == maximo_ventas:
                    if registro["mes"] not in meses_maximos:
                        meses_maximos.append(registro["mes"])

        if len(meses_maximos) > 0:
            print("Maxima cantidad de ventas:", maximo_ventas)
            print("Mes/es en los que se realizaron:", meses_maximos)
        else:
            print("No se registraron ventas.")

        print("Cantidad de vendedores sin comision:", vendedores_sin_comision)
        print("==================================")

    else:
        print("No se ingresaron vendedores.")


    # primero se recorren los vendedores y sus registros de ventas para sumar
    # todas las cantidades y comprobar si cada vendedor recibio alguna comision.
    # despues se calcula el promedio dividiendo el total de ventas por la cantidad
    # de vendedores. finalmente se busca la mayor cantidad de ventas registrada
    # y se guardan los meses correspondientes. tambien se cuenta la cantidad de
    # vendedores que nunca recibieron una comision.

def reporte_vendedores(vendedores):
    if len(vendedores) == 0:
        print("No hay vendedores registrados.")
    else:
        reporte = []

        for vendedor in vendedores:
            sueldo_total = vendedor["sueldo_basico"]

            for registro in vendedor["ventas"]:
                sueldo_total += registro["comision"]

            reporte.append([vendedor["legajo"], sueldo_total])

        reporte = sorted(reporte, key=lambda vendedor: vendedor[0])

        print("\n========== REPORTE DE VENDEDORES ==========")
        print("Vendedor;sueldototal")

        for vendedor in reporte:
            print(str(vendedor[0]) + ";" + str(vendedor[1]))

        print("===========================================")

        exportar = input("¿Desea exportar el reporte a CSV? (si/no): ").strip().lower()

        while exportar not in ["si", "no"]:
            exportar = input("Ingrese si o no: ").strip().lower()

        if exportar == "si":
            with open("reporte_vendedores.csv", "w", encoding="utf-8") as archivo:
                archivo.write("Vendedor;sueldototal\n")

                for vendedor in reporte:
                    archivo.write(str(vendedor[0]) + ";" + str(vendedor[1]) + "\n")

            print("Reporte exportado correctamente.")

    # primero se verifica si hay vendedores registrados. si los hay, se recorre
    # la lista de vendedores y se calcula el sueldo total de cada uno, sumando
    # el sueldo basico y todas las comisiones obtenidas por sus ventas. despues
    # se guarda el legajo y el sueldo total en la lista reporte, que se ordena 
    # por legajo utilizando una funcion lambda. finalmente, se muestra el reporte
    # por pantalla y se le pregunta al usuario si desea exportarlo a un archivo 
    # csv. si la respuesta es "si", se crea el archivo y se escriben los nombres de 
    # las columnas y los datos de cada vendedor, separados por punto y coma.


def guardar_datos(vendedores):
    with open("vendedores.json", "w", encoding="utf-8") as archivo:
        json.dump(vendedores, archivo, indent=4, ensure_ascii=False)

    # aca se abre el archivo vendedores.json en modo escritura para guardar
    # la lista de vendedores. json.dump convierte los datos de python
    # a formato json y los escribe en el archivo. el indent=4 organiza
    # la informacion para que sea mas facil de leer y ensure_ascii=False
    # permite conservar correctamente las tildes y la letra ñ.

    print("Datos guardados correctamente.")

# aca decidi hacer una funcion que pueda recuperar los datos ingresados
def cargar_datos():
    try:
        with open("vendedores.json", "r", encoding="utf-8") as archivo:
            vendedores = json.load(archivo)

    except FileNotFoundError:
        vendedores = []

    # se abre el archivo vendedores.json en modo lectura para recuperar
    # los datos guardados anteriormente. json.load convierte la informacion
    # del archivo json nuevamente a una lista de python. si el archivo no
    # existe, se produce un FileNotFoundError y se crea una lista vacia
    # para comenzar a cargar vendedores desde cero.

    return vendedores

def menu():
    constantes = cargar_constantes()

    meses = constantes["MESES"]
    respuesta = constantes["RESPUESTA"]

    vendedores = cargar_datos()

    opcion = 0
    while opcion != 11: # si la opcion ingresada no es salir
        print("\n========== MENU PRINCIPAL ==========")
        print("1. Alta de vendedor")
        print("2. Baja de vendedor")
        print("3. Modificar vendedor")
        print("4. Alta de venta")
        print("5. Baja de venta")
        print("6. Modificar venta")
        print("7. Consultar vendedores y ventas")
        print("8. Informar estadísticas")
        print("9. Guardar datos")
        print("10. Reporte de vendedores")
        print("11. Salir")
        print("====================================")

        try:
            opcion = int(input("Seleccione una opcion: "))

            if opcion == 1:
                vendedores = alta_vendedor(vendedores, meses, respuesta)

            elif opcion == 2:
                vendedores = baja_vendedor(vendedores)

            elif opcion == 3:
                vendedores = modificar_vendedor(vendedores)

            elif opcion == 4:
                vendedores = alta_venta(vendedores, meses)

            elif opcion == 5:
                vendedores = baja_venta(vendedores, meses)

            elif opcion == 6:
                vendedores = modificar_venta(vendedores, meses)

            elif opcion == 7:
                consultar_vendedores_ventas(vendedores, meses, respuesta)

            elif opcion == 8:
                informar_estadisticas(vendedores)

            elif opcion == 9:
                guardar_datos(vendedores)

            elif opcion == 10:
                reporte_vendedores(vendedores)

            elif opcion == 11:
                print("Programa finalizado.")

            else:
                print("Opcion invalida. Intente nuevamente.")

        except ValueError:
            print("Error: debe ingresar un numero.")



menu()