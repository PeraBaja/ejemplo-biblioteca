def seleccionar_operacion(cantOperaciones: int) : # Antes: Interactuar_menu()
    operacion = int(input('Seleccione una de las operaciones listadas'))
    while operacion < 1 or operacion > cantOperaciones or ValueError:
        print("Error. Seleccione un número de operación de los listados")
        operacion = int(input('Seleccione una de las operaciones listadas'))