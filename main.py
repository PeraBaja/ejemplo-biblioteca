from Libro import Libro
from socio import Socio
from menu import interactuar_menu, menu_modificar_usuario
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
  juan = Socio('Juan', '42637834','ada@gmail','421421','15/6/2000','lamadrid 133','15/6/2024', True )
  nacho = Socio('Nacho', '44858900', 'nacho@gmail', '12414252', '25/5/2008','lamadrid 544', '15/6/2024', True)
  libros = [a, b]
  socios = [juan, nacho]
  accion = interactuar_menu()

  match accion :
    case 1 :
      claves = ['nombre','genero','autor', 'codigo','es para adultos']
      valores = []
      print('Ingrese los datos del libro a cargar')
      for clave in claves :
        if clave == 'es para adultos' :
          print('este libro es para mayores de 18? (si/no)')
          adultos = input()
          if adultos.lower() == 'si' :
            valores.append(True)
          else : 
            valores.append(False)
        else :
          valores.append(input(f'{clave}'))
      libros.append(Libro(valores[0], True, valores[1], valores[2], valores[3], valores[4]))
    case 2 :
      claves = ['nombre','dni','email', 'telefono','fecha de nacimiento', 'domicilio', 'fecha de inscripcion']
      valores = []
      print('Ingrese los datos del libro a cargar')
      for clave in claves :
        valores.append(input(f'{clave}: '))
      socios.append(Socio(valores[0], valores[1], valores[2], valores[3], valores[4], valores[5], valores[6], True))
    case 3 :
      print('Ingrese el numero de documento del usuario')
      dni = input('')
      for socio in socios :
        if dni == socio.getDni():
          numero = menu_modificar_usuario()
          match numero :
            case 1 : socio.setEmail(input("Ingrese el email nuevo"))
            case 2 : socio.setTelefono(input("Ingrese el telefono nuevo"))
            case 3 : socio.setDomicilio(input("Ingrese el domicilio nuevo"))
            case 4 : socio.setEstado(not socio.getEstado())
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
        print(socios[i].getDni())
        if socios[i].getDni() == dni :
          socio = socios[i]           
      if socio == None :
        print('este usuario no existe')
        exit()
      print("libros:")
      for libro in libros :
        print(libro)
      nombre_libro = input('Ingrese el nombre del libro a retirar')
      for i in range(len(libros)) :
        if nombre_libro == libros[i].get_nombre() :
          libro_a_retirar = libros[i]
      if libro_a_retirar.get_adulto() :
        if socio.calcularMayoriaEdad() :
          print('Puedes retirar el libro')
        else :
          print('debes ser mayor de edad para retirar este libro')
      else :
        print('Puedes retirar el libro')

if __name__ == '__main__' :
  main()
