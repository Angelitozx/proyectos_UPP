import os
from Usuario import Usuario
from Cuenta import Cuenta


class CuentaJoven(Cuenta):
    def __init__(self, usuario: Usuario, bonificacion=0,balance=0):
        super().__init__(usuario)
        self.__bonificacion = bonificacion

    def retirar(self, retiro):
        if self.__validar_edad():
            super().retirar(retiro)
        else:
            print("No se puede retirar de una cuenta joven si el titular es mayor de 25 años")

    def mostrar_balance(self):
        return f"Cuenta Joven - balance total: {self.get_balance() + self.__calcular_bonificacion()}"

    def __validar_edad(self):
        edad = self._Cuenta__usuario.get_edad()
        if 18 <= edad <= 25:
            return True
        return False

    def __calcular_bonificacion(self):
        return self.get_balance() * (self.__bonificacion / 100)



os.system('cls')
usuario_joven = Usuario("Juan Pérez", 22, "PEJU910531HDFRRN02")
cuenta_joven = CuentaJoven(usuario_joven, balance=1000, bonificacion=0.1)
cuenta_joven.deposito(500)
cuenta_joven.retirar(200)
print("Datos de la cuenta joven: \n ")
print(usuario_joven.mostrar_datos (),"\n")
print(cuenta_joven.mostrar_balance (),"\n")