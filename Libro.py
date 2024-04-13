class Libro:
  def __init__(self, nombre, estado, genero, autor, codigo, esParaAdultos):
    self.__nombre: str = nombre
    self.__estado: bool = estado
    self.__genero: str = genero
    self.__autor: str = autor
    self.__codigo: str = codigo
    self.__esParaAdultos: bool = esParaAdultos
  @property
  def nombre(self) :
    return self.__nombre
  @property
  def estado(self) :
    return self.__estado
  @property
  def genero(self) :
    return self.__genero
  @property
  def autor(self) :
    return self.__autor
  @property
  def codigo(self) :
    return self.__codigo
  @property
  def esParaAdultos(self):
    return self.__esParaAdultos
  @esParaAdultos.setter
  def set_esParaAdultos(self, esParaAdultos) :
    if type(esParaAdultos) != bool :
      print('Ingrese un valor booleano')
      exit()
    self.__esParaAdultos = esParaAdultos
  @nombre.setter
  def set_nombre(self, nombre) :
    try: 
      self.__nombre = str(nombre)
    except :
      print('El tipo de valor ingresado debe ser una cadena')
  @estado.setter
  def set_estado(self, estado) :
    if type(estado) != bool :
      print('Ingrese un valor booleano')
      exit()
    self.__estado = estado
  @genero.setter
  def set_genero(self, genero) :
    try: 
      self.__genero = str(genero)
    except :
      print('El tipo de valor ingresado debe ser una cadena')
  @autor.setter
  def set_autor(self, autor) :
    try: 
      self.__autor = str(autor)
    except :
      print('El tipo de valor ingresado debe ser una cadena')
  @codigo.setter
  def set_codigo(self, codigo) :
    try: 
      self.__codigo = str(codigo)
    except :
      print('El tipo de valor ingresado debe ser una cadena')

  def __str__(self) :
    return f'nombre: {self.__nombre}'
