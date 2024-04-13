from datetime import datetime
class Socio:
    def __init__ (self,nombre, dni, email, telefono, fecha_nacimiento, domicilio, fecha_inscripcion, estado : bool):
            self.__nombre=nombre
            self.__dni=dni
            self.__email  = email
            self.__telefono = telefono
            self.__fecha_nacimiento = fecha_nacimiento
            self.__domicilio = domicilio
            self.__fecha_inscripcion = fecha_inscripcion
            self.__estado = estado
    
    
    def setNombre(self, nombre):
        if type(nombre) != str or nombre.isdigit() == True:
            print("Ingrese una cadena de texto por favor")
            exit()
        self.__nombre = nombre
        
    
    def getNombre(self):
        return self.__nombre

    def setDni(self, dni):
        if type(dni) != str or dni.isdigit() == False:
            print("Ingrese un valor numerico por favor")
            exit()
        self.__dni = dni

    def getDni(self):
        return self.__dni

    def setEmail(self, email):
        if type(email) != str or "@" in email == False:
            print("Ingrese un formato de email valido por favor")
            exit()
        self.__email = email

    def getEmail(self):
        return self.__email
    
    def setTelefono(self, telefono):
        if type(telefono) != str or telefono.isdigit() == False:
            print("Ingrese un numero de telefono valido por favor")
            exit()
        self.__telefono = telefono

    def getTelefono(self):
        return self.__telefono
    
    def setFechaNacimiento(self, fecha_nacimiento):
        if type(fecha_nacimiento) != str or "/" in fecha_nacimiento == False:
            print("Ingrese una fecha de nacimiento valida por favor")
            exit()
        self.__fecha_nacimiento = fecha_nacimiento

    def getFechaNacimiento(self):
        return self.__fecha_nacimiento
    
    def setDomicilio(self, domicilio):
        if type(domicilio) != str :
            print("Ingrese un domicilio valido por favor")
            exit()
        self.__domicilio = domicilio

    def getDomicilio(self):
        return self.__domicilio
    
    def setFechaInscripcion(self, fecha_inscripcion):
        if type(fecha_inscripcion) != str or "/" in fecha_inscripcion == False:
            print("Ingrese una fecha de inscripcion valida por favor")
            exit()
        self.__fecha_inscripcion = fecha_inscripcion

    def getFechaInscripcion(self):
        return self.__fecha_inscripcion

    def setEstado(self, estado):
        if type(estado) != bool :
            print("Ingrese un valor booleano por favor")
            exit()
        self.__estado = estado

    def getEstado(self):
        return self.__estado
    

    def calcularMayoriaEdad(self):
        nacimiento = self.__fecha_nacimiento.split("/")
        fecha = str(datetime.now()).split(" ")[0].split("-")
        dias_nacimiento = int(nacimiento[0]) + int(nacimiento[1])* 30 + int(nacimiento[2]) * 365
        dias_fecha = int(fecha[2]) + int(fecha[1]) * 30 + int(fecha[0]) * 365
        edad_my = round((dias_fecha - dias_nacimiento)/365,2)
        if edad_my >= 18:
            return True
        else: return False


    def __str__(self):
        return f"{self.__nombre}\n{self.__edad}\n{self.__dni}\n{self.__email}\n{self.__telefono}\n{self.__fecha_nacimiento}\n{self.__domicilio}\n{self.__fecha_inscripcion}\n{self.__estado}"
