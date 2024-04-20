# Inicio del programa
#subete njdaaaaas
# Constructor de la clase cuenta
class Cuenta:
    def __init__(self, titular='', cuenta='', saldo=0):
        self.__titular = titular
        self.__cuenta = cuenta
        self.__saldo = saldo

    # Métodos get
    def get_titular(self):
        return self.__titular

    def get_cuenta(self):
        return self.__cuenta

    def get_saldo(self):
        return self.__saldo

    # Métodos set
    def set_titular(self, titular):
        self.__titular = titular

    def set_cuenta(self, cuenta):
        self.__cuenta = cuenta

    # Metodo para depositar dinero
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            return f"Depósito exitoso. Saldo actual: {self.__saldo}"
        else:
            return "Cantidad a depositar debe ser positiva."

    # Metodo para retirar dinero
    def retirar(self, cantidad):
        self.__saldo -= cantidad
        return f"Retiro exitoso. Saldo actual: {self.__saldo}"

# Ingreso de Datos
a = input("Desea crear una nueva cuenta (s/n): ")

while a.lower() == "s":
    titular = input("Indique el nombre del titular: ")
    cuenta = input("Indique el número de cuenta: ")
    saldo = float(input("Indique el saldo inicial: "))
    nuevo = Cuenta(titular, cuenta, saldo)
    transaccion = input("Desea ingresar o retirar dinero (i/r): ").lower()
    
    while transaccion == "i" or transaccion == "r":
        
        if transaccion == "i":
            monto = float(input("Indique el monto que desea ingresar:"))
            print(nuevo.depositar(monto))

        else:
            monto = float(input("Indique el monto que desea retirar:"))
            print(nuevo.retirar(monto))
        transaccion = input("Desea realizar otra transacción (i/r/n): ").lower()

    a = input("Desea crear otra cuenta (s/n): ").lower()


















