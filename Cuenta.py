"""
1. Crear clase Cuenta
2. Para poder crear una 
  cuenta es necesario pasarle su respectivo usuario.
3. El deposito inicial de apertura es opcional
4. Crear metodos retirar() y deposito() de los atributos que
  solo seran modificables a traves de los metodos publicos.
5. Crear un metodo mostrar_datos() que muestre
  nombre de usuario y balance total.
"""
import os
from Usuario import Usuario


class Cuenta:
    def __init__(self, usuario: Usuario, balance=0):
        self.__usuario = usuario
        self.__balance = balance

    def deposito(self, balance):
        if balance > 0:
            self.__balance += balance

    def retirar(self, retiro):
        if self.validar_retiro(retiro):
            self.__balance -= retiro
        else:
            print("Saldo insuficiente\n")

    def validar_retiro(self, retiro):
        if retiro <= self.__balance:
            return True

    def mostrar_balance(self):
        return f"balance total: {self.__balance}" 
    
    def get_balance(self):
        return self.__balance


if __name__ == "__main__":
  os.system('cls')
  usuario_1 = Usuario("Miguel", 18, "123456789123456789")
  cuenta_1 = Cuenta(usuario_1, 1000)
  cuenta_1.retirar(9999)
  print(usuario_1.mostrar_datos(), "\n")
  print(cuenta_1.mostrar_balance(),"\n")