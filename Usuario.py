"""
1. Crear una clase Usuarios
2. Atributos: nombre, edad, CURP
3. Validar que CURP sea de 18 caracteres exactamente
4. Definir un metodo que muestre los datos del usuario (atributos definidos)
5. Definir un metodo que valide que la edad del usuario es mayor o igual a 18

"""
import os

class Usuario:
    def __init__(self, nombre, edad, curp):
        self.__nombre = nombre
        if self.validar_edad(edad) == None:
            return "Edad invalida"
        self.__edad = edad
        if self.validar_curp(curp) == None:
            return "CURP invalido"
        self.__curp = curp

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        if self.validar_edad(edad):
            self.__edad = edad
        else:
            print("Edad invalida")

    def get_curp(self):
        return self.__curp

    def set_curp(self, curp):
        if self.validar_curp(curp):
            self.__curp = curp

    def validar_curp(self, curp):
        if len(curp) == 18:
            return curp

    def mostrar_datos(self):
        return f"Nombre: {self.__nombre}\nEdad: {self.__edad}\nCURP: {self.__curp}"

    def validar_edad(self, edad):
        if edad >= 18:
            return edad


if __name__ == "__main__":
    os.system('cls')
    usuario_1 = Usuario("Miguel", 18, "123456789123456789")
    print(usuario_1.mostrar_datos(), "\n")