class Libro:
  def __init__(self, nombre: str, estado: bool, genero: str, autor: str, codigo: str|int, adulto: bool) :
    self.__nombre = nombre
    self.__estado = estado
    self.__genero = genero
    self.__autor = autor
    self.__codigo = codigo
    self.__adulto = adulto

  def get_nombre(self) :
    return self.__nombre
  def get_estado(self) :
    return self.__estado
  def get_genero(self) :
    return self.__genero
  def get_autor(self) :
    return self.__autor
  def get_codigo(self) :
    return self.__codigo
  def get_adulto(self) :
    return self.__adulto

  def set_adulto(self, adulto) :
    if type(adulto) != bool :
      print('Ingrese un valor booleano')
      exit()
    self.__adulto = adulto
  def set_nombre(self, nombre) :
    try: 
      self.__nombre = str(nombre)
    except :
      print('El tipo de valor ingresado debe ser una cadena')
  def set_estado(self, estado) :
    if type(estado) != bool :
      print('Ingrese un valor booleano')
      exit()
    self.__estado = estado
  def set_genero(self, genero) :
    try: 
      self.__genero = str(genero)
    except :
      print('El tipo de valor ingresado debe ser una cadena')
  def set_autor(self, autor) :
    try: 
      self.__autor = str(autor)
    except :
      print('El tipo de valor ingresado debe ser una cadena')
  def set_codigo(self, codigo) :
    try: 
      self.__codigo = str(codigo)
    except :
      print('El tipo de valor ingresado debe ser una cadena')

  def __str__(self) :
    return f'nombre: {self.__nombre}'

