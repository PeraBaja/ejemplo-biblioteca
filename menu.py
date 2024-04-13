from Libro import Libro
from socio import Socio
def seleccionar_operacion(cantOperaciones: int):
    operacion = 0
    while not (cantOperaciones > operacion > 0):
        try:
            operacion = int(input('Seleccione una de las operaciones listadas: '))
            if not (cantOperaciones > operacion > 0):
                raise ValueError
        except ValueError:
            print("Error. Seleccione un número de operación de los listados")  
    return operacion

def crear_libro():
    claves = ['nombre','genero','autor', 'codigo','es para adultos']
    valores = []
    print('Ingrese los datos del libro a cargar')
    for clave in claves :
      if clave == 'es para adultos' :
        respuesta = input('este libro es para mayores de 18? (si/no): ')
        if respuesta.lower() == 'si' :
          valores.append(True)
        else : 
          valores.append(False)
      else :
        valores.append(input(f'{clave}: '))
    print(Libro(valores[0], True, valores[1], valores[2], valores[3], valores[4]))
    return Libro(valores[0], True, valores[1], valores[2], valores[3], valores[4])

def crear_socio():
    claves = ['nombre','dni','email', 'telefono','fecha de nacimiento', 'domicilio', 'fecha de inscripcion']
    valores = []
    print('Ingrese los datos del socio a cargar')
    for clave in claves :
      valores.append(input(f'{clave}: '))
    return Socio(valores[0], valores[1], valores[2], valores[3], valores[4], valores[5], valores[6], True)