# la función def llamada cajero_automatico() da la funcionalidad al ATM
def cajero_automatico():
#Se ponen las variables
#intentos: Se establece en 3 y representa el número de intentos permitidos para ingresar la contraseña
    
#clave_correcta: Esta variable contiene la contraseña correcta para acceder al cajero automático
    
##saldo_cuenta: Esta variable representa el saldo de la cuenta del usuario y se inicia en 9999
    
#saldo_banco: Esta variable representa el saldo total del banco y se establece en 10000.0
    intentos = 3
    clave_correcta = 9856
    saldo_cuenta = 9999
    saldo_banco = 10000.0
#Encabezado para que se vea que se está utilizando el ATM
    
    print("-------CAJERO AUTOMATICO-------")
    
#while que permite al usuario ingresar su contraseña hasta que agote sus 3 intentos o ingrese la contraseña correcta.
    #while es una estructura de control  que se utiliza para crear bucles o ciclos.
    #Su función principal es repetir un bloque de código mientras una condición especificada sea verdadera.
    
    while intentos > 0:

#las siguientes 3 le piden al usuario que ingrese su contraseña y
#muestran el número de intentos restantes.
#La contraseña ingresada por el usuario se almacena en la variable clave.
        
        print("Ingrese su contraseña")
        print(f"{intentos} Intentos")
        clave = int(input())

#Se reduce en 1 el número de intentos restantes después de cada intento fallido.
        intentos -= 1

#Se verifica si la contraseña ingresada (clave) es igual a la contraseña correcta (clave_correcta).
#if es una estructura de control  que se utiliza para tomar decisiones en función de una condición.
#Si la clave es correcta se prosigue con el programa.
#Si la contraseña es correcta, se muestra un mensaje de bienvenida
#y se le pide al usuario que elija una de las opciones disponibles.
#Si la clave es incorrecta y se fallan los 3 intentos no prosigue el programa.
        if clave == clave_correcta:
            print("BIENVENIDO")
            print("ELIJA UNA DE LAS OPCIONES")

#El break se utiliza para salir del bucle while una vez que el usuario ha ingresado la contraseña correcta.
            break

        #Si la contraseña es incorrecta, pero todavía quedan intentos, se ejecuta este bloque de código.
        #elif se utiliza  para agregar condiciones adicionales a una serie de declaraciones if.
        #Se utiliza cuando se tiene múltiples condiciones que se desea evaluar en orden y se quiere que solo una de ellas sea verdadera.
        elif intentos > 0:

            #Se muestra el mensaje que la contraseña es incorrecta
            print("CLAVE INCORRECTA")

            #Se muestra un mensaje de error si la contraseña es incorrecta
            #else se utiliza para manejar el caso en el que ninguna de las condiciones anteriores se cumple.
        else:

            #Este bloque de código se ejecuta si se agotan todos los intentos de ingreso de la contraseña.
            #sale un mensaje de cuenta bloqueada
            print("CUENTA BLOQUEADA")
            print("----------SE LE HA TOMADO UNA FOTO POR MEDIDAS DE SEGURIDAD------")

            #return se utiliza para finalizar la función cajero_automatico() en este punto y salir del programa.
            return

        
#Se abre el menú principal en caso que la contraseña sea correcta 
    print("PONER EL NUMERO DE CUAL OPCION QUIERE:")
    print("1.- RETIRO")
    print("2.- DEPOSITO")
    print("3.- CONSULTA")
    print("4.- CAMBIO DE CLAVE")
    print("5.- EXIT")

    #Se utiliza input() para obtener la entrada del usuario,
    #y esta entrada se almacena en la variable opcion después de convertirla a un número entero (int(input())).
    opcion = int(input())

    #Se utiliza una estructura if-elif-else para determinar qué acción realizar según la opción seleccionada por el usuario

    #Si opcion es igual a 1, el programa permite al usuario seleccionar un valor específico para retirar.
#Si opcion es igual a 2, el programa permite al usuario realizar un depósito en su cuenta.
#Si opcion es igual a 3, el programa muestra el saldo de la cuenta.
#Si opcion es igual a 4, el programa permite al usuario cambiar su contraseña.
#Si opcion es igual a 5, el programa finaliza y sale del cajero automático.
#Si opcion no coincide con ninguna de las opciones anteriores, se muestra un mensaje de "Opción inválida".

    if opcion == 1:
        print("Seleccione un valor:")
        print("1.- 20 $")
        print("2.- 40 $")
        print("3.- 60 $")
        print("4.- 100 $")
        print("5.- Otro valor")
        valor = int(input())

        if valor == 1:
            print("Su retiro es de $20")
            saldo_cuenta -= 20.0
            print("TENGA UN EXCELENTE DIA")
        elif valor == 2:
            print("Su retiro es de $40")
            saldo_cuenta -= 40.0
            print("TENGA UN EXCELENTE DIA")
        elif valor == 3:
            print("Su retiro es de $60")
            saldo_cuenta -= 60.0
            print("TENGA UN EXCELENTE DIA")
        elif valor == 4:
            print("Su retiro es de $100")
            saldo_cuenta -= 100.0
            print("TENGA UN EXCELENTE DIA")
        elif valor == 5:
            retiro = float(input("Ingrese la cantidad que desea retirar (múltiplo de 5): "))
            if retiro % 5 == 0 and retiro <= saldo_cuenta:
                saldo_cuenta -= retiro
                print(f"Su retiro es de ${retiro}")
                print("TENGA UN EXCELENTE DIA")
            else:
                print("Monto no válido o falta de fondos")
        else:
            print("Opción inválida")

    elif opcion == 2:
        print(f"Su dinero Actual es: ${saldo_cuenta}")
        deposito = float(input("CUANTO DINERO DESEA DEPOSITAR: "))
        saldo_cuenta += deposito
        print(f"Su dinero Actual es: ${saldo_cuenta}")
        print("TENGA UN EXCELENTE DIA")

    elif opcion == 3:
        print(f"Su dinero es: ${saldo_cuenta}")
        print("TENGA UN EXCELENTE DIA")

    elif opcion == 4:
        print("-----CAMBIO DE CLAVE-----")
        nueva_clave = int(input("INGRESE LA NUEVA CLAVE (máximo 4 dígitos): "))
        if 1000 <= nueva_clave <= 9999:
            clave_correcta = nueva_clave
            print("CLAVE CAMBIADA CORRECTAMENTE")
            print(f"Clave nueva: {nueva_clave}")
        else:
            print("Clave no válida")
        print("TENGA UN EXCELENTE DIA")

    elif opcion == 5:
        print("GRACIAS POR PREFERIRNOS")
        print("TENGA UN EXCELENTE DIA")

    else:
        print("Opción inválida")

#Se define una función llamada main(). Esta función tiene la lógica principal del programa.
#En este caso, la función main() simplemente llama a la función cajero_automatico(),
#que es la función que contiene toda la lógica para el cajero automático.
def main():
    cajero_automatico()
    
#e utiliza la línea if __name__ == "__main__": para verificar si el script se está ejecutando como el programa principal
#Esto es importante porque a veces quieres reutilizar funciones definidas en un script en otros programas sin que se ejecuten automáticamente.
#Si __name__ es igual a "__main__", significa que el script se está ejecutando como el programa principal

if __name__ == "__main__":
    main()

