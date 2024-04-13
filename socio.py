from datetime import datetime
class Socio:
    def __init__ (self,nombre, dni, email, telefono, fecha_nacimiento, domicilio, fecha_inscripcion, estado):
            self.__nombre=nombre
            self.__dni=dni
            self.__email  = email
            self.__telefono = telefono
            self.__fecha_nacimiento: datetime = fecha_nacimiento
            self.__domicilio = domicilio
            self.__fecha_inscripcion: datetime = fecha_inscripcion
            self.__estado: bool = estado
        
    @property        
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        if type(nombre) != str or nombre.isdigit():
            print("Ingrese una cadena de texto por favor")
            exit()
        self.__nombre = nombre
    @property    
    def dni(self):
        return self.__dni
    @dni.setter
    def dni(self, dni):
        if type(dni) != str or not dni.isdigit():
            print("Ingrese un valor numerico por favor")
            exit()
        self.__dni = dni
    @property
    def mail(self):
        return self.__email
    @mail.setter
    def mail(self, email):
        if type(email) != str or not "@" in email:
            print("Ingrese un formato de email valido por favor")
            exit()
        self.__email = email
    @property
    def telefono(self):
        return self.__telefono
    @telefono.setter
    def telefono(self, telefono):
        if type(telefono) != str or not telefono.isdigit():
            print("Ingrese un numero de telefono valido por favor")
            exit()
        self.__telefono = telefono
    @property
    def fechaNacimiento(self):
        return self.__fecha_nacimiento
    @fechaNacimiento.setter
    def fechaNacimiento(self, fecha_nacimiento):
        if type(fecha_nacimiento) != datetime:
            print("Ingrese una fecha de nacimiento valida por favor")
            exit()
        self.__fecha_nacimiento = fecha_nacimiento
    @property
    def domicilio(self):
        return self.__domicilio
    @domicilio.setter
    def domicilio(self, domicilio):
        if type(domicilio) != str:
            print("Ingrese un domicilio valido por favor")
            exit()
        self.__domicilio = domicilio
    @property
    def fechaInscripcion(self):
        return self.__fecha_inscripcion
    @fechaInscripcion.setter
    def fechaInscripcion(self, fecha_inscripcion):
        if type(fecha_inscripcion) != datetime:
            print("Ingrese una fecha de inscripcion valida por favor")
            exit()
        self.__fecha_inscripcion = fecha_inscripcion
    @property
    def estado(self):
        return self.__estado
    @estado.setter
    def estado(self, estado):
        if type(estado) != bool :
            print("Ingrese un valor booleano por favor")
            exit()
        self.__estado = estado
    def calcularMayoriaEdad(self):
        FECHA_ACTUAL = datetime.now()
        EDAD = (FECHA_ACTUAL - self.__fecha_nacimiento).days / 365.25 
        return EDAD >= 18

    def __str__(self):
        return f"{self.__nombre}\n{self.__edad}\n{self.__dni}\n{self.__email}\n{self.__telefono}\n{self.__fecha_nacimiento}\n{self.__domicilio}\n{self.__fecha_inscripcion}\n{self.__estado}"

