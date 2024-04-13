def interactuar_menu() :
  
  print('BIENVENIDO\n')
  print('1 - cargar socio')
  print('2 - cargar libro')
  print('3 - modificar usuario')
  print('4 - modificar el estado de un libro')
  print('5 - retirar libro')
  try :
    operacion = int(input("Ingrese el numero de operacion que desea realizar: "))
    while operacion < 1 or operacion > 5 :
      print('\nSolo puedes ingresar numeros validos')
      operacion = int(input("Ingrese el numero de operacion que desea realizar: "))
    return operacion
  except ValueError :
    print('debes ingresar un numero valido')

def menu_modificar_usuario() :
  
  print('ingrese el dato que quiere modificar')
  print('1 - modificar email')
  print('2 - modificar telefono')
  print('3 - modificar domicilio')
  print('4 - modificar estado')
  try :
    valor = int(input('Ingrese un numero: '))
    while valor < 1 or valor > 4 :
      print('\nSolo puedes ingresar numeros validos')
      valor = int(input("Ingrese el numero de operacion que desea realizar: "))
    return valor 
  except ValueError :
    print('debes ingresar un numero valido')