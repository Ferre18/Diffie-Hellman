from funciones_auxiliares import *

class DiffieHellman :
    
    def __init__(self, q, alfa):

        if not(es_primo(q)):
            print("ERROR: q no es primo")
            exit(-1)

        if not(es_raiz_primitiva(alfa, q)):
            print("ERROR: alfa no es raiz primitiva de q")
            exit(-1)

        self.__q__ = q
        self.__alfa__ = alfa

        self.__generarClaves__()

    def __generarClaves__(self):
        # X < q
        self.__clavePrivada__ = numero_aleatorio(self.__q__)
        # Y = alfa^X mod q
        self.__clavePublica__ = ( self.__alfa__ ** self.__clavePrivada__ ) % self.__q__

    def compartir_clave_publica(self):
        return self.__clavePublica__

    def generar_clave_secreta(self, clavePublicaB):
        # K = Yb^Xa mod q
        self.__claveSecreta__ = ( clavePublicaB ** self.__clavePrivada__ ) % self.__q__

    # Este metodo solo se utiliza para comprobar
    # que ambas claves secretas son iguales.
    # Las claves secretas no se deben compartir.
    def compartir_clave_secreta(self):
        return self.__claveSecreta__
    
    # Cifrar un mensaje usando XOR y la clave secreta
    def cifrar_xor(self, mensaje):
        cifrado = [char ^ self.__claveSecreta__ for char in mensaje.encode()]
        return bytes(cifrado)

    # Cifrar un mensaje usando XOR y la clave secreta
    def descifrar_xor(self, cifrado):
        mensaje = ''.join([chr(char ^ self.__claveSecreta__) for char in cifrado])
        return mensaje
