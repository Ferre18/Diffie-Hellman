from algoritmo import *

print("----- INICIALIZAR VALORES -----")
print("q = 353")
print("alfa = 3")
print()
DH1 = DiffieHellman(353,3)
DH2 = DiffieHellman(353,3)

print("----- GENERAR CLAVE SECRETA -----")
DH1.generar_clave_secreta(DH2.compartir_clave_publica())
print("Clave de DH1: " + str(DH1.compartir_clave_secreta()))
DH2.generar_clave_secreta(DH1.compartir_clave_publica())
print("Clave de DH2: " + str(DH2.compartir_clave_secreta()))
print()

print("------ CIFRADO/DESCIFRADO ------")
mensaje = "Diffie Hellman"
cifrado = DH1.cifrar_xor(mensaje)
print("DH1 cifrando...")
print(mensaje + " -> " + str(cifrado))
mensaje_descifrado = DH2.descifrar_xor(cifrado)
print("DH2 descifrando...")
print(str(cifrado) + " -> " + mensaje_descifrado)

