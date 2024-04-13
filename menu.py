def seleccionar_operacion(cantOperaciones: int):
    operacion = 0
    while not (cantOperaciones > operacion > 0):
        try:
            operacion = int(input('Seleccione una de las operaciones listadas'))
        except ValueError:
            print("Error. Seleccione un número de operación de los listados")  
    return operacion