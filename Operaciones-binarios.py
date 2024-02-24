# Programa que permite el ingreso de números binarios, enteros y hexadecimales; realizando las operaciones correspondientes
# Estuardo Andrés Castro Bonifaz 23890
# Ángel de Jesús Mérida Jiménez 23661

#Función para entero a binario
def entero_a_binario():
    num = int(input("Ingresa un número entero: "))
    if num >= 0 and num <= 256:
        binario = format(num, '08b')
        print(f"El número binario de 8 bits es: {binario}")
    else:
        print("El número debe estar en el rango de 0 a 255.")

def binario_a_complemento_dos():
    num = input("Ingresa un número binario de 8 bits: ")
    #Acetar valores 0 y 1
    if len(num) == 8 and all(c in '01' for c in num):
        if num[0] == '1':
            num = ''.join('1' if bit == '0' else '0' for bit in num)
            num = bin(int(num, 2) + 1)[2:]
        print(f"La representación en complemento a dos es: {num}")
    else:
        print("Por favor, ingresa un número binario de 8 bits, 0 y 1.")

def hexadecimal_a_decimal():
    num = input("Ingresa un número hexadecimal de 3 dígitos: ")
    # Aceptar características  del 0 al 9 y del a a la f, tanto en minúsculas como mayúsculas  
    if len(num) == 3 and all(c in '0123456789abcdefABCDEF' for c in num):
        decimal = int(num, 16)
        print(f"El número decimal es: {decimal}")
    else:
        print("Por favor, ingresa un número hexadecimal de 3 dígitos.")


def decimal_a_hexadecimal():
    # Solicita al usuario uqe ingrese un número decimal
    num = int(input("Ingresa un número decimal: "))
    # verifica si el número ingresado es menor o igual a 4095. 
    #Esto se debe a que solo se pueden representar números hasta 4095 con tres dígitos hexadecimales.
    if num <= 4095:
        # La cadena de formato '03x' se utiliza para asegurar que el número hexadecimal tenga exactamente tres dígitos
        hexadecimal = format(num, '03x')
        print(f"El número hexadecimal es: {hexadecimal}")
    else:
        print("El número no puede ser representado con 3 dígitos hexadecimales")

#Menú 
def menu():
    while True:
        print("Bienvenido, por favor ingresa una opción para realizar una operación: ")
        print("\n1. Convertir entero a binario de 8 bits")
        print("2. Convertir binario de 8 bits a complemento a dos")
        print("3. Convertir hexadecimal de 3 dígitos a decimal")
        print("4. Convertir decimal a hexadecimal de 3 dígitos")
        print("5. Salir")
        opcion = int(input("Selecciona una opción: "))
        if opcion == 1:
            entero_a_binario()
        elif opcion == 2:
            binario_a_complemento_dos()
        elif opcion == 3:
            hexadecimal_a_decimal()
        elif opcion == 4:
            decimal_a_hexadecimal()
        elif opcion == 5:
            print("Gracias por usar mi programa .")
            break
        else:
            print("Opción no válida, ingrese una opción correcta.")

# Llamada a la función del menú
menu()
