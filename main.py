from Libro import Libro
from socio import Socio
from datetime import datetime
from menu import crear_libro, crear_socio, seleccionar_operacion
def consultar_disponibilidad_libro(libro: Libro) :
  if libro.get_estado() :
    print('El libro esta disponible')
  else : 
    print('El libro no esta disponible')

def check_verificacion_adultos(socio: Socio) :
  if socio.calcularEdad() :
    print('Puedes leer este libro')
  else :
    print('no tienes la edad suficiente para leer este libro')
def main() :
  a = Libro('cuentos pepito',True,'a','los a', 1234515252,False)
  b = Libro('prohibido',True,'Adultos','Vatsyayana',100000000,True)
  juan = Socio('Juan', '42637834','ada@gmail','421421', datetime(2000, 6, 15),'lamadrid 133', datetime(2024, 6, 15), True)
  nacho = Socio('Nacho', '44858900', 'nacho@gmail', '12414252', datetime(2008, 5, 25),'lamadrid 544', datetime(2024, 6, 15), True)
  libros = [a, b]
  socios = [juan, nacho]
  print('BIENVENIDO\n''\n1 - cargar socio''\n2 - cargar libro'
  '\n3 - modificar usuario''\n4 - modificar el estado de un libro''\n5 - retirar libro')
  accion = seleccionar_operacion(5)

  match accion :
    case 1 :
        libros.append(crear_libro())
    case 2 :
        socios.append(crear_socio())
    case 3 :
      print('Ingrese el numero de documento del usuario')
      dni = input('')
      for socio in socios :
        if dni == socio.dni:
          print('Ingrese el dato que quiere modificar:''\n1 - modificar email'
                '\n2 - modificar telefono''\n3 - modificar domicilio''\n4 - modificar estado')
          operacion = seleccionar_operacion(4)
          match operacion:
            case 1 : socio.email = input("Ingrese el email nuevo")
            case 2 : socio.telefono = input("Ingrese el telefono nuevo")
            case 3 : socio.domicilio = input("Ingrese el domicilio nuevo")
            case 4 : socio.estado = input("Ingrese el nuevo estado nuevo")
    case 4 :
      print('Ingrese el codigo del libro')
      codigo = input('')
      for libro in libros :
        if codigo == libro.get_codigo() :
          libro.set_codigo(not libro.get_codigo())
        else : 
          print(f'No se encontro un libro con el codigo {codigo}')
    case 5 :
      dni = input('Ingrese su numero de dni')
      socio = None
      libro_a_retirar = ''
      for i in range(len(socios)) :
        print(socios[i].dni)
        if socios[i].dni == dni :
          socio = socios[i]           
      if socio == None :
        print('este usuario no existe')
        exit()
      print("libros:")
      for libro in libros :
        print(libro)
      nombre_libro = input('Ingrese el nombre del libro a retirar')
      for i in range(len(libros)) :
        if nombre_libro == libros[i].nombre:
          libro_a_retirar = libros[i]
      if libro_a_retirar.esParaAdultos() :
        if socio.calcularMayoriaEdad() :
          print('Puedes retirar el libro')
        else :
          print('debes ser mayor de edad para retirar este libro')
      else :
        print('Puedes retirar el libro')

if __name__ == '__main__' :
  main()
