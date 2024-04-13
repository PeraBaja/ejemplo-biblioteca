def seleccionar_operacion(cantOperaciones: int):
    operacion = int(input('Seleccione una de las operaciones listadas'))
    while not (cantOperaciones > operacion > 0):
        print("Error. Seleccione un número de operación de los listados")
        operacion = int(input('Seleccione una de las operaciones listadas'))
    return operacion